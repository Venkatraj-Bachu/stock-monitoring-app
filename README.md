## stock-monitoring-app

This Python script monitors the stock price of a specified company and sends text messages with relevant news articles if the stock price changes by a significant percentage. It integrates stock data retrieval, news article fetching, and text messaging using the Alpha Vantage API, a news API, and the Twilio service.

## Requirements

Before using this script, you need to have the following requirements in place:

1. **Python**: Make sure you have Python installed on your system.

2. **API Keys**:
   - Alpha Vantage API Key for stock data retrieval.
   - News API Key for fetching news articles.
   - Twilio Account SID and Authentication Token for sending text messages.

## Configuration

You should configure the script by setting the following constants and variables in the script:

- `STOCK`: The stock symbol you want to monitor (e.g., "TSLA" for Tesla Inc).
- `COMPANY_NAME`: The name of the company.
- `THRESHOLD_PERCENTAGE_CHANGE`: The percentage change threshold that triggers news article retrieval.
- `NEWS_API_KEY`: Your API key for the news API.
- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio Authentication Token.
- `TWILIO_PHONE`: Your Twilio phone number.
- `MY_PHONE`: Your phone number.

## Usage

1. Run the script using the configured parameters.
2. The script will retrieve historical stock data and calculate the percentage change.
3. If the change is significant (above the defined threshold), it will fetch news articles related to the company.
4. The script will send text messages with the stock information and news headlines to your phone using the Twilio service.

## Acknowledgments

- [Alpha Vantage API](https://www.alphavantage.co/) for stock data.
- [News API](https://newsapi.org/) for news articles.
- [Twilio](https://www.twilio.com/) for text messaging.

Feel free to modify and improve this script to suit your specific needs. Happy monitoring and stay informed!
