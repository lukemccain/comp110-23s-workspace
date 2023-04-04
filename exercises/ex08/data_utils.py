"""Wrangling Data."""

__author__ = "730486310"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table 
    first_row: dict[str, str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_vals(table, key)
    return result


def head(inp_d: dict[str, list[str]], num_of_rows: int) -> dict[str, list[str]]:
    """Return a column-based table with the first X rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in inp_d:
        list_values: list[str] = []
        idx: int = 0
        while idx < num_of_rows and idx < len(inp_d[column]):
            list_values.append(inp_d[column][idx])
            idx += 1
        result[column] = list_values
    return result


def select(inp_d: dict[str, list[str]], str_list: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only a subset of values from the original columns."""
    result: dict[str, list[str]] = {}
    for header in str_list:
        result[header] = inp_d[header]
    return result


def concat(inp_d1: dict[str, list[str]], inp_d2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column based table that combines two column based tables."""
    result: dict[str, list[str]] = {}
    for column in inp_d1:
        result[column] = inp_d1[column]
    for column in inp_d2:
        if column in result:
            result[column] += inp_d2[column]
        else:
            result[column] = inp_d2[column]
    return result


def count(inp_l: list[str]) -> dict[str, int]:
    """Produce a dictionary in which the keys are a string sequence and the values are the frequency those strings occur."""
    result: dict[str, int] = {}
    for item in inp_l:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result