"""
The following code is used to encrypt and decrypt stuff.

Author: Shravan Asati
Originally Written: 1 July 2021
Last Edited: 1 July 2021
"""

import os
import cryptocode
import random
import pickle
import string
import json


class Configuration:
    """
    Base class for setting up chrono configuration.
    """

    def __init__(self) -> None:
        """
        Constructs the `Configuration` class. Creates key if it doesnt exists and reads the key and password.
        """
        # * making a chrono datadir if not exists
        self.datadir = os.path.join(os.path.expanduser("~"), ".chrono", "data")
        if not os.path.exists(self.datadir):
            os.makedirs(self.datadir)

        self.__key = self.__get_encryption_key()
        self.__user_data = self.__get_user_data()

    def __get_encryption_key(self) -> str:
        # * creating key if not exists and reading it
        key_file = os.path.join(self.datadir, "key.pkl")

        if not os.path.exists(key_file):
            # * creating key if not exists randomly of length of 100 chars
            key = ''.join([random.choice(random.choice(
                [string.ascii_letters, string.digits, string.punctuation])) for _ in range(100)])
            with open(key_file, 'wb') as kf:
                pickle.dump(key, kf)

        else:
            with open(key_file, 'rb') as kf:
                key = pickle.load(kf)

        return key

    def __get_user_data(self) -> dict:
        self.data_file = os.path.join(self.datadir, "user.dat")

        if not os.path.exists(self.data_file):
            with open(self.data_file, 'wb') as df:
                self.__user_data = json.dumps(({"api-key": ""}))
                pickle.dump(cryptocode.encrypt(
                    self.__user_data, self.__key), df)

            self.__user_data = json.loads(self.__user_data)

        else:
            with open(self.data_file, 'rb') as df:
                self.__user_data = json.loads(
                    cryptocode.decrypt(pickle.load(df), self.__key))

        return self.__user_data

    def set_api_key(self, key: str) -> None:
        """
        Sets the API key.
        """
        self.__user_data["api-key"] = key
        with open(self.data_file, 'wb') as df:
            pickle.dump(cryptocode.encrypt(
                json.dumps(self.__user_data), self.__key), df)

    def get_api_key(self) -> str:
        """
        Returns the API key.
        """
        return self.__user_data["api-key"]


if __name__ == "__main__":
    c = Configuration()
    c.set_api_key("super secret")
    print(c.get_api_key())
