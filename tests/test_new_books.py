import new_books
monthly_log_path = 'tests/sources/jul1987.txt'

def test_parse_new_books():
    books = new_books.parse_new_books(monthly_log_path)
    assert len(books) == 2
    assert type(books) == list
    assert type(books[0]) == dict
    book1 = {'ISBN': '2070342263', 'author': 'Alain Damasio', 'date': 'July 1987', 'rating': 9.5, 'title': 'La Horde du Contrevent'}
    assert books[1] == book1
