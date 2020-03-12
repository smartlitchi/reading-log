import new_books
monthly_log_path = 'tests/sources/jul1987.txt'

def test_gen_unique_id():
    title = 'La Horde du Contrevent'
    ISBN = '2070342263'
    result = new_books.gen_unique_id(title, ISBN)
    assert type(result) == str
    assert result == 'a45bd062ca947a03f43306b00a408f4c'

def test_parse_new_books():
    books = new_books.parse_new_books(monthly_log_path)
    assert len(books) == 2
    assert type(books) == list
    assert type(books[0]) == dict
    book1 = {'ISBN': '2070342263', 'author': 'Alain Damasio', 'date': 'July 1987', 'rating': 9.5, 'title': 'La Horde du Contrevent', 'id': 'a45bd062ca947a03f43306b00a408f4c'}
    assert books[1] == book1
