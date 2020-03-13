import web_render
template_path = 'templates/monthly_log.html'
render_witness = 'tests/sources/reading_log.html'
books = [[{'ISBN': '9781401209971', 'author': 'Brian K. Vaughan', 'date': 'February 2020', 'id': '6cdd27a056c76e60743439a311a174f1', 'rating': 8.0, 'title': 'Ex Machina Vol 4'}], [{'ISBN': 'B01FNAQ2ZS', 'author': 'Tom King', 'date': 'January 2020', 'id': 'ca2b906efb7277baa8b1d632ed965146', 'rating': 7.5, 'title': 'The Vision #10'}]]

def test_generate_html():
    result = web_render.generate_html(books, template_path)
    assert type(result) == str
    with open(render_witness, 'r') as witness:
        assert result == witness.read()

def test_render_html(tmpdir):
    result = tmpdir.join('result.html')
    web_render.render_html(books, template_path, result)
    with open(render_witness, 'r') as witness:
        assert result.read() == witness.read()
