import jinja2

def generate_html(books_list, template_path):
    """
    Takes a list of books and generate the html template as a string

    books_list -- list of lists of all the books I need to render, sorted by month
    template_path -- str, path of the template to be used
    """
    template_folder, template_file = template_path.split('/')
    file_loader = jinja2.FileSystemLoader(template_folder)
    env = jinja2.Environment(loader=file_loader)
    template = env.get_template(template_file)
    return(template.render(months=books_list))

def render_html(books, template_path, webpage_path):
    """
    Writes the template to a webpage

    books -- list of all the books I need to render
    template_path -- str, path of the template to be used
    webpage_path -- str, path for the output
    """
    with open(webpage_path, 'w') as webpage:
        webpage.write(generate_html(books, template_path))
        print("webpage successfully rendered")
