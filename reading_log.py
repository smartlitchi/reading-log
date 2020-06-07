import new_books
import db_actions
import web_render

if __name__ == "__main__":
    monthly_log = 'assets/monthly_reports/may2020.txt'
    json_file = 'assets/reading_log.json'
    template_path = 'templates/monthly_log.html'
    webpage_path = 'render/reading_log.html'
    books_of_the_month = new_books.parse_new_books(monthly_log)
    #db_actions.add_new_books(json_file, books_of_the_month)
    books_parsed = db_actions.get_monthly_lists(json_file)
    web_render.render_html(books_parsed, template_path, webpage_path)
