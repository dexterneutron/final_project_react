import sqlalchemy as db
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/articles", methods = ['GET'])
def retrive_data():
    data = get_articles()
    return jsonify(data)

def get_articles():
    engine = db.create_engine('sqlite:///articles.sqlite')
    connection = engine.connect()
    metadata = db.MetaData()
    articles = db.Table('articles', metadata, autoload=True, autoload_with=engine)
    query = db.select([articles])
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    result_dicts = [{key: value for (key, value) in row.items()} for row in result_set]
    return result_dicts

if __name__ == '__main__':
    app.run()