# What you can use AI and agents for

AI is a tool — a machine that is very good at processing language. Most research
work is language: code, prose, data, references. That is why these tools help
across so much of what you do. They are not a superintelligence, and won't be for
a long time, so treat them as a capable text tool rather than a mind — you bring
the question and the judgment; they extend how much you can attempt.

This training maps where they can help you with your research. You already use some of these; the aim is to see
the full range — and, further down, what changes once a tool becomes an *agent*
that can act on its own.

## Across your research

**Coding and software.** Write and test a function, work with a library or API you
don't know well, refactor code you've inherited — or, with a coding agent, develop
and maintain a whole software library. You set what the software is for and do the
final quality control; the model can do most of the writing, testing, and revising in
between. Often the most useful case is **debugging**: paste an error or a stack trace
and the model can explain what went wrong and fix it.

**Working with data.** Wrangle and clean messy files, convert between formats,
write the regex you never remember, and **extract** structured information from
unstructured text or PDFs — pulling values out of a table, or screening records
for a review.

**Writing.** Draft and tighten prose — abstracts, method sections, ``README``
files, docstrings, emails, cover and response letters — and **translate or polish**
English when it is not your first language.

**Feedback.** Have a draft critiqued before anyone else sees it: the argument, the
evidence, the structure, the places a reviewer would push back. The lab's reviewing
skills do exactly this, in a supervisor's voice ({doc}`Skills <skills>`); the habits
for using such feedback well are in
{doc}`Higher-quality results <higher_quality_results>`.

**Finding literature.** Find papers you would have missed: a new class of AI search tools
takes a research question rather than a keyword string and explains what each result
contributes — [Google Scholar Labs](https://scholar.google.com/scholar_labs/search)
(experimental), [Asta](https://asta.allen.ai/) from Ai2,
[alphaXiv](https://www.alphaxiv.org/), and
[LeapSpace](https://www.elsevier.com/products/leapspace)
({doc}`see Useful companion tools <companion_tools>`). 

**Reading and learning.** Then work with what you found — and not only by reading,
because you can now **discuss with your papers**: ask a PDF, or your whole reference
library, a question and get an answer grounded in the text.
Summarize a dense paper, triage a stack of PDFs, or get a plain explanation of an
unfamiliar method before you commit time to it.

**Analysis.** Talk through an analysis plan, sketch a figure, interpret an
unexpected result, or check your reasoning against a different approach.

## Thinking and understanding

Two uses cut across all of the above and are easy to overlook.

**Brainstorming.** Use AI as a thinking partner: frame a research question, weigh
study-design options, name a variable or a package, or argue both sides of a
decision. It generates options quickly and cheaply, which suits the messy early
stage where you are still working out what you want.

**Learning and explanation.** Ask it to explain a method, a library, a statistical
concept, a dense paragraph, or an error message, at the level you need. Used this
way, AI deepens your own expertise instead of standing in for it.

:::{note}
The {doc}`Using AI well <using_ai_well>` rule still holds for every use here: you
own and check the result. Brainstorms and explanations can be confidently wrong
too.
:::

## Agents

An **agent** is AI that can take actions toward a goal rather than answer in one
shot: it can read files, run commands, search, and work through several steps
before it comes back. That changes what you can hand off.

**Coding agents** (such as Claude Code) work inside your project — read the repo,
edit across files, run the tests, and iterate — so you describe an outcome and
review a working change instead of typing every line.

**Reviewer agents** read your work and critique it: a second model checking your
code or a draft against a plan. They *find* issues for you to judge; they do not
replace your own checking (see *Higher-quality results*).

**Research agents** search online, gather sources, and organize what they find —
for example a tool inside your reference manager that answers a question from your
library and the wider literature and cites each claim back to its source.

**Subagents and workflows** hand parts of a task to several agents working in
parallel, which helps when a job splits into independent pieces.

Most of this theme is about the coding agent and the reviewer agents, since those
are the ones the rest of the material puts to work.
