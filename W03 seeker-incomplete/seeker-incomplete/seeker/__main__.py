"""Seeker

I once met a lady named Lark,
With whom I would play in the park;
We'd play hide and seek,
Frolic in the creek,
Which was fine until she started to bark.

- Regis Auffray -

Overview

Seeker is a game in which the player seeks to find the hider by guessing its location. The hider gives hints until it is found.

Rules

Seeker is played according to the following rules.

The hider's location is a random number between 1 and 1000.
The seeker searches for the hider by guessing its location.
If the guess is closer to the hider's location it says, "Getting warmer!"
If the guess is farther away from the hider's location it says, "Getting colder!"
If the guess is correct the hider says, "You found me!". The game is over.

Requirements

The program must also meet the following requirements.

The program must include a README file.
The program must include class and method comments.
The program must have at least four classes.
The program must remain true to game play described in the overview.

Have Some Fun

Have some fun by enhancing the game any way you like. A few ideas are as follows.

Enhanced input validation.
Enhanced game play and game over messages.
Enhanced game display, e.g. different hints"""


from game.director import Director

director = Director()
director.start_game()