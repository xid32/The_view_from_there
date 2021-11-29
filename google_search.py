import googlesearch as google
import requests
import bs4


def google_search(query, top_pages=30):
    search_results = google.search(query)
    urls = []
    for i, result in enumerate(search_results):
        if i >= top_pages:
            break
        urls.append(result)
    return urls

if __name__ == '__main__':
    # for test
    urls = google_search('article 我爱你，吴亦凡')
    for url in urls:
        re = requests.get(url)
        soup = bs4.BeautifulSoup(re.text)
        print(soup.title.text)