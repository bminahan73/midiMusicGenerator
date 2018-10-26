#!/usr/bin/env python3

#example usage

import midiMusicGenerator as m
from midiMusicGenerator import pitches, notetypes, scales, velocities, chords

con = m.open_midi_connection()
m.play_scale(con=con, scale=scales.D_NATURAL_MINOR)
m.rest(notetypes.QUARTER)
m.play_chord_from_root(con=con, root_note=pitches.D4, chord=chords.MAJOR + [-12,-17], note_type=notetypes.QUARTER)
m.play_chord(con=con, chord=[scales.D_MAJOR[0], scales.D_MAJOR[3], scales.D_MAJOR[5]], note_type=notetypes.QUARTER)
m.play_chord(con=con, chord=m.get_chord_notes(pitches.D4, chords.MAJOR), note_type=notetypes.QUARTER)
m.close_midi_connection(con)
