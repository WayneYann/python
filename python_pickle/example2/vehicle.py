"""
File that contains Vehicle class.
"""

import pickle


class Vehicle:
    """
    Vehicle class
    """

    def __init__(self, name, year):
        self.name = name
        self.year = year

    @classmethod
    def load(cls, pfile):
        """
        Load attributes from pickle file
        pfile is a string representing path to pickle file
        """
        vh = pickle.load(open(pfile, 'rb'))
        return cls(vh.name, vh.year)


