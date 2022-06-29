MAX_GUESSES = 12


class Jumper:
    """The person trying to guess the word.

    The responsibility of a Jumper is to keep track of the letters it has
    guessed, the number of wrong guesses, and to return True if the # of
    wrong guesses = the # of max wrong guesses. Also, to return the jumper and
    parachute based upon the number of wrong guesses remaining.

    Attributes:
        _guessed_lst (list): The list of letters guessed by Jumper.
        _letter_guessed (string): The letter guessed by Jumper.
        _wrong_guesses (int): The number of wrong guesses made by Jumper.
        _chute1-chute12 (strings): The chutes drawn by Jumper.(the scoreboard)
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._guessed_lst = []
        self._letter_guessed = ""
        self._wrong_guesses = 0
        self._chute0 = """
  ___
 /___\\
\\   /
 \\ /
   O
  /|\\
  / \\


^^^^^^^
"""

        self._chute1 = """
    __
   /___\
   \   /
    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute2 = """
    _
   /___\
   \   /
    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute3 = """

   /___\
   \   /
    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute4 = """

   /___
   \   /
    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute5 = """
   ___
   \   /
    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute6 = """
   _
   \   /
    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute7 = """

   \   /
    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute8 = """

   \
    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute9 = """

    \ /
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute10 = """

    \
     O
    /|\
    / \


  ^^^^^^^
"""

        self._chute11 = """

     X
    /|\
    / \
  ^^^^^^^
"""

    def set_letter_guessed(self, letter, correct):
        """Sets the letter_guessed attribute. Adds the letter to the
        list of letters guessed.

        Args:
            self (Jumper): An instance of Jumper.
            letter (string): The letter guessed.
            correct (boolean): True if the letter is correct, else false.
        """
        self._letter_guessed = letter
        # add letter to the guessed letters list
        self._guessed_lst.append(letter)
        print(f"Letter = {letter}")
        print(f"Letter lst = {self._guessed_lst}")
        # if the letter is correct, increment the wrong guesses counter
        if not correct:
            self._wrong_guesses += 1
            print(f"Letter = {letter}")
        return

    def get_letters_guessed(self):
        """Gets the list of letters guessed.

        Returns:
            list: The list of letters guessed
        """

        return self._guessed_lst

    def is_crashed(self):
        """Checks if jumper has crashed (max wrong guesses has been reached).

        Args:
            self (Jumper): An instance of Jumper.

        Returns:
            boolean: True if max guesses has been reached; false if otherwise.
        """
        print("Wrong_guesses = ", self._wrong_guesses)
        print("MAX_GUESSES = ", MAX_GUESSES)
        return self._wrong_guesses == MAX_GUESSES

    def get_chute(self):
        """Returns the chute.

        Args:
            self (Jumper): An instance of Jumper.

        Returns:
            string: The chute.
        """

        match self._wrong_guesses:
            case 0:
                return self._chute0
            case 1:
                return self._chute1
            case 2:
                return self._chute2
            case 3:
                return self._chute3
            case 4:
                return self._chute4
            case 5:
                return self._chute5
            case 6:
                return self._chute6
            case 7:
                return self._chute7
            case 8:
                return self._chute8
            case 9:
                return self._chute9
            case 10:
                return self._chute10
            case 11:
                return self._chute11
