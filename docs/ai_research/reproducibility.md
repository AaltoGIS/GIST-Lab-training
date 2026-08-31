# Reproducibility and record-keeping

```{image} /_static/comic-reproducibility.svg
:alt: Comic illustrating the “Reproducibility and record-keeping” section.
:width: 100%
```

Research should be reproducible: someone following your record can see how you
reached a result and reach it themselves. AI complicates this. Model outputs vary
from run to run, and hosted models change and are retired, so you often cannot
rerun a prompt later and get the same answer. That does not let you off the hook —
it changes what you aim for.

## Auditability, not exact reproduction

Separate two things people tend to run together:

- **Exact reproduction** means running the step again and getting the same output.
  For many AI steps this is not possible: the model is stochastic, and the version
  you used may not exist next year.
- **Auditability** means a reader can see what you did and judge it — the inputs,
  the output you used, your edits, and the decisions in between. This you can always
  preserve, and it is what matters.

Aim for auditability, and be honest about which steps cannot be rerun identically.

## What to keep

- The prompt or instruction that shaped the result, or a clear description of it.
- The tool, the model or version, the settings, and the date you used them.
- The AI output you kept, and your changes to it — a diff, if it is code or text
  under version control.
- The code and data themselves, under version control, as for any analysis.
- A note of which steps were AI-assisted — the same record you disclose (see
  {doc}`Integrity, disclosure, and provenance <integrity_and_disclosure>`).

In practice that is a few lines beside the result. In Claude Code, `claude --version`
prints the client version and `/status` shows the model and the account you are signed
into. The lab's `github-api` skill ({doc}`Skills <skills>`) writes the same record into
every pull request as its last line, read live at the moment the PR is opened:

```text
AI assistants: Claude Opus 4.8 (claude-opus-4-8, xhigh reasoning) via Claude Code 2.1.153;
OpenAI gpt-5.5 (high reasoning) via Codex CLI 0.125.0.
```

For a manuscript, keep the same facts in your project notes and carry them into the
methods (below). The prompt itself is worth keeping when it shaped the result — a plan
file under `plans/`, or the task description you gave the agent — and not worth keeping
for a routine "fix this error".

:::{note}
A prompt log gives you auditability, not exact reproducibility. Do not describe an
AI-assisted step as reproducible if a reader could not rerun it and get the same
output. Say what was done and how you checked it instead.
:::

## In the methods

Describe the AI's role the way you describe any method: which tool and version,
what it did, and how you verified the output. A reader should come away
understanding what the model contributed and how you checked it, even when they
cannot regenerate the exact text or code. For a limited role, one sentence is enough:

> The analysis scripts were drafted with Claude Code (Claude Opus 4.8, June 2026) and
> revised by the authors; all reported results were regenerated from the committed
> scripts, and the accessibility measures were checked against a hand-computed subset.

## Keep it ordinary

None of this needs new machinery. Put your code and your edits under version
control, keep the AI output you used as an artifact, and record the tool, version,
and date beside it. It is the same habit that makes any analysis traceable — AI
just makes the "write down what you did" part matter more.
