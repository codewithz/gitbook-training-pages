# Driver style

The trainer runs the session from the page. Write so that someone standing at a projector, mid-sentence, can look down and know what to do next.

## Trainer notes block

Open every page with one blue hint. It holds timing, the opening question and the main thing to get across.

```markdown
{% hint style="info" %}
**Trainer notes**

Time: 45 minutes (10 talk, 5 diagram, 30 lab).
Open with: "Who has installed something and then broken something else?" Wait for hands.
Land this: each project needs its own isolated set of packages.
{% endhint %}
```

## Hint colors

GitBook hints come in four styles. Keep each one tied to a single job, so the trainer learns to read the page by color.

| Style | Color | Job |
|---|---|---|
| `info` | Blue | Trainer notes, tips, background |
| `success` | Green | Checkpoint: what candidates should see on screen now |
| `warning` | Yellow | Common trap, or a spot where the room usually gets stuck |
| `danger` | Red | An error or action that breaks things or loses data |

Purple is used in Mermaid diagrams for data and external systems. GitBook hints have no purple style, so do not try to fake one.

## Pacing the page

- Put an approximate time in the trainer notes, and split it across talk, diagram and lab.
- Put a green checkpoint hint after every lab stage that produces something visible, so the trainer can scan the room and confirm.
- Put a yellow hint before the step where candidates usually fail. Say what the failure looks like.
- Write one "ask the room" question in the explanation, with the expected answer in the next sentence, so the trainer is never left without a follow-up.

## Reading on a projector

- Keep paragraphs to 3 or 4 sentences.
- Keep code blocks under about 25 lines. Split longer files into stages and show the full file at the end.
- Show the command and its output in separate blocks, so candidates can copy the command without the output.
- Keep diagrams small enough to read from the back row: 12 nodes at most.
- Use tables for comparisons and mappings, because they scan quickly.

## Voice

Write the way a good trainer talks: plain words, short sentences, one idea at a time. Say "you" to the candidate. A joke should explain something, so the analogy stays attached to the concept. Do not announce the point ("Let's dive in"). State it.
