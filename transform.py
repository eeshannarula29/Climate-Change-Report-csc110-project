"""
File related to - CO2 emissions (kg per PPP $ of GDP) dataset.
Data set taken from - data.workbank.org website.
Data set name - C02emissionsPPP.csv

Objectives -
    -In this file we would be doing a series of computations to convert the data
     in CO2PPP.csv file into appropriate data types.
    -We would be performing a series of computations to restructure the data in .......
    -We would be performing various <> to clean up the data and discard irrelevant data.

Add doctest
Run python_ta
Add return types to function headers
"""

from typing import List
import csv


def read_convert_csv_file(filename: str) -> List[list]:
    """
    Read all the data from csv file and convert it into the required format.

    When converting the data, discard the irrelevant/blank (N/A) fields in the data file.

    An N/A value is that value, which is the data relating to years less than 1990 and
    greater than 2016.

    Also ignore any irrelevant information while generating the new list.

    Irrelevant information is - Country Code, Indicator name, Indicator Code

    Use functions:-
    convert_row  and convert_header to achieve this.
    """

    # ACCUMULATOR: to make a new list of lists with appropriate header and related data.
    aggregate = []

    with open(filename) as file:
        reader = csv.reader(file)

        header = next(reader)

        for row in reader:
            aggregate.append(convert_row(row, header))

        aggregate.insert(0, convert_header(header))

    return aggregate


def convert_row(row: List[str], header: List[str]) -> list:
    """Convert a row of CO2emissionsPPP data to a list with the appropriate data types.
    Discarding all N/A values when transforming data into new list.

    An N/A value is that value, which is the data relating to years less than 1990 and
    greater than 2016.
    A non-N/A year is a year which comes between 1990 and 2016 (inclusive).

    Also ignore any irrelevant information while generating the new list.

    Irrelevant information is - Country Code, Indicator name, Indicator Code
    """

    # ACCUMULATOR: To store the new data which is being converted
    new_lst = []

    for i in range(0, len(row)-1):
        if i == 0:
            new_lst.append(row[i])  # Country name
        elif i == 1:
            continue  # Ignoring Country Code
        elif i == 2:
            continue  # Ignoring Indicator name - CO2 emissions (kg per PPP $ of GDP)
        elif i == 3:
            continue  # Ignoring Indicator Code
        else:  # Data of every non-N/A year
            if 1990 <= int(header[i]) <= 2016:
                new_lst.append(row[i])

    return new_lst


def convert_header(row: List[str]) -> list:
    """Converting the header data to a list with the appropriate data types.
    Discarding all N/A values when transforming data into new list.

    An N/A value is that value, which is the data relating to years less than 1990 and
    greater than 2016.
    A non-N/A year is a year which comes between 1990 and 2016 (inclusive).

    Also ignore any irrelevant information while generating the new list.

    Irrelevant information is - Country Code, Indicator name, Indicator Code
    """

    # ACCUMULATOR: To store the new data which is being converted
    new_lst = []

    for i in range(0, len(row) - 1):
        if i == 0:
            new_lst.append(row[i])  # Country name
        elif i == 1:
            continue  # Ignoring Country Code
        elif i == 2:
            continue  # Ignoring Indicator name - CO2 emissions (kg per PPP $ of GDP)
        elif i == 3:
            continue  # Ignoring Indicator Code
        else:  # the data of every non-N/A year
            if 1990 <= int(row[i]) <= 2016:
                new_lst.append(row[i])

    return new_lst


def cleanup(lst: List[list]) -> List[list]:
    """
    Return a list of cleaned up data.

    Cleaned up data refers to those rows (lists) in lst which do not contain a single
    '' value.
    """

    # ACCUMULATOR: Store the new cleaned up list so far
    new_lst = []

    for x in lst:
        c = 0
        for i in x:
            if i == '':
                c = c + 1

        if c >= 1:
            continue
        else:
            new_lst.append(x)

    return new_lst


