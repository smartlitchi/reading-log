# Reading-Log

Reading-Log is a small script to record your own reading. It generates a log in HTML format that you can put on your website. The log is highly inspired by [Good OK Bad](http://goodokbad.com/log.html)

You can see an example [here](http://zimhat.info/reading-log)

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

You need to initialize the different folders. Just type this command.

```sh
pipenv run python reading_log.py --init
```

Your repository tree should then look like this.

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

Once a month, execute the script with :

```sh
pipenv run python reading_log.py <path_to_monthly_record>
```

For September 2020 for example, the command would be :

```sh
pipenv run python reading_log.py assets/monthly_reports/sep2020.txt
```

## Testing

This program use [pytest](https://docs.pytest.org/en/stable/).

```sh
pipenv run pytest -v
```
