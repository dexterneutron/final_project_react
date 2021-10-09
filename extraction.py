from bs4 import BeautifulSoup
import requests
import pandas as pd
 
class ReadRss:
    HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
        }
    VERGE_URL = 'https://www.theverge.com/rss/index.xml'
    TECHCRUNCH_URL = 'https://techcrunch.com/feed/'
    MASHABLE_URL = 'https://mashable.com/feeds/rss/all'    
    URL_LIST = ["mashable","techcrunch","verge"]

    def __init__(self):
        self.reponse_objects = {}
        urls = {"verge":self.VERGE_URL,"techcrunch":self.TECHCRUNCH_URL, "mashable":self.MASHABLE_URL}
        
        for page in self.URL_LIST:
            rss_url =  urls[page]       
            try:
                r = requests.get(rss_url, headers = self.HEADERS)
                self.reponse_objects[page] = r
            except Exception as e:
                print('Error fetching the URL: ', rss_url)
                print(e)

    def parse_articles(self):
        all_articles = []

        for key,value in self.reponse_objects.items():
          #Each RSS site has its own structure, so, it's needed to parse each of them separately
            if key == "verge":
                try:    
                    soup = BeautifulSoup(value.text, 'lxml')
                    articles = soup.findAll('entry')
                    articles_dicts = [{'source':'The Verge',
                    'title':a.find('title').getText(),
                    'published':a.find('published').getText(),
                    'id':a.find('id').getText(),
                    } for a in articles]
                    all_articles.append(articles_dicts)
                except Exception as e:    
                    print('Could not parse the xml from the verge')
                    print(e)

            elif key == "techcrunch":
                try:    
                    soup = BeautifulSoup(value.text, 'xml')
                    articles = soup.findAll('item')
                    articles_dicts = [{'source':'Techcrunch',
                    'title':a.find('title').text,
                    'published':a.find('pubDate').text,
                    'id':a.find('link').text
                    } for a in articles]
                    all_articles.append(articles_dicts)
                except Exception as e:    
                    print('Could not parse the xml: from techcrunch')
                    print(e)

            elif key == "mashable":
                try:    
                    soup = BeautifulSoup(value.text, 'xml')
                    articles = soup.findAll('item')
                    articles_dicts = [{'source':'Mashable',
                    'title':a.find('title').text,
                    'published':a.find('pubDate').text,
                    'id':a.find('link').text
                    } for a in articles]
                    all_articles.append(articles_dicts)
                except Exception as e:    
                    print('Could not parse the xml: from mashable')
                    print(e)
            #Finally we merge the list into one
            output_list = []
            for list in all_articles:
                output_list.extend(list)
            dataframe = pd.DataFrame(output_list)
        return dataframe