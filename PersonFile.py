import random
from typing import Tuple


class Person:

    def __init__(self):
        self.private_key = 0
        self.base = 1
        self.clock_size = 1
        self.shared_secret = 0
        self.friends_ppn = 2
        self.name = ""

    def request_name(self):
        self.name = input("Creating a new person: Hello, what is your name?")
        print(f"Welcome, {self.name}")

    def pick_clock_and_base(self) -> Tuple[int, int]:
        while True:  # pick the clock.
            clock_string = input(f"{self.name}, please select an clock size: ")
            try:
                self.clock_size = int(clock_string)
            except ValueError:
                print("That wasn't an integer.")
                continue
            if self.clock_size > 0:
                break
            print("Please try again with a positive integer.")

        while True:  # pick the base.
            base_string = input(f"{self.name}, now please select a base: ")
            try:
                self.base = int(base_string)
            except ValueError:
                print("That wasn't an integer.")
                continue
            if self.base > 0:
                break
            print("Please try again with a positive integer.")

        return self.clock_size, self.base

    def receive_clock_and_base(self, clock: int, base: int):
        self.clock_size = clock
        self.base = base

    def select_private_key_and_generate_ppn(self) -> int:
        """
        chooses a private key and generates a public-private-number, as per the book.
        (See page 55)
        :return: A public-private-number to share.
        """
        self.private_key = random.randrange(1, self.clock_size+1)
        ppn = 3  # TODO -replace this with a proper calculation.
        return ppn

    def receive_friend_ppn(self, ppn: int):
        self.friends_ppn = ppn

    def calculate_shared_secret(self):
        """
        Based on self.base, self.clock_size, self.friends_ppn, and self.private_key, calculate the shared secret and
        put it into self.shared_secret.
        :return: None
        """
        self.shared_secret = 1  # TODO: calculate your shared secret.

    def encode_message(self) -> str:
        """
        Requests a string from the user and uses the shared secret number to encrypt it into a new string.
        :return: an encrypted string.
        """
        message = input(f"{self.name}, please enter a message to encode, about 20 - 30 characters, including three "
                        f"4-letter words. ")
        key = self.shared_secret
        encoded = message  # TODO - replace this with a proper encoding that uses the key.
        # possibly helpful: num = ord(message[5]) will convert the fifth character to its ASCII/Unicode number and put
        # it in "num" variable
        #                   str = chr(65) will convert the number 64 to its ASCII character ("A").
        return encoded

    def decode_message(self, encoded: str, key: int = None) -> str:
        """
        converts the given string into a (hopefully) decoded string by reversing the method encode_message.
        If key is not explicitly set, will use the self.shared_secret as the key.

        :param encoded: string to decode
        :param key: a numerical key, or None -- if self.shared_secret is desired as key.
        :return: a decoded version of the given encoded string.
        """
        if key is None:
            key = self.shared_secret
        decoded = encoded  # TODO - replace this with a proper decoding that uses the key.
        # possibly helpful: num = ord(message[5]) will convert the fifth character to its ASCII/Unicode number and put
        # it in "num" variable
        #                   str = chr(65) will convert the number 64 to its ASCII character ("A").

        return decoded
