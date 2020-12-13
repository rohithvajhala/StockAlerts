from django.shortcuts import render
from api.stocks import*


# Create your views here.
def update_quotes(request):
    contents = {
        'stocks': get_popular_stocks(),
    }

    return render(request, 'update_quotes.html', contents)


def home_view(request, *args, **kwargs):
    contents = {}
    if request.POST:
        query = request.POST.get('query')
        stocks = search_stocks(query)
        contents = {
            'stocks': stocks,
        }
        return render(request, "search.html", contents)

    contents = {
        'stocks': get_popular_stocks(),
    }

    return render(request, "home.html", contents)


def stock_details_view(request, name, *args, **kwargs):
    stocks = get_stock_details(name)
    if request.user.is_authenticated:
        watch_list = request.user.customer.userstock_set.all()
    else:
        watch_list = []

    stocks['subscribe_button'] = True

    for item in watch_list:
        if item.stock_name == name:
            stocks['subscribe_button'] = False
            break

    params = {
        'stocks': [stocks],
    }
    return render(request, "stock_details.html", params)
