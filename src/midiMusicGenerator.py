#!/usr/bin/env python3

import os
import time
import rtmidi
import random

import pitches, notetypes, events, scales

def open_midi_connection():
    con = rtmidi.MidiOut()
    available_ports = con.get_ports()
    if available_ports:
        try:
            port = available_ports.index(os.environ['MIDI_PORT'])
        except KeyError:
            print('MIDI_PORT environment variable is not set, so we will assign to the first midi out.')
            port = 0
        finally:
            con.open_port(port)
    else:
        con.open_virtual_port('python virtual MIDI port')
        print('No availible midi output devices detected, so we will open a virtual device.')
    return con


def close_midi_connection(con):
    del con


def list_available_midi_ports(con):
    available_ports = con.get_ports()
    print('available ports are: {0}'.format(available_ports))


def play_notes(con, num_notes=10, velocities=events.VELOCITY_RANGE, pitches=pitches.MIDI_NOTE_RANGE, note_types=notetypes.EASTERN_NOTE_TYPES):
    notes = []
    for i in range(0,num_notes):
        velocity = random.choice(velocities)
        pitch = random.choice(pitches)
        note_type = random.choice(note_types)
        notes.append( { 'pitch': pitch, 'velocity': velocity, 'length': note_type } )
    for note in notes:
        con.send_message( [ events.NOTE_ON, note['pitch'], note['velocity'] ] )
        time.sleep(note['length'])
        con.send_message( [ events.NOTE_OFF, note['pitch'], note['velocity'] ] )


def play_single_note(con, pitch, note_type=notetypes.QUARTER, velocity=65):
    con.send_message( [ events.NOTE_ON, pitch, velocity ] )
    time.sleep(note_type)
    con.send_message( [ events.NOTE_OFF, pitch, velocity ] )


def play_scale(con, scale, note_type=notetypes.QUARTER, velocity=65):
    for note in scale:
        play_single_note(con=con, pitch=note, note_type=note_type, velocity=velocity)

    for note in reversed(scale):
        if scale.index(note) == len(scale) - 1:
            pass
        else:
            play_single_note(con=con, pitch=note, note_type=note_type)


if __name__ == '__main__':
    con = open_midi_connection()
    play_notes(con)
    close_midi_connection(con)
