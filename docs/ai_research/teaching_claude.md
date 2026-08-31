# Teaching Claude who you are

```{image} /_static/comic-teaching_claude.svg
:alt: Comic illustrating the “Teaching Claude who you are” section.
:width: 100%
```

An agent that knows who you are, what you are working on, and how you like to work
needs far less steering and makes fewer wrong assumptions. It is worth telling it
once, rather than repeating yourself in every session.

## The baseline: `CLAUDE.md` and memory

Claude Code reads a file called `CLAUDE.md` at the start of every session and treats
it as standing context. Use two levels:

- A **global** `CLAUDE.md`, at `~/.claude/CLAUDE.md`, for facts that hold across
  everything you do: who you are, your role, and standing preferences — how you like
  commits and pull requests, your writing conventions, the tools you rely on.
- A **project** `CLAUDE.md`, in the repository root and committed with it, for
  context specific to that project: what it is, how to build and test it, its
  conventions.

Keep both short and factual — under 200 lines, and only what the agent could not
work out from the code itself. Do not write the project one from scratch: run `/init`
in the project and Claude drafts it from what it finds, then add what it could not
have discovered. The project file for this very training site, trimmed, shows the
register:

```markdown
# CLAUDE.md

## What this repository is
A documentation-only Sphinx project: training material on testing, packaging, and
CI for Python libraries, using pyrosm as the running example. There is no package
source here — the code blocks in the .rst files are illustrative, not runnable.

## Build / preview
python -m pip install -r docs/requirements.txt
python -m sphinx -b html docs docs/_build/html
docs/_build/ is gitignored — don't commit it.

## Conventions
- Pages are wired by the toctree in docs/index.rst; adding a file alone won't
  surface it.
- Prose is second-person, defines terms in bold on first use, and grounds each
  concept in a pyrosm example.
```

Add to it whenever Claude makes the same mistake twice, or you type the same
correction you typed last session. `/memory` opens these files from inside a session,
and `/context` shows which ones actually loaded. Some tools read a project
`AGENTS.md` the same way; a `CLAUDE.md` containing the line `@AGENTS.md` imports it,
so both tools read one file. On top of these, Claude keeps **auto memory** — notes it
writes itself from your corrections and preferences, stored per project under
`~/.claude/projects/`, which you can read and edit through `/memory`. The
[memory docs](https://code.claude.com/docs/en/memory) cover all of this.

## A structured context portfolio

For the "who you are" part, it helps to write a small, structured description of
yourself once and reuse it everywhere, instead of scattering it across projects. One
workable framework is a set of ten short files, each covering one category:

*identity · role and responsibilities · current projects · team and relationships ·
tools and systems · communication style · goals and priorities · preferences and
constraints · domain knowledge · decision log*

For a doctoral researcher, that might read: **identity** — a PhD researcher in
spatial data science; **current projects** — a manuscript and a small Python
package; **team** — an advisor and two co-authors; **tools** — Python and GIS,
Claude Code, Zotero; **domain knowledge** — your subfield and its methods;
**decision log** — choices you have made and why. The aim is to capture how you
actually work, so any tool can pick it up.

Build these files by interview rather than from a blank page. The lab's repository
({doc}`Skills <skills>`) has a `context-portfolio/` folder with everything needed:

- `templates/` — one file per category, each with the interview questions an agent
  should ask you and the structure of the finished file;
- `interview-protocol/` — a system prompt that turns Claude into the interviewer, and
  a review-mode variant for polishing files you already have;
- `examples/` — complete example portfolios for fictional researchers, to see what a
  finished one reads like.

The procedure is short. Open a template — start with `identity.md`, then
`role-and-responsibilities.md`; the others build on those two — paste it to Claude,
and say "let's do this one." It interviews you, drafts the file, you correct what it
got wrong, and you save it. Ten files takes an hour or two, spread over a few sittings.

## Advanced: serve it as a read-only MCP server

Copying the same context into every tool lets it drift out of date. Instead, you can
serve your context files as read-only **resources** through a small local MCP server,
so Claude Code, Claude Desktop, and other tools all read one source. The lab's
`portfolio-mcp/` (in the same repository) does exactly this: it serves the ten files
as `portfolio://identity`, `portfolio://current-projects`, and so on. It runs with
[uv](https://docs.astral.sh/uv/), and registering it with Claude Code is one command —
absolute paths, because the client runs it directly:

```bash
claude mcp add portfolio \
  --env PORTFOLIO_DIR="/absolute/path/to/your/portfolio-files" \
  -- uv run --directory /absolute/path/to/gist-lab-ai/portfolio-mcp portfolio-mcp
```

(The exact variable name is in `portfolio-mcp/README.md`.) Then `/mcp` should list it
as connected, and asking Claude "what am I working on at the moment?" should draw on
`current-projects.md`.

Be clear about what that server's controls do. Serving the files **read-only**, from
a fixed **allowlist** of exactly those files, over local **stdio**, with **no network
listener**, protects the server itself: nothing can write to it, expose extra files,
or reach it from outside your machine. Those are access controls — not a guarantee of
confidentiality.

:::{warning}
The moment a tool pulls one of these resources into a conversation, its content is
sent to the model provider like any other prompt. So keep genuinely sensitive
personal detail out of your context files. Describe how you work, not who your
participants are or what your passwords and tokens are — the
{doc}`Data protection and privacy <data_protection>` rules apply here too.
:::

Used that way — professional context, no sensitive data — one context portfolio can
serve every tool you connect to it, so each starts from the same understanding of
who it is working with.
