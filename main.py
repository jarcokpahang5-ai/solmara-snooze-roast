"""Snooze Button Roast — one-line roast of an alarm clock ringing at 6 AM on a Saturday.

The joke: the alarm clock is personified as a smug, self-important man who
is absolutely certain it is time to get up — while being wrong about the most
basic fact of all, that it is Saturday. The punchline lands in the last few
words: all that confidence, and he has never once been right about what day
it is. The roast is aimed at the clock itself (its arrogance), not at
mornings in general, and it never asks who invented the thing.
"""

ENTRY = (
    "My alarm clock rings at 6 AM on a Saturday with the confidence "
    "of a man who has never once been right about what day it is."
)

for _path in ("/output/entry.txt", "output/entry.txt"):
    try:
        with open(_path, "w", encoding="utf-8") as _f:
            _f.write(ENTRY)
    except OSError:
        pass

print(ENTRY, end="")
