# Reading-Log

Reading-Log is a small script to record your own reading. It generates a log in HTML format that you can put on your website. The log is highly inspired by [Good OK Bad](http://goodokbad.com/log.html)

## Requirements

* python 3.8
* pipenv

## Installation

First, clone the repository : 

```sh
git clone git@github.com:zimhat/reading-log.git
```

Then install required packages via ``pipenv``.

```sh
pipenv install
```

## Configuration

In the folder ``assets`` create two folders, ``covers`` and ``monthly_reports``. Your repository tree should look like this.

```sh
.
├── assets
│   ├── covers
│   ├── monthly_reports
│   └── reading_log.json
├── db_actions.py
├── new_books.py
├── Pipfile
├── Pipfile.lock
├── reading_log.py
├── render
├── templates
├── tests
└── web_render.py
```

## Usage

### Record a book

To record a book, add it to your monthly log. It's a basic text file. Its name must follow this convention  for the script to pick it 

```
<3-letters-month><year>.txt
```

For example, ``oct2020.txt`` is a valid name. It also has to be in ``assets/monthly_reports``.

Each entry must be separated by an empty line and be of the form :

```
Title
Author
ISBN
Rating out of 10
```

The cover must be saved in ``assets/covers`` and its name must be ``<ISBN>.jpg``

### Update the database and generate the full html log

Once a month, open ``reading_log.py`` and change this line :

```py
monthly_log = 'assets/monthly_reports/<your record>'
```

Then, comment out the line ``#db_actions.add_new_books(json_file, books_of_the_month)``.

Finally, execute the script with :

```sh
pipenv run python reading_log.py
```
