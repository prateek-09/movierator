import requests
from bs4 import BeautifulSoup

class IMDBScrapper():
    
    def __init__(self, url='https://www.imdb.com/chart/top/'):
        self.url = url
        response = requests.get(self.url).text
        self.soup = BeautifulSoup(response, 'html.parser')

    def _get_data(self):
        data = []
        table = self.soup.find('table', attrs={'class':'chart'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values
        print(data)

    def _get_table(self):
        self.data_arr = []

        try:

            table = self.soup.find('table', attrs={'class':'chart'})
            table_body = table.find('tbody', attrs={'class': 'lister-list'})
            rows = table_body.find_all('tr')
            
            for row in rows:
                title_column = row.find_all('td', attrs={'class': 'titleColumn'})
                
                title = title_column[0].text
                split_title = title.split()
                rank = split_title[0][:-1]
                year = split_title[-1][1:-1]
                title = " ".join(split_title[1:-1])
                imdb_rating_column = row.find_all('td', attrs={'class': 'imdbRating'})
                
                details = {
                    'rank' : int(rank.strip()),
                    'title' : title.strip(),
                    'year' : int(year.strip()),
                    'rating' : float(imdb_rating_column[0].text)

                }
                self.data_arr.append(details)
            
            return self.data_arr
        
        except:
            
            return self.data_arr


        def get_data(self):
            return self._get_table()