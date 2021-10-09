from extraction import ReadRss
from validation import validate_data


if __name__ == '__main__':

#data extraction
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