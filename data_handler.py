"""
This file will be used to handle all the data
"""

from datetime import datetime
from typing import List, Dict
import csv
import ast


def read_csv(filepath: str) -> List[List[str]]:
    """Return a List rows of csv file, where every row
    is a list, with all variables in string format.

    @param filepath: the path of the csv file
    @return: List of rows in the csv file
    """

    with open(filepath) as file:
        reader = csv.reader(file)

        next(reader)  # skip the header row

        data = [row for row in reader]

        return data


def read_csv_and_transform(filepath: str, types: list, year_only: bool = False, day_only: bool = False) -> List[List[str]]:
    """Return a List rows of csv file, where every row
    is a list, with all variables in their respective datatype

    @param filepath: the path of the csv file
    @param types: list of datatype objects corresponding to each variable in list
    @return: List of rows in the csv file
    """

    with open(filepath) as file:
        reader = csv.reader(file)

        next(reader)  # skip the header row

        data = [convert_datatype(row, types, year_only, day_only) for row in reader]

        return data


def transform(dataset: List[List], types: list, year_only: bool = False, only_day: bool = False) -> List[List]:
    """Return a dataset with all the variables in their appropriate
    data type.

    :param year_only: if we just want the year from datetime object
    :param dataset: the dataset for which we want to apply this function
    :param types: list of datatype objects
    :return: dataset with variables having appropriate datatype
    """
    return [convert_datatype(row, types, year_only, only_day) for row in dataset]


def convert_to_datetime(dt: str) -> datetime:
    """Convert a string to datetime format and
    return datetime object

    Preconditions:
    - dt is in valid datetime format
    """

    return datetime.fromisoformat(dt)


def convert_datatype(values: list, types: list, only_year: bool = False, only_day: bool = False) -> list:
    """
    Returns a list with every element of the list converted
    into the appropriate datatype passed in the types.

    Appropriate types:
    - str
    - int
    - float
    - datetime
    - bool

    @param values: row of a dataset
    @param types: type to change each value in the row
    @param only_year: if we just want the year from datetime object
    @return: list with each value having appropriate dataset

    Preconditions:
    - len(values) == len(types)
    """

    list_so_far = []  # ACCUMULATOR: stores the new values

    for index in range(len(values)):
        if types[index] != datetime and types[index] != list:
            list_so_far.append(types[index](values[index]))

        elif types[index] == datetime:
            if only_year:
                list_so_far.append(convert_to_datetime(values[index]).year)
            elif only_day:
                list_so_far.append(convert_to_datetime(values[index]).day)
            else:
                list_so_far.append(convert_to_datetime(values[index]))
        elif types[index] == list:
            list_so_far.append(ast.literal_eval((values[index])))

    return list_so_far


def filter_by_value(dataset: List[List], column: int, values: list):
    """
    Return a filtered dataset, with rows in which column <column>
    has a value in <value> list

    @param dataset: the dataset we want to filter
    @param column: the column with which we want to filter
    @param values: the list of values with column could have
    @return: A filtered dataset
    """

    return [row for row in dataset if row[column] in values]


def filter_by_function(dataset: List[List], filter_function):
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

    return all(element is not None and element != '' for element in row)


def remove_na(dataset: List[List]) -> List[List]:
    """Return a dataset with all the None values removed

    @param dataset: the dataset we want to filter
    @return: A filtered dataset
    """
    return filter_by_function(dataset, __remove_na_for_row__)


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


def head(dataset: List[List], n=5) -> None:
    """Print the first <n> rows of a dataset"""

    for i in range(n):
        print(dataset[i])


def unique(dataset: List[List], column: int) -> set:
    """Return a list of unique values for the column <column> in dataset"""
    return {row[column] for row in dataset}


def group_by(dataset: List[List], column: int, filter_values=None) -> Dict[str, List[List]]:
    """Group the data by different values of the column <column> and return an list
    with lists of observations for a specific value of the column.

    @param dataset: the dataset we want to filter
    @param column: the column number to group by
    @param filter_values: set of values for column we want to keep
    @return: dict containing datasets with different values for the column
    """

    values_to_keep = unique(dataset, column)

    if filter_values:
        values_to_keep = values_to_keep.intersection(filter_values)

    dict_so_far = {value: [] for value in values_to_keep}

    for row in dataset:
        if row[column] in dict_so_far:
            dict_so_far[row[column]].append(row)

    return dict_so_far


def group_by_function(dataset: List[List], column: int, filter_function, filter_values=None) -> Dict[str, List[List]]:
    """Group the data by different values of the column <column> applied to the filter_function
    and return an list with lists of observations for a specific value of the column applied to
    the filter function.

    @param dataset: the dataset we want to filter
    @param column: the column number to group by
    @param filter_function: function to get values from column
    @param filter_values: set of values for column we want to keep
    @return: dict containing datasets with different values for the column
    """

    all_values = [row + [filter_function(row[column])] for row in dataset]

    values_to_keep = unique(all_values, len(dataset[0]))

    if filter_values:
        values_to_keep = values_to_keep.intersection(filter_values)

    dict_so_far = {value: [] for value in values_to_keep}

    for row in all_values:
        if row[len(dataset[0])] in dict_so_far:
            dict_so_far[row[len(dataset[0])]].append(row)

    return dict_so_far


def calc_avg_col(dataset: List[List], column: int) -> float:
    """Return the average for a column

    @param dataset: the dataset for which we want to compute average
    @param column: the column for which we want the average
    @return: average of the column <column>
    """
    return sum([row[column] for row in dataset]) / len(dataset)


def extract_column(dataset: List[List], column: int) -> list:
    """Return a column of a dataset"""
    return [row[column] for row in dataset]


def calculate_average(data: List[List], grouping_cloumn: int, avg_column: int, grouping_column_modifier=None) -> List[List]:
    """The function groups the data by column <grouping column> of the dataset and then calculate
    the average of column <avg_column> for every group and return the list of those averages and
    list of values for grouping column

    @param data: dataset for which we want to compute the average
    @param grouping_cloumn: column with which we would group
    @param avg_column: the column of which we want to compute average
    @param grouping_column_modifier: function to group by modified value of the grouping column
    @return: List containing the average of column <avg_column> for every group of column <grouping_column>
    """
    values = []
    group = []

    if grouping_column_modifier:
        data = group_by_function(data, grouping_cloumn, grouping_column_modifier)
    else:
        data = group_by(data, grouping_cloumn)

    for i in data:
        values.append(calc_avg_col(data[i], avg_column))
        group.append(data[i][0][grouping_cloumn])

    return [group, values]
