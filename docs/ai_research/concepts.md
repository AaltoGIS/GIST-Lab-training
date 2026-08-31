# Concepts and terminology

In the materials we use a handful of terms repeatedly. Here is what they mean;
the pages that follow go into each.

**Model.** The AI itself — for example, Claude. Models differ in how capable, fast,
and expensive they are, and you choose which one to use for a given task. Reach for
a stronger model when the work is hard or the quality matters (see
{doc}`Getting started <getting_started>`).

**Agent.** AI that can act toward a goal over several steps — reading files, running
commands, using tools — rather than answering in a single reply. **Claude Code** is
a coding agent that works inside your project.

**Subagent.** An agent that another agent starts to handle part of a task, often
several at once, so a large job can be split up.

**Skill.** A packaged set of instructions for a particular kind of task that the
agent loads when it is relevant — for example, the lab's writing and review skills.
You can write your own (see {doc}`Skills <skills>`).

**MCP server.** A small program that gives an AI application like Claude Code access
to data or actions outside itself through the Model Context Protocol, a shared
standard for connecting AI applications to context and actions. An MCP server can expose **resources** (read-only content, such
as your reference library or a set of notes) or **tools** (actions the agent can
take). Henrikki runs one for Zotero and one that serves a personal context portfolio
(both in {doc}`Useful companion tools <companion_tools>`).

**Slash command.** A shortcut you type, such as `/review-plan-codex`, to run a
predefined command or skill.

**Permissions, sandbox, and Auto mode.** The controls that decide what an agent is
allowed to do: permission rules (allow / ask / deny), an OS-level sandbox that
limits what a command can touch, and an optional Auto mode that approves routine
actions for you. {doc}`Rules and safety <rules_and_safety>` covers these.
