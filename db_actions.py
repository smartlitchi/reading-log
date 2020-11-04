from pathlib import Path
import os
import json
from dateutil.parser import parse

def init_log(assets_folder, json_file):
    """
    Create the necessary folders and files before first time use

    assets_folder -- str, path to the assets
    json_file -- str, path of the database
    """
    covers = assets_folder + 'covers'
    reports = assets_folder + 'monthly_reports'
    try:
        Path(covers).mkdir(parents=True)
    except FileExistsError:
        print('covers folder already exists')
    try:
        Path(reports).mkdir(parents=True)
    except FileExistsError:
        print('monthly reports folder already exists')

    if not os.path.exists(json_file):
        database = open(json_file, 'w')
        database.close()
        print('database initiated')
    else:
        print('database already exists')

    print('Reading log ready to be used')

def get_books(json_file):
    """
    Reads the json database

    json_file -- str, the path of the database
    """
    with open(json_file, "r") as read_file:
        log = json.load(read_file)
    return log["books"]

def sort_by_month(books_list):
    """
    Returns a list OF LISTS of books. The sorting is in reverse chronological order

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

def write_books(books, json_file):
    """
    Write log file to json database

    books -- list of books
    json_file -- str, path to the json dbase
    """
    with open(json_file, 'w') as write_file:
        log = dict()
        log['books'] = books
        json.dump(log, write_file)

def get_monthly_lists(json_file):
    """
    Returns a list of lists of books

    json_file -- string of json database's path
    """
    books = get_books(json_file)
    books_sorted = sort_by_month(books)
    return books_sorted

def add_new_books(json_file, new_books):
    """
    Write the new books into the json database
    Doesn't return anything

    json_file -- a string, path of json database
    new_books -- a list, new books to be added
    """
    old_books = get_books(json_file)
    new_db = new_books + old_books
    write_books(new_db, json_file)
    print('new books added to database')

def add_tag(book, new_tag):
    """
    Adds a new tag to a book in json database and returns a copy of the book

    book -- dictionary containing all the infos of a single book
    new_tag -- tuple, (tag key, tag value) to be added
    """
    modified_book = book
    tag_key, tag_value = new_tag
    modified_book[tag_key] = tag_value
    return modified_book
