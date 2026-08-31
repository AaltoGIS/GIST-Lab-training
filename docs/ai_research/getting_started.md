# Getting started with Claude Code

Claude Code is the coding agent this half of the theme is mostly about. You can run
it in more than one place; which one to use depends on the work.

## Where to run it

**In the terminal.** The command-line version runs where your code lives. It is the
most direct way to use Claude Code on a real project — point it at a repository and
it can read, edit, run, and test across the whole thing. Start here for development
work.

**In VS Code (or another IDE).** The editor extension runs the same agent inside
your editor, so its edits show up as diffs you can review in place and file
references are one click away. Use it when you are already working in the IDE.

**Claude Desktop.** The desktop app is the chat-style Claude, not the coding agent.
It suits work that is not tied to a code repository — thinking through a problem,
drafting, working with documents and PDFs, and connecting to tools through MCP.
Reach for it for the writing, literature, and brainstorming uses from
{doc}`What you can use AI and agents for <what_you_can_use_ai_for>`.

The account is the same across all three, so you can move between them.

## Install it

You do this once per surface. The commands change, so if one below fails, use the
current [Claude Code install docs](https://code.claude.com/docs/en/setup).

- **The CLI (terminal).** The recommended install is the native installer, which
  keeps itself up to date.

  macOS, Linux, or WSL:

  ```bash
  curl -fsSL https://claude.ai/install.sh | bash
  ```

  Windows PowerShell:

  ```powershell
  irm https://claude.ai/install.ps1 | iex
  ```

  Windows CMD:

  ```batch
  curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
  ```

  On native Windows, also install [Git for Windows](https://git-scm.com/downloads/win)
  so Claude Code has a Bash shell to run commands in. Package managers work too —
  Homebrew (`brew install --cask claude-code`) or WinGet
  (`winget install Anthropic.ClaudeCode`) — but those do not update themselves. Then
  run `claude` in a project and, when the browser prompt appears, sign in with the
  lab's **Claude Team** account, not a personal one — the difference decides whether
  your prompts can be used for training
  ({doc}`Data protection and privacy <data_protection>`).
- **The VS Code extension.** Install it from the VS Code Marketplace — open Extensions,
  search for "Claude Code," and click Install — then authenticate when prompted. It
  works on its own; you do not need the CLI first. Details are in the
  [extension docs](https://code.claude.com/docs/en/vs-code).
- **Claude Desktop.** Download the app from <https://claude.com/download> (macOS,
  Windows, and Linux in beta), install it, and sign in with the same Claude account.
- **Apply the lab's baseline configuration.** Once the CLI works, clone the lab's
  repository, [github.com/AaltoGIS/gist-lab-ai](https://github.com/AaltoGIS/gist-lab-ai),
  and run `scripts/install-claude-config.sh` from it to get the permissions, safety
  hook, and sandbox described in {doc}`Rules and safety <rules_and_safety>`. The
  exact commands, which also install the lab's skills, are in
  {doc}`Skills <skills>`. Restart Claude Code afterward so the configuration loads.

:::{note}
Install commands and download links change. If a step here does not match what you
see, trust the [official install docs](https://code.claude.com/docs/en/setup) — this
page tells you *what* to install and in what order, not the exact current command.
:::

## Choosing a model

You choose which model runs your task, and the choice is a trade-off: stronger
models reason better but are slower and cost more; lighter models are faster and
cheaper. A good default is a capable general model — drop to a lighter one for
simple or bulk work, and move to the strongest available model when a problem is
hard or the quality really matters. For quality-critical work, changing the model
is only half of it; bring in a review as well (see
{doc}`Higher-quality results <higher_quality_results>`).

The available models change often, so check the
[current line-up](https://platform.claude.com/docs/en/models/overview) rather than
memorizing names.

## Fast mode

Fast mode makes Claude Code respond faster using the same top model, rather than
quietly switching you to a smaller one. Turn it on, where it is available, when you
want quicker turnaround on interactive work and don't need to wait on the deepest
reasoning.

## Your first task

- Work in a git repository, from a clean working tree, so its changes land as diffs you
  can review and undo — the baseline for any coding agent
  ({doc}`Rules and safety <rules_and_safety>`).
- Open Claude Code in your project directory.
- Give it context — a `CLAUDE.md` describing the project and how you work is the
  usual way (see {doc}`Teaching Claude who you are <teaching_claude>`).
- Start with one small, well-scoped task rather than a vague request.
- Review what it did before you accept it — the {doc}`Using AI well <using_ai_well>`
  rule applies from the first command.

Before you let it loose on a real project, read
{doc}`Rules and safety <rules_and_safety>`.
