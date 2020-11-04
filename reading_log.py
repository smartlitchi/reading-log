import new_books
import db_actions
import web_render
import sys

if __name__ == "__main__":
    assets_folder = 'assets/'
    json_file = 'assets/reading_log.json'
    template_path = 'templates/monthly_log.html'
    webpage_path = 'render/index.html'
    if len(sys.argv) == 2:
        if sys.argv[-1] == '--init':
            db_actions.init_log(assets_folder, json_file)
        else:
            books_of_the_month = new_books.parse_new_books(sys.argv[-1])
            db_actions.add_new_books(json_file, books_of_the_month)
    try:
        books_parsed = db_actions.get_monthly_lists(json_file)
        web_render.render_html(books_parsed, template_path, webpage_path)
        web_render.copy_covers('assets/covers', 'render/covers')
    except IndexError:
        print('Database empty, nothing to render')
