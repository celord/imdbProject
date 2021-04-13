import requests,re
from bs4 import BeautifulSoup
from urllib.parse import urlencode


class Movie:

    def __init__(self):

        self.top1000 = 'https://www.imdb.com/search/title/?title_type=movie,tv_movie&groups=top_1000&production_status=released&start={}'

    def get_top_movies(self):
        """
        Returns a dictionary with the top 1000 movies from imdb with charateristics
        """
        movies = {}
        counter = 1

        for i in range(1,1000,50):

            result = requests.get(self.top1000.format(str(i)))
            result = BeautifulSoup(result.content, features='html.parser')
            result = result.find_all('div', {'class': 'lister-item-content'})
            for i in result:
                actor_director = i.find_all('p')[2].find_all('a')
                year = i.find('h3').find_all(
                    'span', {'class': 'lister-item-year text-muted unbold'})[0].text.strip('()')
                movies[counter] = {'movie_title' : i.find('h3').find('a').text,
                                   'director_actor': [i.text for i in actor_director],
                                   'year': year}

                counter += 1

        return movies



