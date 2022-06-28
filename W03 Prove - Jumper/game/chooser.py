import random
# from nltk.corpus import words


class Chooser:
    """Chooses the word that the guesser needs to guess. The word is chosen
    from a list of all English words. The responsibility of Chooser is to keep
    track of the word, and which letters have been guessed correctly, and
    incorrectly.

    Attributes:
        _word_list (list): A list of all English words.
        _word (str): The word that needs to be guessed.
        _word_lst (list): A list of the letters in the chosen word, with
        guessed letters replace by an underscore ("_").
        _wrong_guesses (int): The number of wrong guesses made by the guesser.

    """

    def __init__(self):
        """Constructs a new Chooser.

        Args:
            self (Chooser): An instance of Chooser.
        """

        # self._words_lst = words.words()
        self._words_lst = ['small', 'large', 'medium', 'tiny', 'huge',
                           'ridiculous', 'tiny', 'large', 'medium', 'small', 
                           'huge', 'ridiculous']
        self._word = random.choice(self._words_lst)
        self._word_lst = list(self._word)

    def is_landed(self):
        """Whether or not the jumper has won, or "landed."

        Args:
            self (guesser): An instance of Guesser.

        Returns:
            boolean: True if the guesser has landed; false if otherwise.
        """
        if "__" in self._word_lst:
            return False
        else:
            return True

    def is_correct(self, letter):
        """Returns True if the letter guessed by the Jumper is correct.

        Args:
            self (Chooser): An instance of Chooser.
            letter (string): The letter guessed.
        Returns:
            boolean: True if the guess is correct; false if incorrect.
        """
        if letter in self._word_lst:
            return True
        else:
            return False

    def get_word(self, lst):
        """Returns the word that the jumper needs to guess, with underscores
        in place of any unguessed letters.

        Args:
            self (Chooser): An instance of Chooser.
            lst (list): The list of letters guessed.

        Returns:
            string: The word that the guesser needs to guess, with underscores
            in place of unguessed letters.
        """
        lst2 = self._word_lst
        self._word = join(['__' if item not in lst else item for item
                          in lst2], "")
        return self._word

