from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.chooser import Chooser


class Director:
    """A person who directs the game.
    The director is in charge of the game, & to control the sequence of play.

    Attributes:
        chooser (Chooser): The game's chooser.
        is_playing (boolean): Whether or not to keep playing.
        Jumper (Jumper): The game's jumper.
        terminal_service: For getting and displaying information in the
        terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._chooser = Chooser()
        self._is_playing = True
        self._jumper = Jumper()
        self._ts = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets the letter guessed by the Jumper.

        Args:
            self (Director): an instance of Director.
        """
        new_letter = self._ts.read_text("\nEnter a letter [a - z]: ",
                                        min_length=1, max_length=1)
        self._jumper.set_letter_guessed(new_letter)
        if self._chooser.is_landed():
            self._is_playing = False
            return
        if self._jumper.is_crashed:
            self._is_playing = False
            return

    def _do_updates(self):
        """Keeps track of which letters the guesser has guessed.

        Args:
            self (Director): An instance of Director.
        """
        self._chooser.get_word(f"\n{self._jumper.get_letters_guessed()}")

    def _do_outputs(self):
        """Send output to the screen.

        Args:
            self (Director): An instance of Director, 
            prompt (string): The prompt to display.
        """
        if self.is_landed():
            self._ts.write_text("\nCongratulations, you are on the ground!")
        elif self._jumper.is_max_guesses():
            self._ts.write_text("\nSorry, you crashed!")
        else:
            self._ts.write_text(f"\n{self.jumper.get_chute()}")
