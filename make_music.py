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
        notes_to_midi("D4 F4 A4 C5 E5 G5"),
        notes_to_midi("D4 G4 A#4 D5 F5 A#5"),
        notes_to_midi("D4 F4 A4 C5 E5 G5"),
        notes_to_midi("D#4 F#4 A#4 C#5 F5 G#5"),
        notes_to_midi("C#4 E4 G4 A#5 C#5 E5 G5")
    ]

    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=0, time=0))

    drum_track = MidiTrack()
    mid.tracks.append(drum_track)

    # Program change is not needed for drums on channel 9, but you can set velocity and timing
    # Define drum notes (e.g., bass drum = 35, snare = 38, closed hi-hat = 42)
    bass_drum = 35
    snare = 38
    hi_hat = 42

    # Simple drum pattern loop
    for i in range(5 * len(chords)):
        time_between_hits = 480  # adjust timing to match chord rhythm

        # Bass drum on beats 1 and 3
        drum_track.append(Message('note_on', channel=9, note=bass_drum, velocity=100, time=0 if i == 0 else time_between_hits))
        drum_track.append(Message('note_off', channel=9, note=bass_drum, velocity=0, time=120))

        # Snare on beats 2 and 4
        drum_track.append(Message('note_on', channel=9, note=snare, velocity=100, time=time_between_hits))
        drum_track.append(Message('note_off', channel=9, note=snare, velocity=0, time=120))

        # Hi-hat on every beat
        drum_track.append(Message('note_on', channel=9, note=hi_hat, velocity=80, time=time_between_hits))
        drum_track.append(Message('note_off', channel=9, note=hi_hat, velocity=0, time=100))


    for i in range(5):
        for chord in chords:
            # Play chord
            for note in chord:
                track.append(Message('note_on', note=note, velocity=50, time=0))

            # Hold the chord for a while
            if chord == notes_to_midi("D#4 F#4 A#4 C#5 F5 G#5") or chord == notes_to_midi("C#4 E4 G4 A#5 C#5 E5 G5"):
                hold_time = 1080 # We are making the last two chords play for half the time
                                # beacuse that sounds a lot better
            else:
                hold_time = 2160

            track.append(Message('note_off', note=chord[0], velocity=50, time=hold_time))
            for note in chord[1:]:
                track.append(Message('note_off', note=note, velocity=50, time=0))

            # Add a pause after the chord fades (rest time)
            rest_time = 12  # this is the silence before next chord
            track.append(Message('note_on', note=0, velocity=0, time=rest_time))  # dummy to create time gap

    mid.save('./music/lofi_chords.mid')
    print("Saved: lofi_chords.mid")


if __name__ == '__main__':
    make_music()
