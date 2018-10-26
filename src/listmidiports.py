#!/usr/bin/env python3

import midiMusicGenerator as m

con = m.open_midi_connection()
m.list_available_midi_ports(con)
m.close_midi_connection(con)
