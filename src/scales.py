#!/usr/bin/env python3

import pitches

C_MAJOR = [60, 62, 64, 65, 67, 69, 71, 72]
CS_MAJOR = [61, 63, 65, 66, 68, 70, 72, 73]
D_MAJOR = [62, 64, 66, 67, 69, 71, 73, 74]
DS_MAJOR = [63, 65, 67, 68, 70, 72, 74, 75]
E_MAJOR = [64, 66, 68, 69, 71, 73, 75, 76]
F_MAJOR = [65, 67, 69, 70, 72, 74, 76, 77]
FS_MAJOR = [66, 68, 70, 71, 73, 75, 77, 78]
G_MAJOR = [67, 69, 71, 72, 74, 76, 78, 79]
GS_MAJOR = [68, 70, 72, 73, 75, 77, 79, 80]
A_MAJOR = [69, 71, 73, 74, 76, 78, 80, 81]
AS_MAJOR = [70, 72, 74, 75, 77, 79, 81, 82]
B_MAJOR = [71, 73, 75, 76, 78, 80, 82, 83]
DB_MAJOR = [61, 63, 65, 66, 68, 70, 72, 73]
EB_MAJOR = [63, 65, 67, 68, 70, 72, 74, 75]
GB_MAJOR = [66, 68, 70, 71, 73, 75, 77, 78]
AB_MAJOR = [68, 70, 72, 73, 75, 77, 79, 80]
BB_MAJOR = [70, 72, 74, 75, 77, 79, 81, 82]
C_NATURAL_MINOR = [60, 62, 63, 65, 67, 68, 70, 72]
CS_NATURAL_MINOR = [61, 63, 64, 66, 68, 69, 71, 73]
D_NATURAL_MINOR = [62, 64, 65, 67, 69, 70, 72, 74]
DS_NATURAL_MINOR = [63, 65, 66, 68, 70, 71, 73, 75]
E_NATURAL_MINOR = [64, 66, 67, 69, 71, 72, 74, 76]
F_NATURAL_MINOR = [65, 67, 68, 70, 72, 73, 75, 77]
FS_NATURAL_MINOR = [66, 68, 69, 71, 73, 74, 76, 78]
G_NATURAL_MINOR = [67, 69, 70, 72, 74, 75, 77, 79]
GS_NATURAL_MINOR = [68, 70, 71, 73, 75, 76, 78, 80]
A_NATURAL_MINOR = [69, 71, 72, 74, 76, 77, 79, 81]
AS_NATURAL_MINOR = [70, 72, 73, 75, 77, 78, 80, 82]
B_NATURAL_MINOR = [71, 73, 74, 76, 78, 79, 81, 83]
DB_NATURAL_MINOR = [61, 63, 64, 66, 68, 69, 71, 73]
EB_NATURAL_MINOR = [63, 65, 66, 68, 70, 71, 73, 75]
GB_NATURAL_MINOR = [66, 68, 69, 71, 73, 74, 76, 78]
AB_NATURAL_MINOR = [68, 70, 71, 73, 75, 76, 78, 80]
BB_NATURAL_MINOR = [70, 72, 73, 75, 77, 78, 80, 82]
C_HARMONIC_MINOR = [60, 62, 63, 65, 67, 68, 71, 72]
CS_HARMONIC_MINOR = [61, 63, 64, 66, 68, 69, 72, 73]
D_HARMONIC_MINOR = [62, 64, 65, 67, 69, 70, 73, 74]
DS_HARMONIC_MINOR = [63, 65, 66, 68, 70, 71, 74, 75]
E_HARMONIC_MINOR = [64, 66, 67, 69, 71, 72, 75, 76]
F_HARMONIC_MINOR = [65, 67, 68, 70, 72, 73, 76, 77]
FS_HARMONIC_MINOR = [66, 68, 69, 71, 73, 74, 77, 78]
G_HARMONIC_MINOR = [67, 69, 70, 72, 74, 75, 78, 79]
GS_HARMONIC_MINOR = [68, 70, 71, 73, 75, 76, 79, 80]
A_HARMONIC_MINOR = [69, 71, 72, 74, 76, 77, 80, 81]
AS_HARMONIC_MINOR = [70, 72, 73, 75, 77, 78, 81, 82]
B_HARMONIC_MINOR = [71, 73, 74, 76, 78, 79, 82, 83]
DB_HARMONIC_MINOR = [61, 63, 64, 66, 68, 69, 72, 73]
EB_HARMONIC_MINOR = [63, 65, 66, 68, 70, 71, 74, 75]
GB_HARMONIC_MINOR = [66, 68, 69, 71, 73, 74, 77, 78]
AB_HARMONIC_MINOR = [68, 70, 71, 73, 75, 76, 79, 80]
BB_HARMONIC_MINOR = [70, 72, 73, 75, 77, 78, 81, 82]


def shift_notes_octave(notes, shift_amount):
    shifted_notes = [];
    for note in notes:
        shifted_notes.append(note + (shift_amount * 12))
    return shifted_notes


def shift_notes(notes, shift_amount):
    shifted_notes = [];
    for note in notes:
        shifted_notes.append(note + shift_amount)
    return shifted_notes