import random

MAX_WRONG_GUESSES = 12


class Jumper:
    """The person trying to guess the word.

    The responsibility of a Jumper is to keep track of the letters it has
    guessed, the number of wrong guesses, andd to return True if the # of 
    wrong guesses = the # of max wrong guesses. Also to return the jumper and 
    parachute based upon the number of wrong guesses remaining.

    Attributes:
        letters_guessed (list): The list of letters guessed by Jumper.
        wrong_guesses (int): The number of wrong guesses.
        letter (string): The letter guessed by Jumper.
        chute1-chute12 (strings): The chutes drawn by Jumper.(the scoreboard)
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letters_guessed_lst = []
        self._wrong_guesses = 0
        self._letter = ""


        self.chute0 = """
                    ___
                   /___\  
                   \   /
                    \ / 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute1 = """
                    __
                   /___\  
                   \   /
                    \ / 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute2 = """
                    _
                   /___\  
                   \   /
                    \ / 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute3 = """
                    
                   /___\  
                   \   /
                    \ / 
                     O
                    /|\
                    / \ 


                  ^^^^^^^
                    """

        self.chute4 = """
                    
                   /___
                   \   /
                    \ / 
                     O
                    /|\
                    / \


                  ^^^^^^^
                    """

        self.chute5 = """
                    
                   ___  
                   \   /
                    \ / 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute6 = """
                    
                   _
                   \   /
                    \ / 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute7 = """
                    
                    
                   \   /
                    \ / 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute8 = """
                    
                    
                   \   
                    \ / 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute9 = """
                    
                    
                    
                    \ / 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute10 = """
                    
                    
                    
                    \ 
                     O
                    /|\
                    / \   


                  ^^^^^^^
                    """

        self.chute11 = """
                    
                    
                    
                    
                     X
                    /|\
                    / \   


                  ^^^^^^^
                    """

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

    def get_chute(self):
        """Returns the chute.

        Args:
            self (Jumper): An instance of Jumper.

        Returns:
            string: The chute.
        """

        match self._wrong_guesses:
            case 0:
                return self.chute0
            case 1:
                return self.chute1
            case 2:
                return self.chute2
            case 3:
                return self.chute3
            case 4:
                return self.chute4
            case 5:
                return self.chute5
            case 6:
                return self.chute6
            case 7:
                return self.chute7
            case 8:
                return self.chute8
            case 9:
                return self.chute9
            case 10:
                return self.chute10
            case 11:
                return self.chute11
            case 12:
                return self.chute12
