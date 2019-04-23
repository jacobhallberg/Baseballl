from flask import Flask, render_template, flash, request, abort, redirect, url_for
from wtforms import Form, StringField,validators
from flask_wtf import FlaskForm

import sqlite3, csv
import pandas as pd

app = Flask(__name__)
app.secret_key = 'super secret key'

FILE_PATH = "./webApp/2014-2018_specialty_score.csv"
TABLE_NAME = "player_data"

SQL = sqlite3.connect(":memory:")

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


DF = pd.read_csv(FILE_PATH, index_col=0)
DF.to_sql(TABLE_NAME, SQL, if_exists="append", index=False)
SQL.row_factory = make_dicts

def query_db(db, query, args=()):
    return db.execute(query, args)

class SearchForm(FlaskForm):
    player_name = StringField("Firstname Lastname", [validators.Length(min=3, max=25), validators.DataRequired()])

@app.route("/", methods=["GET", "POST"])
def search():
    form  = SearchForm()

    if form.validate_on_submit():
        name = form.player_name.data.split(" ")
        if len(name) >= 2:
            lastname, firstname = name[0], name[1]
        else:
            lastname, firstname = name[0], " "
            
        query_result = list(query_db(SQL, "SELECT * FROM player_data WHERE name_last = '{}' AND name_first = '{}';".format(lastname, firstname)))
        
        if len(query_result) == 0:
            query_result = list(query_db(SQL, "SELECT * FROM player_data WHERE name_last = '{}';".format(lastname)))

        if len(query_result) == 0:
            return render_template("search.html", form=form, no_player = lastname)

        return render_template("search.html", form=form, player_data = query_result)

    return render_template("search.html", form=form)

if __name__ == '__main__':
    app.run(debug=False)
