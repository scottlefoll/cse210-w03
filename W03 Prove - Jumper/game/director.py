from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.chooser import Chooser


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        chooser (Chooser): The game's chooser.
        is_playing (boolean): Whether or not to keep playing.
        Jumper (Jumper): The game's jumper.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._chooser = Chooser()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
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
        """Asks the guesser for a new letter.

        Args:
            self (Director): An instance of Director.
        """
        new_letter = self._terminal_service.read_letter("\nEnter a letter [a - z]: ")
        self._jumper.set_letter(new_letter)
        
    def _do_updates(self):
        """Keeps track of which letters the guesser has guessed.

        Args:
            self (Director): An instance of Director.
        """
        self._chooser.track_letters(self._jumper.get_letters_guessed())
        
    def _do_outputs(self):
        """Provides a hint for the jumper to use.

        Args:
            self (Director): An instance of Director.
        """
        # hint = self._chooser.get_hint()
        # self._terminal_service.write_text(hint)
        if self._chooser.is_landed():
            self._is_playing = False

        self._terminal_service.write_text(scoreboard)

    def _do_scoreboard(Self):
        """Provides a scoreboard for the guesser to use.

        Args:
            self (Director): An instance of Director.
        """
        _terminal_service.write_text(scoreboard)
