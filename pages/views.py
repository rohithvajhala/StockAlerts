from django.shortcuts import render
from django.shortcuts import redirect
from api.stocks import*
from customer.models import UserStock, Customer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from customer.forms import clean_new_user_stock_form_data


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


@login_required(login_url='login_page')
def subscribe_stock_view(request, name, *args, **kwargs):
    watch_list = request.user.customer.userstock_set.all()

    # Don't allow same stock to be subscribed more than once
    for item in watch_list:
        if item.stock_name == name:
            return redirect('watch_list')

    customer_obj = request.user.customer
    stocks = get_stock_details(name)
    context = {'stock': stocks,
               'low_th': stocks['quote']['c'] * 0.9,
               'high_th': stocks['quote']['c'] * 1.1
               }

    if request.method == 'POST':
        data = clean_new_user_stock_form_data(request)

        if data['error']:
            messages.error(request, data['error'])
            return render(request, 'subscribe_stock.html', context)

        item = UserStock(
            customer_obj=customer_obj,
            stock_name=name,
            stock_full_name=stocks['description'],
            threshold_low=data['th_low'],
            threshold_high=data['th_high'],
            send_update=data['send_update']
        )

        item.save()
        return redirect('watch_list')

    return render(request, 'subscribe_stock.html', context)


@login_required(login_url='login_page')
def watch_list_view(request, *args, **kwargs):
    watch_list = request.user.customer.userstock_set.all()
    context = {'watch_list': watch_list}
    return render(request, 'watch_list.html', context)


@login_required(login_url='login_page')
def update_view(request, name, *args, **kwargs):
    watch_list = request.user.customer.userstock_set.all()

    for item in watch_list:
        if item.stock_name == name:
            stocks = get_stock_details(name)
            context = {'stock': stocks,
                       'low_th': item.threshold_low,
                       'high_th': item.threshold_high,
                       'send_update': item.send_update
                       }

            if request.method == 'POST':
                data = clean_new_user_stock_form_data(request)

                if data['error']:
                    messages.error(request, data['error'])
                    return render(request, 'user_stock_update.html', context)

                item.threshold_low = data['th_low']
                item.threshold_high = data['th_high']
                item.send_update = data['send_update']
                item.save()
                return redirect('watch_list')

    return render(request, 'user_stock_update.html', context)

@login_required(login_url='login_page')
def delete_view(request, name, *args, **kwargs):
    watch_list = request.user.customer.userstock_set.all()
    for item in watch_list:
        if item.stock_name == name:
            item.delete()

    return redirect('watch_list')
