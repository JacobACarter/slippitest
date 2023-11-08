# slippitest
This is a personal project of mine to create a Neural Network that can play Super Smash Brothers Melee.
With the use of the emulator dolphin, much data can be recorded about a specific game. For every frame, it knows:
  *The position of both players
  *Their velocity
  *Their current action
  *Their damage taken
My idea was to use the massive dataset that is my personal game files (which totals to over 300 games played) to train
a neural network to play like me. This bot would be unique in its attenpt to emulate a specific human, and I believe it 
could be the next step in training when it comes to Melee.

I'm using TensorFlow for the neural network, and the melee library to interact with dolphin and create a bot.
