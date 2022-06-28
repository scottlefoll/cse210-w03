class TerminalService:
    """A service that handles terminal operations.

    The responsibility of a TerminalService is to provide input and output
    operations for the terminal.
    """

    def read_text(self, prompt, max_length='', min_length='',
                  case='', constraint_lst=''):
        """Gets text input from the terminal. Directs the user with the given
        prompt.

        Args:
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """

        while True:
            if case == "lower":
                input_txt = input(prompt).lower()
            elif case == "upper":
                input_txt = input(prompt).upper()
            elif case == "title":
                input_txt = input(prompt).title()
            
            if max_length != '' and len(input_txt) > max_length:
                print(f"Please enter fewer than {max_length+1} characters.")
                continue
            elif min_length != '' and len(input_txt) < min_length:
                print(f"Please enter more than {min_length-1} characters.")
                continue
            elif constraint_lst != '' and input_txt not in constraint_lst:
                print("Please enter a valid option.")
                continue
            else:
                return input_txt


    def read_number(self, prompt, max_value='', min_value='', decimals=0):
        """Gets numerical input from the terminal. Directs the user with the
        given prompt.

        Args:
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """


        while True:
            try:

                if decimals == 0:
                    input_num = int(input(prompt))
                else:
                    input_num = float(input(prompt))

                if max_value != '' and input_num > max_value:
                    print(f"Please enter a number less than {max_value+1}.")
                    continue
                elif min_value != '' and input_num < min_value:
                    print(f"Please enter a number greater than {min_value-1}.")
                    continue

            except ValueError:
                if decimals == 0:
                    print("Please enter a valid integer.")
                else:
                    print("Please enter a valid number.")
                continue
            else:
                return input_num

    def write_text(self, text, format_string=''):
        """Displays the given text on the terminal.

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)
