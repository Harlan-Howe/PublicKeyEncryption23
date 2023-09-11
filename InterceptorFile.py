from typing import List
from PersonFile import Person


class Interceptor (Person):
    def __init__(self):
        super().__init__()
        print("**** Creating Interceptor....")
        self.base = 1
        self.clock_size = 1
        self.ppns: List[int] = []
        self.possible_shared_secrets: List[int] = []
        self.word_list: List[str] = []
        self.load_words_from_file("Four letter words.txt")

    def load_words_from_file(self, word_filename: str):
        """
        loads the self.word_list with all the words in the given file.
        :param word_filename: the file to read in a format "word# <tab> word"
        :return: None
        """
        print(f"**** Loading Words from {word_filename}.")
        count = 0
        with open(word_filename, 'r') as ins:
            for line in ins:
                pairs = line.split("\t")  # make a 2-item list with the part before the tab and the part after the tab.
                # if count % 100 == 0:  # show progress....
                #     print(f"Loaded {count} words....")

                count += 1
                self.word_list.append(pairs[1].split("\n")[0])  # The split{"\n") part gets rid of the carriage return.
        print(f"**** Done Loading {len(self.word_list)} words from file {word_filename}.")
        print("-------------------------------------------")

    def intercept_clock_and_base(self, clock: int, base: int):
        """
        copy the intercepted values and acknowledge that you have done so.
        :param clock: the clock_size value to grab
        :param base: the base value to grab
        :return: None
        """
        self.base = base
        self.clock_size = clock
        print(f"**** Interceptor just picked up clock_size {self.clock_size} and base = {self.base}.")

    def intercept_ppn(self, ppn: int):
        """
        adds the given ppn to our list of intercepted ppns. And acknowledge that we have intercepted it.
        (Honestly, I don't think we'll be able to use this ((except maybe to confirm suspected keys)), but we're
        acknowledging that we have seen it.)
        :param ppn: the ppn we intercept
        :return: None
        """
        self.ppns.append(ppn)
        print(f"**** Interceptor just picked up a ppn = {ppn}.")

    def hack_message(self, scrambled: str):
        """
        loops through possible keys, decoding the given scrambled message, looking
        for decoded messages for three or more four-letter words.

        If self.possible_shared_secrets has length zero at the start of the method, tries all the shared secrets from 0
        to clock_size - 1 as keys. If it finds a potential plaintext message with three or more words, prints the
        candidate decoded message and adds the key to the self.possible_shared_secrets list.

        Otherwise, (if there are already possible shared secrets at the start) just uses values in
        self.possible_shared_secrets as keys, prints out any candidate decoded plaintext messages, and removes any
        shared_secrets that didn't work. (Ideally, there will be one that still works!)

        :param scrambled: a string to decode.
        :return:
        """
        print(f"**** Interceptor attempting to decode scrambled message: {scrambled}")
        # -----------------------------------------
        # TODO - you write this!
        #   1) Loop through possible keys (see note above)
        #        2) Call decode(encoded = scrambled, key = possible_key) convert string to a new string.
        #        3) Count the number of four-letter words in decoded string. (See method below.)
        #        4) If there were three or more four-letter words, add this possible_key to the
        #           list of possible shared secrets, and print out the decoded string.
        #  5) If there is only one item in the list of possible_shared_secrets, declare victory!
        # -----------------------------------------

    def count_four_letter_words_in_string(self, sentence: str) -> int:
        """
        loops through the string, selecting four-character sequences and counts how many are contained in
        self.word_list.
        :param sentence: the string in which to search for words
        :return: the count of matching four-letter words.
        """

        return -1  # TODO: write this method!
