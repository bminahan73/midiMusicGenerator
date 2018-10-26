#!/usr/bin/env python3

import os
import time
import rtmidi
import random

import pitches, notetypes, events, scales, velocities, chords

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
        print('No availible midi output devices detected, so we will open a virtual device.')
        con.open_virtual_port('python virtual MIDI port')
    return con


def close_midi_connection(con):
    del con


def list_available_midi_ports(con):
    available_ports = con.get_ports()
    print('available ports are: {0}'.format(available_ports))


def shift_notes(notes, shift_amount):
    shifted_notes = [];
    for note in notes:
        shifted_notes.append(note + shift_amount)
    return shifted_notes


def shift_notes_octave(notes, shift_amount):
    shifted_notes = [];
    for note in notes:
        shifted_notes.append(note + (shift_amount * 12))
    return shifted_notes


def play_single_note(con, pitch, note_type=notetypes.QUARTER, velocity=velocities.VELOCITY_MF):
    con.send_message( [ events.NOTE_ON, pitch, velocity ] )
    time.sleep(note_type)
    con.send_message( [ events.NOTE_OFF, pitch, velocity ] )


def play_chord(con, chord, note_type, velocity=velocities.VELOCITY_MF):
    for note in chord:
        con.send_message( [ events.NOTE_ON, note, velocity ] )
    time.sleep(note_type)
    for note in chord:
        con.send_message( [ events.NOTE_OFF, note, velocity ] )


def get_chord_notes(root_note, chord):
    chord_from_root = []
    for pitch_adjustment in chord:
        note = root_note + pitch_adjustment
        chord_from_root.append(note)
    return chord_from_root


def play_chord_from_root(con, root_note, chord, note_type, velocity=velocities.VELOCITY_MF):
    for pitch_adjustment in chord:
        pitch = root_note + pitch_adjustment
        con.send_message( [ events.NOTE_ON, pitch, velocity ] )
    time.sleep(note_type)
    for pitch_adjustment in chord:
        pitch = root_note + pitch_adjustment
        con.send_message( [ events.NOTE_OFF, pitch, velocity ] )


def rest(note_type):
    time.sleep(note_type)


def play_notes(con, num_notes=10, velocities=velocities.VELOCITY_RANGE, pitches=pitches.MIDI_NOTE_RANGE, note_types=notetypes.WESTERN_NOTE_TYPES):
    notes = []
    for i in range(0,num_notes):
        velocity = random.choice(velocities)
        pitch = random.choice(pitches)
        note_type = random.choice(note_types)
        notes.append( { 'pitch': pitch, 'note_type': note_type, 'velocity': velocity,} )
    for note in notes:
        play_single_note(con, pitch=note['pitch'], note_type=note['note_type'], velocity=note['velocity'])


def play_scale(con, scale, note_type=notetypes.QUARTER, velocity=velocities.VELOCITY_MF):
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
