import random
from mido import Message, MidiFile, MidiTrack

# Chords for C - Am - F - G progression
chords = [
    [60, 64, 67],  # C major
    [57, 60, 64],  # A minor
    [53, 57, 60],  # F major
    [55, 59, 62]   # G major
]

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=0, time=0))

for chord in chords * 8:  # Repeat 8 times
    for note in chord:
        track.append(Message('note_on', note=note, velocity=50, time=0))
    for note in chord:
        track.append(Message('note_off', note=note, velocity=50, time=960))  # longer hold

mid.save('./music/lofi_chords.mid')
print("Saved: lofi_chords.mid")