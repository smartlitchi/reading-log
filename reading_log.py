import json
import jinja2
from dateutil.parser import parse

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

books_parsed = parse_json("assets/reading_log.json")

with open('render/reading_log.html', 'w') as webpage:
    webpage.write(generate_html(books_parsed))
