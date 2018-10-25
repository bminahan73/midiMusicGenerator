#!/usr/bin/env python3

#example usage

import midiMusicGenerator
from midiMusicGenerator import pitches, notetypes, scales

pitches = scales.C_NATURAL_MINOR
note_types = [notetypes.QUARTER, notetypes.EIGHTH]

con = midiMusicGenerator.open_midi_connection()
midiMusicGenerator.play_scale(con=con, scale=scales.C_MAJOR)
midiMusicGenerator.play_notes(con=con, num_notes=100, pitches=pitches, note_types=note_types)
midiMusicGenerator.close_midi_connection(con)
