from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.chooser import Chooser


class Director:
    """A person who directs the game.
    The director is in charge of the game, & to control the sequence of play.

    Attributes:
        _chooser (Chooser): The game's chooser.
        _jumper (Jumper): The game's jumper.
        _ts (TerminalService): For getting and displaying information in the
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
                                        case='lower',
                                        min_length=1,
                                        max_length=1)
        correct = self._chooser.is_correct(new_letter)
        self._jumper.set_letter_guessed(new_letter, correct)
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
        guessed_lst = self._jumper.get_letters_guessed()
        self._chooser.get_word(guessed_lst)

    def _do_outputs(self, prompt=''):
        """Send output to the screen.

        Args:
            self (Director): An instance of Director,
            prompt (string): The prompt to display.
        """
        if prompt != '':
            self._ts.write_text(prompt)
            return

        if self._chooser.is_landed():
            self._ts.write_text("\nCongratulations, you are safely on the ground!")
        elif self._jumper.is_crashed():
            self._ts.write_text("\nSorry, you crashed!")
        else:
            self._ts.write_text(f"\n{self._chooser.get_word(self._jumper.get_letters_guessed())}")
            self._ts.write_text(f"\n{self._jumper.get_chute()}")
