# Rules and safety

An agent that can edit files and run commands is useful precisely because it acts on
its own. That also means you have to decide what it may do without asking, what needs
your approval, and what it must never do. Claude Code gives you layered controls for
this, and the shared baseline configuration means you do not start from nothing. This
page shows what each control is, what the baseline sets it to, and how to adjust it.

## Work inside version control

The controls in the rest of this page limit what an agent may do; version control is
what lets you undo what it did — so start there. Run the agent inside a **git
repository**, from a clean working tree (everything committed or stashed). Changes to
tracked files then show up as diffs you can read, keep, or discard; new (unignored)
files show up in `git status`; and if a run goes wrong you can restore files or return
to an earlier commit. Commit good states as you go, so you always have a recent point to
fall back to. This is what makes an agent's edits across many files easy to review and
undo — without it, seeing what changed and reversing it is far harder.

## Where the settings live

All of the controls below are JSON in a settings file. There are three, and which one
you edit decides who the rule applies to:

| File | Applies to | Shared? |
| :--- | :--- | :--- |
| `~/.claude/settings.json` | you, in every project | no — personal |
| `.claude/settings.json` in a project | everyone working in that project | yes — commit it |
| `.claude/settings.local.json` in a project | you, in that project only | no — gitignored |

The lab's baseline is the first one: it is installed into your user settings (see
{doc}`Getting started <getting_started>`). Project-specific rules — your test runner,
a build command — go in the project file so collaborators get them too. You can also
view and edit rules inside a session with the `/permissions` command instead of opening
the file. The full list of keys is in the
[settings reference](https://code.claude.com/docs/en/settings-reference).

## Permissions: allow, ask, deny

The first control is a set of **permission rules** that decide, for each kind of
action, whether the agent:

- **allows** it — runs without asking, for routine actions you have chosen to permit;
- **asks** you first — for actions you want to review each time; or
- is **denied** — refused outright, for actions it must never take.

A rule names a tool and a pattern: `Bash(git log *)` matches any `git log` command,
`Read(~/.ssh/**)` matches reading anything under `~/.ssh`, `WebFetch(domain:pypi.org)`
matches fetching from that domain. The `*` goes after the subcommand — `Bash(git *)`
would allow *every* git command. Rules are checked in the order **deny, then ask, then
allow**, and the first match wins, so a deny rule cannot be carved out by a narrower
allow. This is the permissions block of the lab's baseline, trimmed to the rules that
matter here:

```json
{
  "permissions": {
    "allow": [
      "Bash(ls *)", "Bash(cat *)", "Bash(grep *)", "Bash(rg *)", "Bash(find *)",
      "Bash(git status)", "Bash(git diff *)", "Bash(git log *)", "Bash(git branch *)",
      "Bash(git add *)", "Bash(git commit *)", "Bash(git fetch *)", "Bash(git stash *)",
      "Bash(python3 -m pytest *)",
      "WebFetch(domain:code.claude.com)",
      "WebFetch(domain:docs.python.org)",
      "WebFetch(domain:github.com)",
      "WebFetch(domain:pypi.org)"
    ],
    "ask": [
      "Bash(git push *)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Bash(git push --force *)",
      "Bash(git push -f *)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)",
      "Read(**/.env)",
      "Read(**/.env.*)"
    ],
    "defaultMode": "auto"
  }
}
```

Read it as three decisions:

- **Allow the routine.** Listing and searching files, and the git commands that
  publish nothing — status, diff, log, add, commit, fetch, stash — run without a
  prompt. So does running the tests. Fetching from a handful of documentation and
  package sites is allowed because the agent needs them constantly and a fetch only
  pulls a page in.
- **Ask before anything leaves your machine.** `git push` always prompts, even in
  auto mode: it is the human checkpoint before changes leave your machine. Fetching
  from a domain not on the allow list prompts too — only the listed sites are silent.
- **Deny the irreversible and the secret.** Recursive force-delete and force-push are
  refused outright, and the `Read` tool may never open SSH keys, cloud credentials, or
  `.env` files (the sandbox's `denyRead`, below, extends that to shell commands). Deny
  rules are checked before everything else, including auto mode.

Add your own *allows* for the tools of a given project — a `Bash(make *)`, a
`Bash(python3 scripts/*)`. Treat the deny list as a floor you do not lower. Details
and the full rule syntax are in the
[permissions docs](https://code.claude.com/docs/en/permissions).

## Permission modes

Rules say what happens per action. The **permission mode** sets a session's default
behaviour for everything the rules do not name; switch it with `Shift+Tab` in the
terminal, or from the mode selector in VS Code and the desktop app.

| Mode | What runs without asking |
| :--- | :--- |
| `default` (labelled *Manual*) | Only what an allow rule covers; everything else prompts. |
| `acceptEdits` | Also file edits inside the project — you review them as diffs. |
| `plan` | Reads and explores only; does not edit your project files. |
| `auto` | Most actions, after a second model checks each one against your request (below). Deny and ask rules still apply first. |

The lab's baseline sets `"defaultMode": "auto"`, which is also where Pro, Max, and
Team sessions start. Use `plan` when you want a proposal before any change. The
[permission modes page](https://code.claude.com/docs/en/permission-modes) describes each
in full.

## The layers underneath

Permission rules are the everyday control, but pattern rules alone leave gaps. The
lab's baseline stacks three more, because no single one covers everything:

1. **A safety hook** — a small script that inspects every shell command before it runs
   and hard-blocks destructive patterns that rules miss.
2. **Auto mode** — the classifier that judges routine actions for you, with your own
   rules for what is trusted and what is off-limits.
3. **An OS sandbox** — the operating system itself limits what a sandboxed command
   can read, write, and connect to, whatever the layers above allowed.

They cover different gaps, which is why the baseline enables all of them rather than
relying on one.

### The safety hook

A **hook** is a script Claude Code runs at a given moment — here, *before each Bash
command*. The script gets the command as JSON on standard input; if it exits with
code 2, the command is blocked and the reason is shown to the agent. You register it
in the settings:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "~/.claude/hooks/block-bypass.py" }
        ]
      }
    ]
  }
}
```

Why a script when there are deny rules? Because a rule matches text. `Bash(rm -rf *)`
catches `rm -rf` and nothing else — not `rm -fr`, `rm -Rf`, or `rm -r -f`, all of which
do the same thing. The hook parses the arguments and blocks the *operation* in any of
those spellings. A blocking hook also wins over allow rules, so it is the right place
for a block that must hold even when an allow rule matches. The lab's hook blocks:

- git operations that lose work or rewrite history: force-push in any form, `commit
  --no-verify`, `reset --hard`, `clean -f`, `branch -D`, deleting tags, `filter-branch`;
- filesystem damage: `rm` with recursive *and* force flags in any combination, `dd` to
  a disk device, `mkfs`, `shred`, `chmod 777`;
- destructive SQL from database clients: `DROP`, `TRUNCATE`, `DELETE` without a
  `WHERE`;
- container clean-ups that discard data: `docker rm -f`, volume and system `prune`,
  `compose down -v`;
- the same patterns sent over `ssh`, and `scp`/`rsync` of credential files or to hosts
  outside an allowlist.

Every block names the reason and, where one exists, a less destructive alternative
(`--soft` instead of `--hard`, `-d` instead of `-D`). If you genuinely need one of these, run it
yourself outside Claude Code. The
[hooks guide](https://code.claude.com/docs/en/hooks-guide) shows how to write your own,
and the [hooks reference](https://code.claude.com/docs/en/hooks) has the exact
interface.

### Auto mode

In auto mode a second model, the **classifier**, reviews each action instead of you. It
is meant to block anything irreversible, destructive, or aimed outside your
environment and approve the rest — a judgment that can be wrong, which is why the
other layers stay on. You tell it what your environment is and where the boundaries
are, in plain prose, in the `autoMode` block of your *user* settings (it deliberately
ignores project settings, so a repository cannot loosen its own rules). Four lists,
each keeping the built-in rules through `"$defaults"`:

```json
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Researcher at a university. Main uses: geospatial Python research code, data pipelines, documentation, and writing skills for Claude Code.",
      "Source control: github.com/<your-account> — pushing, pulling, and fetching any repo under this account is routine.",
      "Manuscripts live under ~/Documents/manuscripts/; reading and converting them is routine.",
      "HPC: SSH to the national supercomputers (CSC Puhti, Mahti) for job submission and data transfer is routine."
    ],
    "allow": [
      "$defaults",
      "Running pre-commit hooks against the working tree is routine — it is part of the commit pipeline."
    ],
    "soft_deny": [
      "$defaults",
      "Never modify in-progress manuscript files unless I name the specific file to edit.",
      "Never run data-processing scripts that overwrite raw research datasets — work on copies.",
      "Never delete research PDFs or anything under a 'My publications/' directory."
    ],
    "hard_deny": [
      "$defaults",
      "Never send research data, manuscript drafts, or unpublished code to AI services the lab has not approved.",
      "Never push to repositories outside my own GitHub account."
    ]
  }
}
```

- **`environment`** describes what is *inside* your boundary — your GitHub account,
  your data locations, the servers you use. Without it, the classifier treats a push to
  your own repository as a possible leak. This is the list most worth filling in.
- **`soft_deny`** names destructive actions it should refuse unless you *explicitly*
  ask for that exact action in the conversation.
- **`allow`** lists exceptions to soft denies that are routine for you.
- **`hard_deny`** is unconditional: no request and no allow rule overrides it.

Leaving out `"$defaults"` replaces the whole built-in list for that section, so keep
it. Run `claude auto-mode config` to print the rules actually in effect, and open
`/permissions` → *Recently denied* to see what the classifier blocked and why. If it
keeps blocking something routine, the fix is usually a missing `environment` line, not
a removed deny. Full details are in the
[auto mode configuration docs](https://code.claude.com/docs/en/auto-mode-config).

### The sandbox

Everything above decides whether a command *starts*. The **sandbox** limits what it can
*do* once running: the operating system confines each sandboxed Bash command (and
anything it spawns) — writes and network connections go through allowlists, and the
paths you list cannot be read. This is the layer that can stop a command from reading
your SSH keys or sending data out even if something upstream went wrong. It runs on
macOS, Linux, and WSL2 — not native Windows. The lab's baseline:

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "network": {
      "allowedDomains": [
        "api.anthropic.com", "*.anthropic.com", "*.claude.com",
        "github.com", "*.github.com", "*.githubusercontent.com",
        "pypi.org", "files.pythonhosted.org", "conda.anaconda.org",
        "*.aalto.fi", "*.csc.fi",
        "docs.python.org", "code.claude.com",
        "localhost", "127.0.0.1"
      ],
      "allowLocalBinding": true
    },
    "filesystem": {
      "allowWrite": ["/tmp", "~/.cache", "~/.local", "~/.claude/plans"],
      "denyRead": ["~/.ssh", "~/.aws", "~/.gnupg", "~/.netrc", "~/.config/gh"]
    },
    "excludedCommands": ["docker *", "ssh *", "scp *", "rsync *"]
  }
}
```

- **Network:** sandboxed commands can reach only the listed domains — the model API,
  GitHub, the package indexes, the university and HPC domains, and localhost for dev
  servers. Other connections are blocked, and Claude Code reports which domain so you
  can add it if it is legitimate.
- **Filesystem:** commands can write to the project directory plus the listed scratch
  locations, and cannot read the credential directories, whatever the permission rules
  say.
- **`autoAllowBashIfSandboxed`** is what removes most prompts: a command that stays
  inside the sandbox runs without asking, because the sandbox has already bounded what
  it can do — unless a deny or ask rule matches first.
- **`excludedCommands`** are tools that do not work confined — containers and remote
  shells run outside the sandbox, which is exactly why the hook watches them.

The [sandboxing docs](https://code.claude.com/docs/en/sandboxing) cover setup on Linux
and the `/sandbox` panel for checking the current state.

## Working with it

- Start from the lab's baseline configuration rather than assembling rules from
  scratch, and run `/permissions` once to see what it set.
- Add project-specific *allows* — your test runner, build tool, scripts — in the
  project's `.claude/settings.json`, so collaborators share them.
- Treat deny rules and the hook as a floor you keep. Loosen auto mode with
  `environment` lines, not by removing denies.
- When something is blocked, read the reason before working around it. A block is
  usually either a rule doing its job or a missing `environment` entry.
- Review the edits it makes through version control — auto mode speeds you up, it does
  not replace reading the diff.
- Leave the sandbox on.

:::{note}
The sandbox matters most for the case you cannot predict: a web page you fetched or a
dependency you installed trying to make the agent do something harmful. The other
layers mostly guard against honest mistakes; the sandbox is the main guard if
something is actively hostile — though none of these is an absolute guarantee on its
own.
:::
