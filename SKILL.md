---
name: gitbook-training-pages
description: Builds GitBook-ready markdown training pages (clear explanation, funny real-life analogies, Mermaid diagrams, step-by-step labs, official docs links) that a trainer can deliver live straight from the page, like a driver script. Use this skill whenever the user wants to create, convert, continue or fix a GitBook page, course topic, module, lab or training material, says "make the page for" a topic, pastes a topic list for a course, asks for a Playwright test page, or asks how to name or number pages for upload to GitBook, even if they never mention GitBook or markdown.
---

# GitBook training pages

## Why these pages look the way they do

The trainer delivers live from the page. They put it on the projector, follow it step by step, and candidates reread it later. So every page works as a delivery script and as study notes at the same time. That is why labs spell out every step, why humor and diagrams carry the explanation, and why the page tells the trainer what to say and what to watch for.

When a design choice is unclear, ask this: could a trainer who has never taught this topic run the whole session from this page alone? If not, the page is missing something.

## Workflow

### 1. Ask where the candidates are from

Before writing anything, ask which country the candidates belong to. The examples (money, food, transport, daily frustrations) come from that country, so the jokes land and the numbers feel real.

Ask once, in a single message. Add only what is still unknown from the conversation: candidate experience level, and operating system if the page has a lab. Use AskUserQuestion when it is available, otherwise ask in plain text. Skip the question if the user already named the country earlier in the conversation. If candidates come from several countries, ask whether to use one shared everyday setting or one example per region.

Read `references/analogies-and-country.md` after the answer comes back.

### 2. Parse and validate the topic

Treat the topic as a claim to check, not as something to recall from memory. Search the official documentation for the current version, install steps, commands and defaults. When a command can be run in the sandbox, run it and paste the real output into the page as the expected output. Keep the official docs URL you actually opened. Never guess a link.

If the user gave a topic list, validate each topic separately and keep the order they gave.

### 3. Pick the format

| Content | Format | Pages produced |
|---|---|---|
| Most topics | Standard page | 1 |
| Machine learning or applied data topics | Applied page | 1 |
| Playwright tests | What and Why, then Solution | 2 |

The exact skeleton for each is in `references/page-formats.md`. Read it before writing. If the user does not say which page number comes next, ask for it, because the number is part of the file name.

### 4. Write the page

Read these as you write, each one covers a different rule set:

- `references/page-formats.md` for the skeleton, file names and front matter
- `references/driver-style.md` for trainer notes, hint colors and pacing
- `references/labs.md` for step-by-step labs where nothing is left to assumption
- `references/diagrams-and-colors.md` for Mermaid diagrams and the five allowed colors
- `references/analogies-and-country.md` for funny analogies and country-based examples

A finished sample is in `assets/examples/1. Python Virtual Environments.md`. Match its depth, not its topic.

### 5. Run the humanizer

After the draft is complete, run the humanizer skill on the page in file mode. It changes prose only, so code blocks, Mermaid blocks, commands, paths, front matter and links stay untouched. Keep the jokes and analogies, which are deliberate voice, and remove the chatbot habits: staged openers, "not X but Y" contrasts, one-line closers, forced triads, em dashes, bold labels on every bullet. If the humanizer skill is not available, apply the same edits by hand.

### 6. Check and deliver

Run the checker on every page you produced:

```bash
python scripts/check_page.py "path/to/1. Page Title.md"
```

It verifies the file name, front matter, dashes, Mermaid colors, docs link, trainer notes and lab structure. Fix every error and read each warning. Then hand the `.md` files to the user. Hand over every page, and give one line of context for each.

## Final checklist

- Country asked, and examples come from it
- File name is `<number>. <Title Case Name>.md`
- Docs link was opened and is current
- Every command was verified, or the page says what could not be verified
- Every lab step has an action, an expected result and a fallback
- Diagrams use only green, blue, yellow, purple and red
- Humanizer pass done, and the checker passes
