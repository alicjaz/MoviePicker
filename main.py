import random
import requests
from bs4 import BeautifulSoup

url='https://www.imdb.com/chart/top'

def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    raiting_tags = soup.select('td.posterColumn span[name=ir]')


    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        year_2 = year[1:5]
        return year_2
        
   
    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in raiting_tags]

    while(True):
        idx = random.randrange(0, len(titles))
        if int(years[idx]) > 2010:
            print(f'title: {titles[idx]} \nyear: {years[idx]} \nraiting: {ratings[idx]:.2f} \nstarring: {actors_list[idx]}\n')

            user_input = input(f'Do you want another film? (y/[n]) ')
            print()

            if user_input !='y':
                print()
                break

if __name__ == '__main__':
    main()