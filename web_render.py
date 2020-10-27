import jinja2
import os
import shutil

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

def copy_covers(covers_fd_path, web_covers_fd_path):
    """
    Copy the covers to the web folder

    covers_fd_path -- str, path of the folder where covers are saved
    web_covers_fd_path -- str, path of the web folder where covers will be stored
    """
    new_covers = set(os.listdir(covers_fd_path)) - set(os.listdir(web_covers_fd_path))
    for cover in new_covers:
        shutil.copy2(covers_fd_path + '/' + cover, web_covers_fd_path + '/' + cover)
    print("covers transfered")
