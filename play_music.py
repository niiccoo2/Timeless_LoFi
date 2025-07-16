import tinysoundfont
import time

synth = tinysoundfont.Synth()
sfid = synth.sfload("florestan-subset.sfo")

seq = tinysoundfont.Sequencer(synth)
seq.midi_load("lofi_chords.mid")

# Larger buffer because latency is not important
synth.start(buffer_size=4096)

while not seq.is_empty():
    time.sleep(0.5)