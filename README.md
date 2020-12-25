# StockAlerts

Stock alerts is an open source website where users can fetch basic information and stock values of
various US companies. Users can create a profile and subscribe to their favorite stocks. Once subscribed, user will be able to get the alerts when their favorite stock price drops/raises depending on the chosen thresholds. This application uses open source
API [finnhub.io](https://finnhub.io/) to get the information related to stocks.

Live site is available at [https://my-stock-alerts.herokuapp.com/](https://my-stock-alerts.herokuapp.com/)
## Build Requirements
- Python 3.7 or higher
- Django
- Whitenoise (For serving static files)
- Heroku account (To host the site)
- Postgres SQL

This application is built using Django framework. Application contains api for creation of user profile, user authentication, api to subscribe to favorite stocks, select when to get mail updates, api to manage and delete subscribed stocks and api to mail alerts related to stock price update and password reset. Users can also fetch details and stock prices of over 10000 US companies,

## Usage

### How to subscribe to stocks?

- Create an account [here](https://my-stock-alerts.herokuapp.com/sign_up) and login to your account.
- Once logged in, on the home page you can search for your favorite stock.
- It shows the list of stocks based on your search query. Click on the stock you like and you can see more details related to the company.
- When you scroll to the bottom of the stock details you can see the subscribe button.
- Once you click subscribe button it will ask you to fill the lower and higher limits for the stock. (You can leave the fields empty if you wish).
- After selecting the limit check option to receive updates.


Now you will receive a mail as soon as the stock price drops below your selected lower limit or raises above your selected higher limit.


### Want to update the limits for your stock or turnoff alerts?

You can easily manage the limits / delete your subscribed stock by going to "WatchList" tab. "WatchList" tab provides you an overview of your subscribed stocks.
