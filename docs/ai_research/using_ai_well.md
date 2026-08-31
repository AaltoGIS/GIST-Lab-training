# Using AI well

You already use AI tools in your research. This training is about using them *well* —
so that they raise the quality of your work, not just the speed of it. The test is
whether the result is better, not whether it came faster.

## A capable, unreliable collaborator

Modern AI assistants are good at one thing above all: producing fluent, plausible
text and code, quickly. That is genuinely useful. It is also the trap, because
*wrong* output reads exactly as convincingly as *correct* output. An assistant
will hand you a function that looks right but mishandles a coordinate reference
system, a reference that does not exist, or a summary that quietly drops the
caveat that mattered — all in the same confident voice it uses when it is right.

So treat these tools as what they are: a fast, well-read collaborator whose drafts
always need checking — not an oracle. The moment you trust the output *because* it
sounds sure, you have misread the tool.

## You own the output

Start from one rule:

:::{important}
Whatever you submit, commit, or publish is yours. You are accountable for every
line of code, every sentence, and every number in a table — whether you wrote it or
an assistant did.
:::

Your co-authors, reviewers, and readers hold *you* accountable, never the tool.
So **do not ship what you cannot explain.** If
you can't say why a piece of generated code is correct, or you haven't checked a
claim it made, it isn't ready — however polished it looks.

## Verification is the real skill

If the assistant can produce a draft in seconds, the value you add is no longer
the drafting. It is the **judgment**: deciding what "correct" means here, and
checking that you got it.

A good habit is to decide the check *before* you accept the output. Ask "how will
I know this is right?" and answer it concretely:

- Read the code and run it against a test — not just the happy path.
- Trace a factual claim back to a primary source you actually open.
- Sanity-check a number against something you already know to be true.
- Compare an AI summary against the real paper before you rely on it.

The concrete methods — validation, tests, cross-review — come later in this theme;
for code specifically, the {doc}`testing lessons </testing_packaging/testing>` show
how to check that it behaves as you expect.

## The failure mode: over-reliance

**Over-reliance** is trusting the output because it is *usually* right, or because
checking feels like a chore. It creeps in exactly where you are least able to
catch the error: outside your own expertise, in an unfamiliar library, or in a
language you read less fluently than you write it.

:::{warning}
If someone asked "how do you know this is right?" and your honest answer is "the
AI said so," you have over-relied. That is the moment to stop and check.
:::

Keep the assistant on work where you *can* judge the result. Use it to move faster
through things you understand — not to paper over things you don't.

## Spotting "AI-isms"

**AI-isms** are the tells of unedited AI output:

- In prose: generic openers, empty enthusiasm ("powerful", "seamless",
  "game-changing"), hedging that says nothing ("it is important to note that…"),
  and padded lists of three where one word would do.
- In code: comments that restate the obvious, defensive scaffolding you never
  asked for, and calls to plausible-sounding functions that don't exist.
- In research specifically: confident but fabricated or mis-attributed citations,
  and smooth summaries that flatten the uncertainty a careful reader needs to see.

They matter for two reasons. They waste your readers' attention — and editors and
reviewers increasingly recognize them on sight. More importantly, they *hide
errors behind fluency*: the same smoothness that makes a fabricated citation read
well is what stops you noticing it is fabricated.

**Do**

- Cut generic phrasing until every sentence carries specific, checkable content.
- Keep the parts you can defend; rewrite the rest in your own voice.
- Open every citation before it stays in your draft.

**Don't**

- Paste AI prose into a manuscript unedited and hope no one notices.
- Keep a comment that only re-describes the line above it.
- Let a confident sentence stand in for a fact you haven't verified.

## In one line

Use AI to do better work, and stay the person who checks it. The concrete quality
methods come later in *Higher-quality results*; the responsibility side — integrity
and disclosure, data protection, reproducibility — runs through the rest of Part A.
