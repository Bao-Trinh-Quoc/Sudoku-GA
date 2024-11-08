"""
Generic helper functions

Created on: 08/11/2024
"""

import datetime

def get_readable_time(start_time, end_time):
    """
    Returns a string in the form [D day[s], ][H]H:MM:SS[.UUUUUU].
    :param start_time: (float) the beginning of the task
    :param end_time: (float) the end of the task
    :return: (string) human readable string with hours, minutes and seconds
    """
    return str(datetime.timedelta(seconds=(end_time - start_time)))

def count_duplicates(iterable):
    """
    Count the number of duplicates in an iterable ( array )
    :param iterable: (iterable) the iterable to check
    :return: (int) the number of duplicates
    """
    # #of duplicates = #of elements - #of unique elements
    return len(iterable) - len(set(iterable))