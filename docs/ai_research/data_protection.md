# Data protection and privacy

```{image} /_static/comic-data_protection.svg
:alt: Comic illustrating the “Data protection and privacy” section.
:width: 100%
```

When you paste text into a cloud AI tool, it leaves your machine and is processed on
a company's servers. Treat that as handing the material to a third party, because
that is what it is. What you send matters.

:::{warning}
Never put personal, sensitive, or confidential data into a third-party AI tool
without a lawful basis and your project's approval. This includes personal and
mobility/location data, participant data, and anything you do not have the right to
share — including other people's unpublished work that you hold in confidence. For
manuscripts you are peer-reviewing, the venue's AI policy decides (below).
:::

Your **own** unpublished drafts and code are a different matter: bringing them to AI
is the point — that is how it works as your reviewer and writing coach. Check only
that nothing *inside* them is itself restricted — participant data, a partner's
confidential material — and do it on the lab's Team account, whose terms keep your
material out of training (see below), not on a personal account. The rule above is
about what is *not yours to share*.

## First, check which account you are using

Whether your prompts and files can be used to train future models depends on the
account you are signed into and its settings, not on the tool. Under Anthropic's
[commercial terms](https://code.claude.com/docs/en/data-usage) — the lab's **Claude
Team** organisation, Enterprise, and the API — prompts and code are **not** used for
training unless the organisation opts in. Under the consumer terms — a personal Free,
Pro, or Max account, *including when you use that account with Claude Code* — a
setting allows training. Turn it off.

Check this now, and again whenever you sign in, switch accounts, or reinstall:

- In Claude Code, run `/status` and confirm the account shown is the lab's Team
  organisation, not a personal account.
- If you also use a personal account, open claude.ai → *Settings → Privacy* and set
  **Help improve our AI models** to off ([how](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings)).

Retention differs too. As of August 2026: 30 days on commercial terms, and on a
personal account 30 days with the setting off but five years with it on — check the
data usage page above for the current figures.

## Why this is strict

**Personal data is regulated.** Under the GDPR, processing personal data needs a
lawful basis and usually a data-processing agreement with whoever does the
processing. A consumer AI account is not covered by your project's agreements, so
sending personal data to it can be an unlawful transfer, not just a bad idea.

**Confidential material is not yours to disclose.** A co-author's draft shared in
confidence, a partner's data under an NDA, and licensed datasets all carry
obligations to other people. A third-party tool is the wrong place for them.

**Peer review runs on the venue's rules, not yours.** A manuscript you are reviewing
is confidential, and whether AI may assist — and which tools — is the venue's call.
The positions genuinely differ: major publishers currently forbid uploading a
submitted manuscript, or any part of it, into an AI tool
([Elsevier](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals),
[Springer Nature](https://www.nature.com/nature-portfolio/editorial-policies/ai)),
while some venues build confidentiality-preserving AI assistance into the review
process itself —
[NeurIPS 2026](https://neurips.cc/Conferences/2026/ai-reviewing-experiment) runs an
opt-in experiment using zero-data-retention models, with fully automated reviewing
still banned. So check the policy of the venue you are reviewing for, each time;
without its explicit permission, the answer is no.

## What not to paste

**Don't**

- Personal or identifiable data — names, addresses, location and mobility traces,
  health or register data.
- Data you don't have the right to share — participants', partners', or licensed
  data.
- Other people's unpublished work that isn't yours to disclose. For manuscripts you
  are peer-reviewing, the venue's AI policy decides (above) — no permission, no AI.
- Secrets — API keys, passwords, tokens.

**Do**

- Bring your own drafts, manuscripts, and code to the lab's Team account — that is
  what it is for.
- Work on non-sensitive, aggregated, or synthetic samples when the problem involves
  data you cannot share.
- Use accounts and tools your institution has approved and covered for that class
  of data.
- Ask before assuming a tool is safe for a given kind of data — for personal data
  the default answer is no.

## Location and mobility data

Spatial data is easy to misjudge. Individual-level location and mobility traces are
personal data even when no name is attached: a single home-to-work trajectory can
re-identify a person. Treat trajectory, GPS, and fine-grained location data as
personal unless it has been properly aggregated or anonymized — and remember that
aggregation can still leak.

## Where to check

- Aalto's guidance on
  [handling personal data in research](https://www.aalto.fi/en/services/how-to-handle-personal-data-in-research)
  and its [data protection pages](https://www.aalto.fi/en/data-protection), and your
  project's data management plan.
- Aalto's data protection officer, <dpo@aalto.fi>, for anything involving personal
  data.
- The tool's own terms: whether it retains inputs, uses them for training, and
  where it processes them — for Claude, the
  [data usage page](https://code.claude.com/docs/en/data-usage) and the
  [commercial](https://www.anthropic.com/legal/commercial-terms) and
  [consumer](https://www.anthropic.com/legal/consumer-terms) terms.

The {doc}`hands-on exercises </ai_research/exercises/before_you_start>` later in this
theme run on your own project, so read this page first and keep sensitive data out of
them.
