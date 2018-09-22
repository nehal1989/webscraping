import requests
import bs4

URL = "https://www.stuffyoushouldknow.com/podcasts/sysk-archive.htm"

def pull_website(URL):
    site = requests.get(URL)
    site.raise_for_status()
    return site

def scrape_site(site):

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    podcast_list_soup = soup.select('.h4')
    podcast_date_soup = soup.select('.separation')

    podcast_list = [tags.get_text().strip() for tags in podcast_list_soup]
    podcast_date = [tags.get_text().strip() for tags in podcast_date_soup]

    new_list = [f"Podcast Title: {title}, {date}" for title, date
                in zip(podcast_list, podcast_date)]

    for idx, txt in enumerate(new_list,1):
        print(f"{idx}. {txt}")


if __name__ == '__main__':
    site = pull_website(URL)
    scrape_site(site)