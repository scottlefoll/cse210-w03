import random

MAX_WRONG_GUESSES = 10


class Jumper:
    """The person trying to guess the word.

    The responsibility of a Jumper is to keep track of the letters it has
    guessed, and to return True if the # of wrong guesses = the # of 
    max wrong guesses.

    Attributes:
        letters_guessed (list): The list of letters guessed by Jumper.
        wrong_guesses (int): The number of wrong guesses.
        letter (string): The letter guessed by Jumper.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letters_guessed_lst = []
        self.wrong_guesses = 0
        self.letter = ""

    def get_letters_guessed(self):
        """Gets the list of letters guessed.

        Returns:
            list: The list of letters guessed
        """

        return self._letters_guessed_lst

    def set_letters_guessed(self, letter):
        """Sets the letter_guessed attribute.

        Args:
            self (Jumper): An instance of Jumper.
            _letter_guessed (string): The letter guessed.
        """
        self._letters_guessed_lst.append(letter)

    def is_max_guesses_reached(self):
        """Checks if the max wrong guesses has been reached.

        Args:
            self (Jumper): An instance of Jumper.

        Returns:
            boolean: True if max guesses has been reached; false if otherwise.
        """
        return (self.wrong_guesses == MAX_WRONG_GUESSES)
