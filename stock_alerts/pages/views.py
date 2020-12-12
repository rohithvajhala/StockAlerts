from django.shortcuts import render
from api.stocks import get_popular_stocks, search_stocks


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
