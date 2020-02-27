import requests
from bs4 import BeautifulSoup
import re
import json
import jinja2
from dateutil.parser import parse

def parse_new_books(monthly_log):
    fields = ["title", "author", "rating"]
    new_book = list()
    new_books = list()
    counting_lines = 0
    with open(monthly_log, 'r') as log:
        for index, line in enumerate(log.readlines()):
            if counting_lines < 3:
                new_book.append(line.rstrip())
                counting_lines += 1
            else:
                new_book[-1] = float(new_book[-1])  # convert ratings into float
                new_books.append(dict(zip(fields, new_book)))
                new_book = []
                counting_lines = 0
    return new_books

def get_isbn(book_dict):
    search = book_dict['title'] + ' ' + book_dict['author']
    url = "https://isbnsearch.org/search"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}
    params = {'s': search.replace(' ', '+')}
    response = requests.get(url, params, headers=headers)
    parsed_response = BeautifulSoup(response.text, features="html.parser")
    book_info = parsed_response.find(class_='bookinfo')
    book_isbn = book_info.find(string=re.compile('ISBN-13'))
    return book_isbn.split()[-1]

def get_books(json_file):
    with open(json_file, "r") as read_file:
        log = json.load(read_file)
    return log["books"]

def generate_html(books_list):
    file_loader = jinja2.FileSystemLoader('templates')
    env = jinja2.Environment(loader=file_loader)
    template = env.get_template('monthly_log.html')
    return(template.render(months=books_list))

def sort_by_date(books_list):
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
    books = get_books(json_file)
    books_sorted = sort_by_date(books)
    return books_sorted

def render_html(books):
    with open('render/reading_log.html', 'w') as webpage:
        webpage.write(generate_html(books))
        print("webpage successfully rendered")

if __name__ == "__main__":
    books_of_the_month = parse_new_books('assets/monthly_reports/jan2020.txt')
    for book in books_of_the_month:
        print(get_isbn(book))
    #books_parsed = parse_json("assets/reading_log.json")
    #render_html(books_parsed)
