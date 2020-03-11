import json
from dateutil.parser import parse

def get_books(json_file):
    """
    Reads the json database

    json_file -- str, the path of the database
    """
    with open(json_file, "r") as read_file:
        log = json.load(read_file)
    return log["books"]

def sort_by_date(books_list):
    """
    Returns a sorted list of books. The sorting is in reverse chronological order

    books_list -- a list of books
    """
    epoch = parse(books_list[0]["date"])
    monthly_books = list()
    reading_list = list()
    for book in books_list:
        if parse(book["date"]) == epoch:
            monthly_books.append(book)
        else:
            epoch = parse(book["date"])
            reading_list.append(monthly_books)
            monthly_books = [book]
    reading_list.append(monthly_books)
    return reading_list

def parse_json(json_file):
    """
    Returns the list of all books

    json_file -- string of json database's path
    """
    books = get_books(json_file)
    books_sorted = sort_by_date(books)
    return books_sorted
