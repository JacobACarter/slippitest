import pandas as pd
import slippi as slp
import os

game = slp.Game('slpfiles\Game_20230127T201933.slp')
print(type(game))

print(game.frames[0])