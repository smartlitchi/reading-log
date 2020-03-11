import json
import jinja2
from dateutil.parser import parse

def parse_new_books(monthly_log):
    fields = ["title", "author", "ISBN", "rating", "date"]
    new_book = list()
    new_books = list()
    file_name = monthly_log.split('/')[-1]
    monthly_date = parse(file_name.split('.')[0])
    monthly_date = monthly_date.strftime('%B %Y')
    counting_lines = 0
    with open(monthly_log, 'r') as log:
        log_lines = log.readlines()
        log_lines.append('')  # adding a last line to avoid skipping last entry
        for index, line in enumerate(log_lines):
            if counting_lines < 4:
                new_book.append(line.rstrip())
                counting_lines += 1
            else:
                new_book[-1] = float(new_book[-1])  # convert ratings into float
                new_book.append(monthly_date)
                new_books.append(dict(zip(fields, new_book)))
                new_book = []
                counting_lines = 0
    return new_books[::-1]

def add_monthly_books(json_file, monthly_log):
    with open(json_file, "r") as read_file:
        log = json.load(read_file)
    new_log = monthly_log + log['books']
    log['books'] = new_log
    with open(json_file, 'w') as write_file:
        json.dump(log, write_file)

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
    monthly_log = 'assets/monthly_reports/mar2020.txt'
    json_file = 'assets/reading_log.json'
    books_of_the_month = parse_new_books(monthly_log)
    books_parsed = parse_json(json_file)
    add_monthly_books(json_file, books_of_the_month)
    books_parsed = parse_json("assets/reading_log.json")
    render_html(books_parsed)
