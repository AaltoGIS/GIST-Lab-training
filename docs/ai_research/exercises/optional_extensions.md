# Optional extensions

These go past the basics. Do them when they are useful, not to tick a box.

## Configure an MCP server

Connect an MCP server — your Zotero library is the easiest start; the commands are in
{doc}`Useful companion tools </ai_research/companion_tools>`. Serving your own context
portfolio is the advanced version
({doc}`Teaching Claude who you are </ai_research/teaching_claude>`).

- **Before:** have the server installed and know what it exposes — for Zotero, keep
  the desktop app open with its local API enabled.
- **Check:** `/mcp` shows the server as connected; confirm it is read-only and exposes
  only what you intend.
- **Done when:** Claude answers a question from your library — "which papers in my
  library use H3 hexagons?" — and cites the items.
- **Teardown:** `claude mcp remove <name>` once you have tested it, if you do not want
  to keep it.

## Use a custom slash command

Run a slash command — for example `/review-plan-codex` on a plan
({doc}`Higher-quality results </ai_research/higher_quality_results>`).

- **Done when:** the command runs and returns a result.
- **Teardown:** remove any temporary files it created.
