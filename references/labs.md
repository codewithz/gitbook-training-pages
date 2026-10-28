# Labs: step by step, nothing left to assumption

Contents: why labs are written this way, lab anatomy, step anatomy, rules, a short example.

## Why

A lab fails when one step assumes something the candidate does not have: a folder, a version, a permission, an open terminal. In a live room that costs ten minutes per stuck candidate, and the trainer cannot help everyone at once. So a lab states every prerequisite, every action and every expected result. A candidate who follows it literally must succeed, or must know exactly why they did not.

## Lab anatomy

Every lab has these parts, in this order:

1. `### Goal` in one sentence, naming the thing candidates will have at the end
2. `### Time` as an honest estimate
3. `### Prerequisites` as a checklist. Each item has a command to check it and the expected output.
4. `### Environment` with the operating system, tool versions and the folder they will work in
5. `### Steps` as numbered steps (see below)
6. `### Verify` with a final check that proves the lab worked
7. `### Cleanup` with exact commands to remove what the lab created
8. `### Troubleshooting` as a table of symptom, cause and fix
9. `### Stretch` with one optional extension for fast finishers

## Step anatomy

Each step is a small block:

- A heading with the step number and a verb: `#### Step 4: Create the virtual environment`
- **Why** in one sentence, so candidates understand the action instead of copying it
- **Where**: which terminal, which folder, which file. Say how to open the terminal if it is the first step.
- **Action**: the exact command or the exact file content, in a code block
- **Expected result**: the output, or what they should see on screen
- **If it differs**: the most likely cause and the fix, or a pointer to the troubleshooting table

One action per step. If a step needs two commands, make it two steps.

## Rules

- Never write "obviously", "simply", "just" or "as usual". They hide assumptions.
- Use full commands, never fragments. Show the path every time the folder matters.
- When a file is created or edited, show the entire file after the change, not a diff.
- Pin versions that matter, and say which versions the expected output came from. Tell candidates that version numbers in the output may differ, and name which parts must match.
- When the operating system is unknown, give Windows, macOS and Linux variants side by side. Mark each variant clearly.
- Run the lab yourself in the sandbox when possible and paste the real output. If something cannot be run, say so in a yellow hint instead of inventing output.
- Include the failure on purpose when it teaches something. Mark it with a red hint so candidates know it is expected.
- Name the data. A lab dataset has a source, a column list and a reason it looks the way it does.
- End with cleanup. Labs that leave services running or files behind cause trouble in the next session.

## Example step

```markdown
#### Step 3: Create the virtual environment

**Why:** The environment keeps this project's packages separate from every other project on the machine.

**Where:** The terminal you opened in Step 1, inside the `spend-report` folder.

**Action:**

```bash
python -m venv .venv
```

**Expected result:** The command prints nothing and returns to the prompt. A new folder named `.venv` now exists. Check it:

```bash
ls -a
```

You should see `.venv` in the list.

**If it differs:** If you see `command not found: python` on macOS or Linux, use `python3` in place of `python` for every step.
```
