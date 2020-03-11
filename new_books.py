from dateutil.parser import parse

def parse_new_books(monthly_log):
    """
    Reads a txt and returns a list of books

    monthly_log -- a string indicating the path of new books report
    """
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
