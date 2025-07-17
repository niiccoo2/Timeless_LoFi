import random
from mido import Message, MidiFile, MidiTrack

note_to_semitone = {
    'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
    'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
}

def notes_to_midi(note_str):
    midi_notes = []
    notes = note_str.split()
    for note in notes:
        # Separate note name from octave
        if len(note) == 2:
            name, octave = note[0], int(note[1])
            accidental = ''
        else:
            # For sharps or flats like C#4 or Db3
            if note[1] in ['#', 'b']:
                name, accidental, octave = note[0], note[1], int(note[2])
                name = name + accidental
            else:
                name, octave = note[0], int(note[1])
        semitone = note_to_semitone[name]
        midi_number = (octave + 1) * 12 + semitone
        midi_notes.append(midi_number)
    return midi_notes

def make_music(seed=None):
    if seed is not None:
        random.seed(seed)

    chords = [
        notes_to_midi("D3 F3 A3 C4 E4 G4"),
        notes_to_midi("D3 G3 Bb3 D4 F4 Bb4"),
        notes_to_midi("D3 F3 A3 C4 E4 G4"),
        notes_to_midi("Eb3 Gb3 Bb3 Db4 F4 Ab4"),
        notes_to_midi("Db3 E3 G3 Bb3 Db4 E4 G4")
    ]

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=0, time=0))

    for chord in chords:
        # Play chord
        for note in chord:
            track.append(Message('note_on', note=note, velocity=50, time=0))

        # Hold the chord for a while
        hold_time = 720  # duration all notes are sustained
        track.append(Message('note_off', note=chord[0], velocity=50, time=hold_time))
        for note in chord[1:]:
            track.append(Message('note_off', note=note, velocity=50, time=0))

        # Add a pause after the chord fades (rest time)
        rest_time = 480  # this is the silence before next chord
        track.append(Message('note_on', note=0, velocity=0, time=rest_time))  # dummy to create time gap

    mid.save('./music/lofi_chords.mid')
    print("Saved: lofi_chords.mid")


if __name__ == '__main__':
    make_music()
