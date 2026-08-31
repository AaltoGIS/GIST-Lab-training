# Efficient prompting strategies

What you get from an agent depends on how you ask. This page covers prompting at
two scales: a piece of work large enough to need a plan first, and a single small
request inside a session — and then the workflow that turns a plan into finished,
reviewed work.

## Start from the outcome — and let Claude interview you

For anything beyond a small task, the highest-leverage prompt is not a
specification. It is a clear description of two things — **the output you want to
exist** and **the objective it serves** — followed by an instruction that inverts
the usual burden:

```text
Here is what I want and why: <the outcome, and the objective behind it>.
Interview me about anything you need to know before starting, then write a plan
for my review. Don't build anything yet.
```

A capable model is better at knowing what it needs to ask than you are at guessing
it: it comes back with the constraints you forgot you had, the edge cases you had
not considered, and the decisions that are genuinely yours to make. Answer what it
asks — and add what it missed, because the domain knowledge is still yours. Your
answers become a plan you review before anything is built. Claude Code's **plan
mode** (`Shift+Tab`) supports exactly this — the agent explores and asks but does
not edit your project until you approve the plan.

## Scoping a small task

When the task is small and you already know exactly what you want, skip the
interview and state it yourself. Give the agent:

- **the goal** — the outcome you want, in a sentence or two;
- **the inputs that matter** — the specific files or context the task depends on,
  not everything at once;
- **constraints** — conventions to follow, approaches or libraries to use or avoid;
- **the expected output** — what a finished result looks like;
- **acceptance checks** — how you will know it is right: a test that should pass, a
  property that should hold.

Written out, a request in this shape looks like this — five short lines rather than
a paragraph:

```text
Goal: scripts/aggregate_trips.py should also write hexagon-level trip counts, next to
the current grid-level output.
Inputs: scripts/aggregate_trips.py, the H3 helper in src/spatial/hex.py, the sample in
tests/data/trips_sample.parquet.
Constraints: reuse the existing hex helper rather than adding a new one; keep the
grid output unchanged; no new dependencies.
Expected output: a --hex-resolution option, the extra output file, and a test.
Acceptance: pytest tests/test_aggregate.py passes, and the hexagon counts sum to the
same total as the grid counts for the sample.
```

Notice that these five are also what the interview above converges to — the
difference is only who produces them: for a small task you state them in one go; for
a bigger one, the model draws them out of you.

Break a large task into smaller ones the agent can finish and you can check. And
when an interaction drifts — the agent has gone down a wrong path and each reply
digs deeper — stop and start a fresh, well-scoped request rather than fighting the
tangled one. A clean restart is usually faster than untangling.

## The project workflow

For work bigger than a single task, work in a loop — the one Henrikki uses for
everything from research code to these very materials:

1. **Plan first.** Write the plan down — a Markdown file under `plans/` in the
   project, kept gitignored so plans are working documents rather than part of the
   repository — before you implement. Get it the interview way:
   describe the outcome and the objective, have the agent interview you, and let it
   draft the plan from your answers. Then review it yourself, and often with a
   second model
   ({doc}`Higher-quality results <higher_quality_results>`). A wrong assumption
   caught in the plan is cheap; caught after implementation, it is not. A plan needs
   five parts:

   ```markdown
   # Plan: <one line saying what changes>

   ## Goal — the outcome, and how you will know it is reached
   ## Context — what exists today, and what constrains the change
   ## Steps — numbered, each small enough to review as one diff
   ## Verification — the tests and checks that show each step worked
   ## Out of scope — what this plan deliberately leaves alone
   ```

2. **Implement in small steps.** Build against the plan, one piece at a time.
3. **Cross-review the change.** Read the diff yourself, and have a reviewer agent or
   a second model check it before it lands.
4. **Ship small pull requests.** One feature or fix per PR, and at most about 300
   lines of code diff (data files excluded) — small enough that a person can actually
   review it. Larger work becomes a series of small PRs, listed in the plan up front
   and opened one at a time, not one big one.
5. **Reuse what already exists.** Before adding a new function, look for one that
   already does the job and extend it. An agent will happily write a third copy of
   something you already have; that is yours to catch.

## Why this shape

Every step keeps a person in control where judgment matters — the plan, the review,
the diff — while the agent moves fast inside each step. You decide between the steps;
it does the legwork within them. This is the method the
{doc}`hands-on exercises </ai_research/exercises/before_you_start>` walk you through.

## Working toward a goal: `/goal`

For work with a clear, checkable end state, the
[`/goal` command](https://code.claude.com/docs/en/goal) lets Claude continue on its
own. You give a completion condition; after each turn, a small fast model checks
whether it holds, and Claude keeps going until the condition is met, judged
impossible, or you run `/goal clear`.

```text
/goal all tests in tests/ pass and ruff reports no issues — or stop after 15 turns
```

A good condition has the same parts as an acceptance check: one measurable end
state, the command that proves it — the evaluator only sees what appears in the
conversation, so the proof has to be run there — any constraints that must hold, and
a limit such as *"or stop after 15 turns"*. `/goal` with no argument shows the
condition, the turn count, and the tokens spent so far.

:::{warning}
Try `/goal` only once the rest of this page is routine for you. It runs many turns
with no human review in between: a vague condition can spend a lot of tokens on work
you end up discarding, and writing conditions that finish is a skill in itself. Keep
a turn limit in the condition, and use it on work where the check is a command. A
met goal does not mean the result is right — you still check it
({doc}`Using AI well <using_ai_well>`).
:::
