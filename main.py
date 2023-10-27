from stock_info import StockData
from news_info import NewsData
from twilio_setup import Twilio


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
THRESHOLD_PERCENTAGE_CHANGE = 1

NEWS_API_KEY="de41e854385b40f5b7855d334776679c"

TWILIO_ACCOUNT_SID = "ACc0bbcd79cbd01c7acf7f814b80d8f4c1"
TWILIO_AUTH_TOKEN = "71b15ed39719da55dea6c5729a26c8b5"
TWILIO_PHONE = "+18447342453"
MY_PHONE = '+15107648921'

# Get Stock Data
stock = StockData(STOCK)

if stock.api_call_valid:
    yesterday_stock_data = stock.get_stock_data()
    day_before_yesterday_stock_data = stock.get_stock_data(2)

    if 'Error' in yesterday_stock_data or 'Error' in day_before_yesterday_stock_data:
        print('Invalid date input given to the get_stock_data method of the StockData class')
    else:
        yesterday_closing_price = yesterday_stock_data['close_price']
        day_before_yesterday_closing_price = day_before_yesterday_stock_data['close_price']
        difference = yesterday_closing_price - day_before_yesterday_closing_price
        percentage_change = (abs(difference) / yesterday_closing_price) * 100

        # Get News if percentage change is greater than threshold
        if percentage_change >= THRESHOLD_PERCENTAGE_CHANGE:
            news = NewsData(COMPANY_NAME, NEWS_API_KEY)
            top_3_articles = news.get_top_n_articles(3)

            if difference < 0:
                up_down = '🔻'
            else:
                up_down = '🔺'

            news_data_messages = [f"{STOCK}: {up_down} by {round(percentage_change)}%\nHeadline: {x['title']}.\nBrief: {x['description']}" for x in top_3_articles]

            # Send text messages
            twilio = Twilio(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            for article in news_data_messages:
                message_status = twilio.send_message(message=article, from_phone=TWILIO_PHONE, to_phone=MY_PHONE)
                print(article)
                print(message_status)

else:
    print(stock.get_stock_data()['Error'])
