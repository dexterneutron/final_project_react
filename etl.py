from extraction import ReadRss
from validation import validate_data
import sqlalchemy
import pandas as pd

def run_etl():
#Data extraction
    reader = ReadRss()
    articles = reader.parse_articles()
    if articles.notnull:
        print("Data extracted")
    else:
        raise Exception("Error extacting data")

#Data validation
    if validate_data(articles):
        print("Data validated")
    else:
        raise Exception("Data validation error")

#Data Loading
    try:
        engine = sqlalchemy.create_engine('sqlite:///articles.sqlite')
        articles['downloaded_at'] = pd.to_datetime("today")
        articles.to_sql('articles',engine, index=False, if_exists='replace')
        print("Data loaded")
    except Exception:
        print("Error Loading")

run_etl()