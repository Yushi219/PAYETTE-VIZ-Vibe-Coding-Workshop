# PAYETTE VIZ — Vibe Coding Workshop

An animated, scroll-paged slide deck for the Payette Design Viz team's internal
Vibe Coding session. September 2026 · 2 hours.

**Live:** https://yushi219.github.io/PAYETTE-VIZ-Vibe-Coding-Workshop/

## The sheets

| # | Sheet | What it covers |
|---|-------|----------------|
| 00 | Cover | — |
| 01 | Which Claude | Claude vs. Cowork vs. Claude Code — what each one hands back |
| 02 | Which model | Cost vs. depth, and how to read the usage meters |
| 03 | Idea to link | The seven steps from a thought to a published page |
| 04 | GitHub & Azure | Where a project lives, and the two rules that matter |
| 05 | Working with it | Briefs, plans, CLAUDE.md, Skills, remote control |
| 06 | Your board | A live idea board the room fills in together |
| 07 | Go build one | Three rules to leave with |

## Running it

Open `index.html` in any browser. Nothing to install, nothing to build —
it is a single self-contained file.

- **Scroll** or use the arrow keys / space to page between sheets.
- `F11` for fullscreen when presenting.
- `#3` on the end of the URL jumps straight to a sheet.

## The idea board (sheet 06)

Built for the room to use live:

- **Drag** any idea to reposition it. Its colour follows where it lands —
  red where it is easy and valuable, blue where it is worth the investment,
  green where it is cheap and minor, violet where it can wait. Anything
  between two corners blends the two.
- **Click** an idea to reveal its ✕ and remove it.
- **Type** a new idea into the box on the right; it drops into the middle
  for you to place.
- The board saves to the browser, so it survives a refresh.
  **Reset the board** puts the starting twelve back.

## Editing

The deck is one file: `index.html`. Open the folder with Claude Code and
describe the change you want.

To republish after an edit:

```bash
git add -A && git commit -m "Update the deck" && git push
```

GitHub Pages picks it up within a minute or so.
