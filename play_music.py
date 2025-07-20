import tinysoundfont
import time

def play_music():
    synth = tinysoundfont.Synth()
    #sfid = synth.sfload("./music/module90.sf2") # Synth
    sfid = synth.sfload("./music/Double_Felt_Grand.sf2") # Piano

    seq = tinysoundfont.Sequencer(synth)
    seq.midi_load("./music/lofi_chords.mid")

    # Larger buffer because latency is not important
    synth.start(buffer_size=4096)

    while not seq.is_empty():
        time.sleep(0.5)

if __name__ == '__main__':
    play_music()