#!/usr/bin/env python3

import midiMusicGenerator

con = midiMusicGenerator.open_midi_connection()
midiMusicGenerator.list_available_midi_ports(con)
midiMusicGenerator.close_midi_connection(con)
