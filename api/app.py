import sqlalchemy as db
from flask import Flask, jsonify
from flask_cors import CORS
from flask_apscheduler import APScheduler
from etl import run_etl

class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
app.config.from_object(Config())

CORS(app)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

@app.route("/api/articles", methods = ['GET'])
def retrive_data():
    data = get_articles()
    return jsonify(data)

@scheduler.task('interval', id='update_from_source', seconds=60, misfire_grace_time=900)
def update_from_source():
    try:
        run_etl()
        print('Data updated sucessfully')
    except:
        print('Error fetching data')


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