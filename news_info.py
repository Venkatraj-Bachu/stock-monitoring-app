import requests

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


class NewsData:
    """
        This class is used to get the news articles by making an API call to "https://newsapi.org/v2/everything"\n
        Required parameters to call the class:\n
        company_name (str) : name of the company to get the news of.
        news_api (str) : the API TOKEN of newsapi.org
    """
    def __init__(self, company_name: str, news_api: str):
        news_parameters = {
            'q': company_name,
            'apiKey': news_api,
        }
        news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
        self.news_data = news_response.json()['articles']

    def get_top_n_articles(self, n: int = 1) -> list:
        """
        Fetches top 'n' news articles of respective company/entity\n
        :param n: (type) int - number of articles required
        :return: (type) list - list of n articles
        """
        top_n_articles = self.news_data[:n] if self.news_data else []
        return top_n_articles
