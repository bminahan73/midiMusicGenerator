#!/usr/bin/env python3

#example usage

import midiMusicGenerator as m
from midiMusicGenerator import pitches, notetypes, scales, velocities, chords

con = m.open_midi_connection()
#scale takes a list of MIDI notes and plays them up and down.
m.play_scale(con=con, scale=scales.D_NATURAL_MINOR)
#rest will simply call sleep on the MIDI connection for desired time.
m.rest(notetypes.QUARTER)
#play chord from root takes a root pitch (the I), and plays notes simltaneously offest from that pitch (1 half step up, -1 half step down)
m.play_chord_from_root(con=con, root_note=pitches.D4, chord=chords.MAJOR + [-12,-17], note_type=notetypes.QUARTER)
#play chord takes a series of arbitrary notes and plays them simultaneously
m.play_chord(con=con, chord=[scales.D_MAJOR[0], scales.D_MAJOR[3], scales.D_MAJOR[5]], note_type=notetypes.QUARTER)
#get_chord_notes takes a root note and and a list of offsets, and returns a list of pitches.
m.play_chord(con=con, chord=m.get_chord_notes(pitches.D4, chords.MAJOR), note_type=notetypes.QUARTER)
m.close_midi_connection(con)
