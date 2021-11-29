from gnewsclient import gnewsclient

def get_new():
    # declare a NewsClient object
    client = gnewsclient.NewsClient(language='Chinese', location='China', max_results=5)

    # get news feed
    res = client.get_news()
    print("news : ", res)

get_new()