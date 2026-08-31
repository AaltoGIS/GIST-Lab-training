# Higher-quality results

Using AI well means checking its output ({doc}`Using AI well <using_ai_well>`). This
page is about how — the concrete methods that turn "it looks right" into "I have
reason to trust it." Two things do the work: real validation, and review. The order
matters: validation is how you get evidence the result is right; review, including a
second AI model, only helps you find problems.

```{image} /_static/comic-higher_quality_results.svg
:alt: Comic illustrating the “Higher-quality results” section.
:width: 100%
```

## Validate against something independent

A model's output is only as trustworthy as the check you put it through, and a useful
check is independent of the model. Depending on the work, that means some of:

- **Primary sources** — does the cited paper actually say what it is cited for? Open
  it and see.
- **Executable tests** — does the code pass tests you wrote, including the awkward
  cases? (The {doc}`testing lessons </testing_packaging/testing>` cover how.)
- **Domain sanity checks** — does the number have the right sign and order of
  magnitude? Do the parts add up to the total? Does the result match a case you
  already know?
- **The data and the plots** — look at them, not only the summary statistic.
- **A reproducible rerun** — does the analysis give the same result when you run it
  cleanly?
- **Human expert review** — you, or a colleague who knows the domain, reading the
  result critically.

:::{important}
A second AI model is not independent evidence. It can repeat the same mistakes,
having learned from the same kind of data. Use AI review to *find* problems; use
checks like the ones above to *confirm* the result is right.
:::

## Reviewer agents and cross-model review

With that boundary clear, review is genuinely useful. A reviewer agent — a second
model reading your code, plan, or draft — gives a fresh read that catches bugs,
unclear reasoning, and cases you missed. A pairing that works well — the one
Henrikki uses daily — is Claude with **Codex**: Claude drafts a plan or a change,
Codex reviews it against the plan, and the two iterate until no serious findings
remain. The `review-plan-codex` and `review-code-codex` skills run exactly this
loop.

Using two different models rather than the same one twice is deliberate: they fail in
different places, so one often catches what the other wrote. But the result is a list
of candidates for you to judge, not a certificate that the work is correct.

### Setting it up

Codex is OpenAI's coding agent, and using it is optional. The loop needs the
[Codex CLI](https://learn.chatgpt.com/docs/codex/cli) installed — on macOS or Linux,

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

— and a sign-in the first time you run `codex`, usually with a ChatGPT account. As of
August 2026, Henrikki's setup pairs Claude with a high-reasoning Codex model
(`gpt-5.6-sol` at `xhigh` effort, set in `~/.codex/config.toml`); the models change,
so check what the current install offers.
With the lab's skills installed ({doc}`Skills <skills>`), the two commands are:

- `/review-plan-codex <absolute path to plans/your-plan.md>` — Codex reviews the plan,
  Claude edits it to address the serious findings, and they repeat until Codex reports
  none.
- `/review-code-codex <absolute path to plans/your-plan.md>` — the same loop on your
  uncommitted changes, reviewed against that plan.

Both only work on a plan inside the project's `plans/` directory, and both stop after
ten rounds or when a round changes nothing.

**Without Codex**, you can still get a fresh read: open a second Claude Code session,
which starts without the first session's conversation, and ask it to review the plan
or the diff against the plan. You lose the second model's different blind spots but
keep the fresh read — and the same rule applies: its findings are candidates for you
to judge.

## When to escalate

Most tasks do not need heavy machinery. When a problem is hard, or a mistake would be
expensive, spend more: move to the strongest model available, and add a cross-review.
The extra time and cost are worth it exactly when the result matters.

## Avoiding AI-isms

For writing, a review pass aimed specifically at AI-isms — the flowery, hollow, or
generic phrasing that unedited AI output carries — is worth running. A second model,
asked to flag AI-sounding text, catches what you have stopped noticing in your own
draft. These very pages were written that way. As always, you make the final call: a
reviewer will happily flatten good prose along with the bad, so keep what you can
defend and cut the rest.
