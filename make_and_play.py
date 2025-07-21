from make_music import *
from play_music import *

seed = random.randint(1,10000)
make_music(drums=True, seed=seed)
print(seed)
play_music()