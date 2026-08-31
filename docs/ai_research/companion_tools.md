# Useful companion tools

```{image} /_static/comic-companion_tools.svg
:alt: Comic illustrating the “Useful companion tools” section.
:width: 100%
```

Claude Code is not the only AI tool worth knowing. A few others fit specific parts of
research work. All of them change quickly, so treat the details below as a starting
point; each tool's own page, linked below, has the current version.

## Claude for Word

[Claude for Word](https://claude.com/claude-for-word) puts Claude inside Microsoft
Word, so you can draft, polish, and get
comments on a manuscript in the document itself. The lab's writing and reviewing
skills work here, attaching feedback as native Word comments rather than a separate
chat. It suits manuscript work that lives in Word.

## Elsevier LeapSpace

[LeapSpace](https://www.elsevier.com/products/leapspace) is a research-focused AI
workspace for tasks across a project — generating
ideas, planning, exploring the literature, and finding collaborators or funding. Its
Writing Coach drafts in dialogue with you, grounded in Scopus-indexed literature,
with citations you can trace and every suggested change left for you to approve. It
is worth a look when you want AI help anchored to the published literature rather than
to a general model.

## Beaver (in Zotero)

[Beaver](https://www.beaverapp.ai/) is an AI research assistant that runs inside
Zotero. It reasons over your own
library and the paper you are reading, answers questions with sentence-level citations
back to the source, and can annotate PDFs and organize your library without leaving
the reference manager. You connect it with a subscription or your own API key.

## Gemini Notebook

[Gemini Notebook](https://notebook.google/) (formerly NotebookLM) builds a workspace
around documents you upload —
papers, your notes, your own drafts. It answers questions only from those sources and
links each claim back to the passage it came from, and it can turn the same material
into study materials: a summary, a briefing, a set of key questions, a podcast-style
audio overview, or a mind map. It fits getting on top of a reading pile, or your own
notes, when you want answers anchored to sources you chose.

## Claude Design

[Claude Design](https://claude.com/product/design) turns a description into an
editable visual design on a canvas you can
refine — mockups, figures, posters, or slides. It is useful when you need a figure or
a presentation to look right and would rather adjust it by hand than in code.

## MCP servers

MCP servers connect an AI application to context and actions outside it (see
{doc}`Concepts and terminology <concepts>`). Two from Henrikki's own setup, worth
adopting:

- **Zotero.** [zotero-mcp-server](https://github.com/54yyyu/zotero-mcp) lets Claude
  search your Zotero library and read metadata, notes, and full text, so its answers
  can point at items you can open and check. Install it and let it write the
  configuration for you:

  ```bash
  uv tool install zotero-mcp-server   # or: pip install zotero-mcp-server
  zotero-mcp setup
  ```

  It talks to the Zotero desktop app, so keep Zotero open and enable *Settings →
  Advanced → Allow other applications on this computer to communicate with Zotero*.
  If `setup` did not register it with Claude Code, do it by hand:

  ```bash
  claude mcp add zotero --env ZOTERO_LOCAL=true -- zotero-mcp
  ```

- **Context portfolio.** A small read-only server that serves your own context files
  ({doc}`Teaching Claude who you are <teaching_claude>`).

Run `/mcp` inside a session, or `claude mcp list` in the terminal, to see which servers
are connected. Adding another local server follows the same `claude mcp add <name>
-- <command>` pattern, described in the
[MCP docs](https://code.claude.com/docs/en/mcp); a server added with
`--scope project` goes into the repository's `.mcp.json`, which you commit so
collaborators get it too.

:::{note}
These tools differ in cost and in how they handle what you give them, and they change
fast. Before putting any research data into one, check the
{doc}`Data protection and privacy <data_protection>` rules and the tool's own terms.
:::
