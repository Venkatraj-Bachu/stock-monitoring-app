from stock_info import StockData
from news_info import NewsData
from twilio_setup import Twilio


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
THRESHOLD_PERCENTAGE_CHANGE = 1

NEWS_API_KEY="de41e854385b40f5b7855d334776679c"

TWILIO_ACCOUNT_SID = "ACc0bbcd79cbd01c7acf7f814b80d8f4c1"
TWILIO_AUTH_TOKEN = "8aec6b9c47112fed92e28afb3804564e"
TWILIO_PHONE = "+18447342453"
MY_PHONE = '+17043095505'

# Get Stock Data
stock = StockData(STOCK)

yesterday_closing_data = stock.get_stock_closing_data()
day_before_yesterday_closing_data = stock.get_stock_closing_data(2)

difference = yesterday_closing_data - day_before_yesterday_closing_data
percentage_change = (abs(difference) / yesterday_closing_data) * 100

# Get News if percentage change is greater than threshold
if percentage_change >= THRESHOLD_PERCENTAGE_CHANGE:

    news = NewsData(COMPANY_NAME, NEWS_API_KEY)
    top_3_articles = news.get_top_n_articles(3)
    news_data_messages = [[x['title'], x['description']] for x in top_3_articles]

    # Send text messages
    twilio = Twilio(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if difference < 0:
        text_message = f"{STOCK} 🔻 {percentage_change}%\n"
    else:
        text_message = f"{STOCK} 🔺 {percentage_change}%\n"
    text_message += "Potential Reasons:\n"
    for message in news_data_messages:
        text_message += f"\n\nHeadline: {message[0]}\nBrief:{message[1]}"

    message_status = twilio.send_message(text_message, TWILIO_PHONE, MY_PHONE)
    print(message_status)

