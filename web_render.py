import jinja2

def generate_html(books_list):
    """
    Takes a list of books and generate the html template

    books_list -- list of all the books I need to render
    """
    file_loader = jinja2.FileSystemLoader('templates')
    env = jinja2.Environment(loader=file_loader)
    template = env.get_template('monthly_log.html')
    return(template.render(months=books_list))

def render_html(books):
    """
    Writes the template to a webpage

    books -- list of all the books I need to render
    """
    with open('render/reading_log.html', 'w') as webpage:
        webpage.write(generate_html(books))
        print("webpage successfully rendered")
