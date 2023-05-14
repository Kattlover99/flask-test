# Flask Test

## Installation

Install a dedicated virtual environment for each Flask project
```bash
python -m venv myworld
```
Then you have to activate the environment, by typing this command:
```bash
myworld\Scripts\activate.bat
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask.

```bash
pip install flask
```

## Run

You can run using the following command

```bash
flask --app app run
```

## Directory Layout
Often it is beneficial to include some reference data into the project, such as
Rich Text Format (RTF) documentation, which is usually stored into the `docs`
or, less commonly, into the `doc` folder.

    .
    ├── ...
    ├── .gitignore
    ├── app.py
    │   ├── /get_movies_dump     # Execute get_data_from_wiki.py
    │   ├── /create_movie_table  # Create 'movies' table in Sqlite 
    │   ├── /movies              # Load movies.html
    ├── database.sqlite          # Sqlite DB file
    ├── get_data_from_wiki.py    # Get and store data from wikidata to Sqlite
    ├── LICENSE
    ├── README.md                
    ├── requirements.tx          # Package dependency
    ├── templates                # Templates directory
    │   ├── movies.html          # Page to display data from Sqlite
    └── ...