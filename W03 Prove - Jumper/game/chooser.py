import random
from nltk.corpus import words


class Chooser:
    """Chooses the word that the guesser needs to guess. The word is chosen
    from a list of all English words. The responsibility of Chooser is to keep
    track of the word, and which letters have been guessed correctly, and
    incorrectly.

    Attributes:
        _word_list (list): A list of all English words.
        _word (str): The word that needs to be guessed.
        _word_letters (list): A list of the letters in the chosen word.
    """

    def __init__(self):
        """Constructs a new Chooser.

        Args:
            self (Chooser): An instance of Chooser.
        """

        self._words_lst = words.words()
        print(len(self._words_lst))
        self._word = random.choice(self._words_lst)
        print(self.word)
        self._word_letters_lst = list(self._word)

    # def get_hint(self):
    #     Gets a hint for the seeker.

    #     Args:
    #         self (Hider): An instance of Hider.

    #     Returns:
    #         string: A hint for the seeker.
    #     """
    #     hint = "(-.-) Nap time."
    #     if self._distance[-1] == 0:
    #         hint = "(;.;) You found me!"
    #     elif self._distance[-1] > self._distance[-2]:
    #         hint = "(^.^) Getting colder!"
    #     elif self._distance[-1] < self._distance[-2]:
    #         hint = "(>.<) Getting warmer!"
    #     return hint

    def is_landed(self):
        """Whether or not the jumper has won, or "landed."

        Args:
            self (guesser): An instance of Guesser.

        Returns:
            boolean: True if the guesser has landed; false if otherwise.
        """
        lst = self._word_lst
        return (len(self._letters_correct_lst) == len(lst))

    def is_guess_correct(self, letter):
        """Tracks the  correct letters guessed by the Guesser.

        Args:
            self (Chooser): An instance of Chooser.
            letter (string): The letter guessed.
        Returns:
            boolean: True if the guess is correct; false if incorrect.
        """
        lst = self._word_lst
        if letter in lst:
            # add letter to the guessed letters list
            self._letters_guessed_lst.append(letter)
            # use list comprehension to replace letter in lst with "_"
            lst = ["_" if item == letter else item for item in lst]
            return True
        else:
            self.wrong_guesses += 1
            return False


    def is_max_guesses_reached(self):
        """Checks if the max guesses has been reached.

        Args:
            self (Chooser): An instance of Chooser.

        Returns:
            boolean: True if max guesses has been reached; false if otherwise.
        """
        return self.wrong_guesses == MAX_GUESSES