from make_music import *
from play_music import *


drums = input("Drums? (Y/n): ")
if drums == 'n':
    drums = False
else:
    drums = True
seed = input("Seed? (Leave Blank for random)")
if type(seed) == int:
    make_music(drums=drums, seed = seed)
else:
    seed = random.randint(1,100000)
    make_music(drums=drums, seed = seed)

print(f"Using seed '{seed}'")
play_music()