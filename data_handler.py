"""
This file will be used to handle all the data
"""

from datetime import datetime
from typing import List
import csv


def read_csv(filepath: str, types: list) -> List[List[str], List[List[str]]]:
    """Return a List rows of csv file, where every row
    is a list, with all variables in string format.

    @param filepath: the path of the csv file
    @param types: list of datatype objects corresponding to each variable in list
    @return: List of rows in the csv file
    """

    with open(filepath) as file:
        reader = csv.reader(file)

        header = next(reader)  # the header row

        data = [convert_datatype(row, types) for row in reader]

        return [header, data]


def convert_to_datetime(dt: str) -> datetime:
    """Convert a string to datetime format and
    return datetime object

    Preconditions:
    - dt is in valid datetime format
    """

    return datetime.fromisoformat(dt)


def convert_datatype(values: list, types: list) -> list:
    """
    Returns a list with every element of the list converted
    into the appropriate datatype passed in the types.

    Appropriate types:
    - string
    - integer
    - float
    - datetime
    - bool

    @param values: row of a dataset
    @param types: type to change each value in the row
    @return: list with each value having appropriate dataset

    Preconditions:
    - len(values) == len(types)
    """

    list_so_far = []  # ACCUMULATOR: stores the new values

    for index in range(len(values)):
        if types[index] != datetime:
            list_so_far.append(types[index](values[index]))

        else:
            list_so_far.append(convert_to_datetime(values[index]))

    return list_so_far


def filter_dataset_by_feature(dataset: List[List], column: int, filter_function):
    """
    Return a filtered dataset, with rows in which column <column>
    satisfies the predicate function filter_function

    @param dataset: the dataset we want to filter
    @param column: the column with which we want to filter
    @param filter_function: the predicate function used for filtering
    @return: A filtered dataset
    """

    return [row for row in dataset if filter_function(row[column])]


def filter_dataset(dataset: List[List], filter_function):
    """
    Return a filtered dataset, with rows that satisfies the
    predicate function filter_function

    @param dataset: the dataset we want to filter
    @param filter_function: the predicate function used for filtering
    @return: A filtered dataset
    """

    return [row for row in dataset if filter_function(row)]


def __remove_na_for_row__(row: list) -> bool:
    """Return whether any of the values in the list
    is an empty string or None"""

    return any(element is None or element == '' for element in row)


def remove_na(dataset: List[List]) -> List[List]:
    """Return a dataset with all the None values removed

    @param dataset: the dataset we want to filter
    @return: A filtered dataset
    """
    return filter_dataset(dataset, __remove_na_for_row__)


def select(dataset: List[List], selected_columns: List[int]) -> List[List]:
    """Return a dataset with only the columns in the <selected_columns> list

    @param dataset: the dataset we want to filter
    @param selected_columns: the columns we want to keep
    @return: A filtered dataset
    """

    return [[row[column] for column in selected_columns] for row in dataset]


def delete(dataset: List[List], selected_columns: List[int]) -> List[List]:
    """Return a dataset with all the columns in <selected_columns> removed

    @param dataset: the dataset we want to filter
    @param selected_columns: the columns we want to delete
    @return: A filtered dataset
    """

    return [[row[column] for column in range(len(row)) if column not in selected_columns] for row in dataset]