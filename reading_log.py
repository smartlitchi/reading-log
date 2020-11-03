import new_books
import db_actions
import web_render
import sys

if __name__ == "__main__":
    json_file = 'assets/reading_log.json'
    template_path = 'templates/monthly_log.html'
    webpage_path = 'render/index.html'
    if len(sys.argv) == 2:
        books_of_the_month = new_books.parse_new_books(sys.argv[-1])
        db_actions.add_new_books(json_file, books_of_the_month)
    books_parsed = db_actions.get_monthly_lists(json_file)
    web_render.render_html(books_parsed, template_path, webpage_path)
    web_render.copy_covers('assets/covers', 'render/covers')
