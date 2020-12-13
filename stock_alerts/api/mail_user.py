import smtplib
import os
from string import Template
import time
from django.contrib.auth.models import User
from pathlib import Path
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(os.path.join(BASE_DIR, 'api'))
from stocks import*


ONE_DAY = (60 * 60 * 24)
MY_ADDRESS = os.environ.get('STOCK_ALERTS_MAIL')
PASSWORD = os.environ.get('STOCK_ALERTS_PASS')


def send_mail(email_id, message):
    msg_txt = Template(message)

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    msg = MIMEMultipart()
    msg['From'] = MY_ADDRESS
    msg['To'] = email_id
    msg['Subject'] = "Favorite stock price alert"

    # add in the message body
    msg.attach(MIMEText(message))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()


def create_low_msg(stock):
    return f"Hey, \n \
    {stock.stock_full_name} stock price dropped \
below {stock.threshold_low}. It might be good time to invest something \n\
\n\
best regards, \n\
StockAlerts"


def create_high_msg(stock):
    return f"Hey \n \
    {stock.stock_full_name} stock price raised above \
    {stock.threshold_high}. It might be good time to sell stocks \n\
\n\
best regards, \n\
StockAlerts"


def send_subscriber_updates():
    users = User.objects.all()
    current_time = time.time()
    for user in users:
        stocks = user.customer.userstock_set.all()
        for stock in stocks:
            if stock.send_update:
                if current_time > (ONE_DAY + stock.last_update_sent):
                    res = stock_get_quote(stock.stock_name)

                    if (res['c'] < stock.threshold_low):
                        msg_txt = create_low_msg(stock)
                        send_mail(user.email, msg_txt)
                        stock.last_update_sent = current_time
                        stock.save()
                    elif(res['c'] > stock.threshold_high):
                        msg_text = create_high_msg(stock)
                        send_mail(user.email, msg_txt)
                        stock.last_update_sent = current_time
                        stock.save()

