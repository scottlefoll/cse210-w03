import random
# from nltk.corpus import words


class Chooser:
    """Chooses the word that the guesser needs to guess. The word is chosen
    from a list of all English words. The responsibility of Chooser is to keep
    track of the word, and which letters have been guessed correctly, and
    incorrectly.

    Attributes:
        _words_list (list): A list of all English words.
        _word (str): The word that needs to be guessed.
        _word_lst (list): A list of the letters in the chosen word, with
        guessed letters replace by an underscore ("_").

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
        self.get_word([])



    def is_landed(self):
        """Returns whether or not the jumper has landed (i.e. won)

        Args:
            self (guesser): An instance of Jumper.

        Returns:
            boolean: True if the jumper has landed; false if otherwise.
        """

        test = '_'

        if '_' in self._word:
            return False
            print("Is_landed = False")
        else:
            print("Is_landed = True")
            print("Word = " + self._word)
            # If the word does not contain any un-guessed letters ('_'), then is_landed = True
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
        in place of any un-guessed letters.

        Args:
            self (Chooser): An instance of Chooser.
            lst (list): The list of letters guessed.

        Returns:
            string: The word that the guesser needs to guess, with underscores
            in place of un-guessed letters.
        """
        lst2 = self._word_lst
        mySep = ''
        self._word = mySep.join(['_ ' if item not in lst else item for item
                          in lst2])
        print(f"Word = {self._word}")
        return self._word

