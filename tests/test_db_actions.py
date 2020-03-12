import db_actions

json_file_path = "tests/sources/reading_log.json"

def test_get_books():
    result = db_actions.get_books(json_file_path)
    book0 = {'ISBN': '9781401209971', 'author': 'Brian K. Vaughan', 'date': 'February 2020', 'id': '6cdd27a056c76e60743439a311a174f1', 'rating': 8.0, 'title': 'Ex Machina Vol 4'}
    assert type(result) == list
    assert len(result) == 2
    assert type(result[0]) == dict
    assert result[0] == book0

def test_sort_by_month():
    input_list = db_actions.get_books(json_file_path)
    result = db_actions.sort_by_month(input_list)
    assert type(result) == list
    assert len(result) == 2  # 2 different months
    assert type(result[0]) == list
    assert result[0] == [{'ISBN': '9781401209971', 'author': 'Brian K. Vaughan', 'date': 'February 2020', 'id': '6cdd27a056c76e60743439a311a174f1', 'rating': 8.0, 'title': 'Ex Machina Vol 4'}]

def test_write_books(tmpdir):
    input_list = db_actions.get_books(json_file_path)
    result = tmpdir.join('result.txt')
    db_actions.write_books(input_list, result)
    with open(json_file_path, 'r') as f:
        assert result.read() == f.read().rstrip()

def test_get_monthly_lists():
    result = db_actions.get_monthly_lists(json_file_path)
    assert type(result) == list
    assert type(result[0]) == list
    assert result == [[{'ISBN': '9781401209971', 'author': 'Brian K. Vaughan', 'date': 'February 2020', 'id': '6cdd27a056c76e60743439a311a174f1', 'rating': 8.0, 'title': 'Ex Machina Vol 4'}], [{'ISBN': 'B01FNAQ2ZS', 'author': 'Tom King', 'date': 'January 2020', 'id': 'ca2b906efb7277baa8b1d632ed965146', 'rating': 7.5, 'title': 'The Vision #10'}]]

def test_add_new_books(tmpdir):
    result = tmpdir.join('result.txt')
    input_list = db_actions.get_monthly_lists(json_file_path)
    db_actions.write_books(input_list, result)
    book = [{'title': 'La horde du contrevent', 'ISBN': '2070342263', 'author': 'Alain Damasio', 'date': 'July 1987', 'rating': 9.5}]
    db_actions.add_new_books(result, book)
    assert result.read() == '{"books": [{"title": "La horde du contrevent", "ISBN": "2070342263", "author": "Alain Damasio", "date": "July 1987", "rating": 9.5}, [{"title": "Ex Machina Vol 4", "author": "Brian K. Vaughan", "ISBN": "9781401209971", "rating": 8.0, "date": "February 2020", "id": "6cdd27a056c76e60743439a311a174f1"}], [{"title": "The Vision #10", "author": "Tom King", "ISBN": "B01FNAQ2ZS", "rating": 7.5, "date": "January 2020", "id": "ca2b906efb7277baa8b1d632ed965146"}]]}'

def test_add_tag():
    book = {'title': 'La horde du contrevent', 'ISBN': '2070342263', 'author': 'Alain Damasio', 'date': 'July 1987', 'rating': 9.5}
    new_tag = ('test', 123)
    result = db_actions.add_tag(book, new_tag)
    assert type(result) == dict
    assert result['test'] == 123
    assert result == {'title': 'La horde du contrevent', 'ISBN': '2070342263', 'author': 'Alain Damasio', 'date': 'July 1987', 'rating': 9.5, 'test': 123}
