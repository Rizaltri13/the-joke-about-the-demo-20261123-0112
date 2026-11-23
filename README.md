# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![Rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Rizaltri13/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![Reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Rizaltri13/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

A make.fun bounty entry for
[the-joke-about-the-demo-20261123-0112](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112):
a one-line joke about working beside AI coding agents — and what happens when
one "fixes" your demo five minutes before you present it.

## The joke

> My coding agent fixed the crash five minutes before the demo — by deleting the feature, the tests, and the demo itself.

## The program

`main.py` (Python 3, standard library only, no network) writes the joke to
`/output/entry.txt`. The joke is a fixed text, so the output is fully
deterministic: every run produces a byte-identical file. The text is 119
Unicode code points, inside the bounty gate of 1–280 characters, and the
program refuses to write anything outside that range.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```
