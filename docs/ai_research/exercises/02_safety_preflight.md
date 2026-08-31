# 2. Safety preflight

Set the boundaries before the agent acts on your project
({doc}`Rules and safety </ai_research/rules_and_safety>`).

- Run `/status` and confirm you are signed into the lab's Claude Team organisation,
  not a personal account
  ({doc}`Data protection and privacy </ai_research/data_protection>`).
- Start from the lab's baseline permissions, and check whether you are changing
  project or global configuration.
- Get to a clean version-control state — commit or stash — or make a backup, so you
  can undo anything.
- Make sure no secrets sit in the working directory or will be pasted in.
- Know what is on allow, ask, and deny, and that edits are yours to review before they
  are kept.

**Done when:** you can say what the agent may do without asking, and you can undo its
changes — a clean Git state and a way back.
