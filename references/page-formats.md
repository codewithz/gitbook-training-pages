# Page formats

Contents: file naming, front matter, standard page, applied page, Playwright pair, numbering.

## File naming

GitBook uses the file name as the document name when the file is uploaded. So the file name is the title candidates see in the sidebar.

Pattern: `<number>. <Title Case Name>.md`

Examples:

- `1. Installation and Architecture.md`
- `7. Joins and Window Functions.md`
- `12. Login Flow What and Why.md`

Rules:

- Capitalize each main word. Keep small words lowercase: a, an, and, as, at, but, by, for, in, of, on, or, the, to, vs, with. The first word is always capitalized.
- Number, then a period, then one space, then the title.
- Spaces stay as spaces. No underscores, no hyphens used as separators.
- Keep names under about 50 characters so the sidebar does not truncate them.

## Front matter

Every page starts with a description. GitBook shows it under the title and uses it in search.

```markdown
---
description: One sentence saying what the candidate can do after this page.
---
```

Do not add a top-level `# Title` heading. GitBook already shows the file name as the title, so a second H1 repeats it. Start the body with the trainer notes block.

## Standard page

Use this order. Headings are sentence case.

1. Trainer notes hint (see `driver-style.md`)
2. `## What you will learn` with 3 or 4 plain bullets
3. `## Explanation` with a clear, plain-language walkthrough. Put the Mermaid diagram here, right after the paragraph it illustrates.
4. `## Math` only when the topic has a formula. Show the formula, define each symbol, then work one example with real numbers.
5. `## Real-life example` with the funny analogy and the mapping table (see `analogies-and-country.md`)
6. `## Official docs` with the link and one line on what is in it
7. `## Code` with a realistic dataset, then each code block followed by a short explanation of what it does and why
8. `## Lab` when the topic is hands-on (see `labs.md`)
9. `## Check your understanding` with 3 questions and answers hidden in `<details>` blocks

Skip a section when the topic has nothing for it, instead of writing filler. A page about installation might have no Math section, and that is fine.

The dataset in the Code section must look like real work: bank transactions, loan schedules, order logs, ticket records. Match it to the candidates' industry and country. Random numbers teach nothing because candidates cannot sanity check the result.

## Applied page (machine learning and applied data topics)

Order: clear explanation, real-life example, basic code, ML implementation, reference link, diagrams where they help.

1. Trainer notes hint
2. `## What you will learn`
3. `## Explanation` with a diagram of the data flow
4. `## Real-life example`
5. `## Basic code` using only the standard library or one common package, so candidates see the idea with nothing hidden
6. `## ML implementation` with a notebook-style flow: load the data, explore it, prepare it, train, evaluate, interpret. Use a real public dataset or a realistic hand-made one, and say where it came from.
7. `## Official docs`
8. `## Lab`
9. `## Check your understanding`

Candidates learn best by running notebooks on real data, so keep the implementation runnable top to bottom in a fresh environment, and list the install command.

## Playwright pages: always two

A Playwright test gets two pages. One page does not work because candidates see the finished code without understanding why it looks that way.

### Page A: What and Why

File name: `<n>. <Test Name> What and Why.md`

Contents:

- Trainer notes
- The user journey being tested, in plain words, with a Mermaid flowchart
- Why this test matters: what breaks in production if it is missing
- What exactly will be asserted, and what will not
- How the selectors will be chosen and why (roles and labels before CSS, with reasons)
- Risks: flaky points, waits, test data, environment
- A build-up in small stages, with only short snippets, so candidates predict the next step before seeing it
- Official docs link

### Page B: Solution

File name: `<n+1>. <Test Name> Solution.md`

Contents:

- Trainer notes
- Prerequisites and project setup, step by step (follow `labs.md`)
- The full test file in one code block with a title
- A line-by-line or block-by-block explanation after the code
- How to run it, with the exact command and the expected output
- What failure looks like, and how to read the report
- Official docs link

Both pages share the same numbering sequence, one after the other.

## Numbering

Pages continue the course sequence. If the user has not said which number comes next, ask. For a Playwright pair, ask once and use `n` and `n+1`.
