import requests
import bs4
from collections import namedtuple

URL = "https://www.stuffyoushouldknow.com/podcasts/sysk-archive.htm"

def pull_website(URL):
    site = requests.get(URL)
    site.raise_for_status()
    return site

def scrape_site(site):
    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    podcast_list_soup = soup.select('.h4')
    podcast_date_soup = soup.select('.separation')


    podcast = namedtuple('podcast', 'title date')

    podcast_titles = [tags.get_text().strip() for tags in podcast_list_soup]
    podcast_date = [tags.get_text().strip() for tags in podcast_date_soup]

    podcast_info = [podcast(title, date) for title, date
                in zip(podcast_titles, podcast_date)]

    for idx, details in enumerate(podcast_info,1):
        print(f"{idx}. {details.title}, {details.date}")

    return podcast_info

if __name__ == '__main__':
    site = pull_website(URL)
    podcast_data = scrape_site(site)