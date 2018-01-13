# Data Loader, November 5, 2017
# Tony DiPadova, January 12, 2018
# This example code is used to load training or testing data sets into numpy arrays

import numpy
from urllib.request import urlopen


def load_csv(filename, delimiter):
    """
    This code loads data from a CSV to a `numpy` array
    :param filename: the path to the data
    :type filename: str
    :param delimiter: delimits the data (like "," or "|")
    :type delimiter: char
    """
    try:
        file = open(filename, 'r')  # open the file
    except IOError:
        print("Unable to open the file \"" + str(filename) + "\"")  # catch error
        return None  # return None to indicate error

    data = numpy.loadtxt(file, delimiter=delimiter)  # load the file into a numpy array
    return data  # return the numpy array


def load_from_web(url, delimiter):
    """
    This code loads data from the web to a `numpy` array
    :param url: the path to the data
    :type url: str
    :param delimiter: delimits the data (like "," or "|")
    :type delimiter: char
    """
    try:
        file = urlopen(url)  # get the file from the web
    except IOError:
        print("Unable to open the url \"" + str(url) + "\"")  # catch error
        return None  # return None to indicate error

    data = numpy.loadtxt(file, delimiter=delimiter)  # load the file into a numpy array
    return data  # return the data
