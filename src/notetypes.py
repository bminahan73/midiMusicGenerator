#!/usr/bin/env python3

#note lengths are in seconds, and based on 120 BPM (MIDI standard)
# TODO: implement triplets, duplets and quarduplets. Skipping for now because math is hard:
# triplets since they are real irrational numbers will cause beat to slowly become OOS. So we would need to account for that somehow...
WESTERN_NOTE_TYPES = [
    0.0625,
    0.125,
    0.1875,
    0.25,
    0.375,
    0.5,
    0.75,
    1.0,
    1.5,
    2.0
]

WHOLE = 2.0
DOTTED_HALF = 1.5
HALF = 1.0
DOTTED_QUARTER = 0.75
QUARTER = 0.5
DOTTED_EIGHTH = 0.375
EIGHTH = 0.25
DOTTED_SIXTEENTH = 0.1875
SIXTEENTH = 0.125
THIRTYSECOND = 0.0625
