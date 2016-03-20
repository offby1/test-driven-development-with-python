from django.http import HttpResponse
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = list_.item_set.all()

    context = {
        'list_id': list_id,
        'items': items,

        # todo -- ask django for this URL, rather than
        # kludging it up by hand
        'add_item_url' : '/lists/{}/add_item'.format(list_id),
    }

    return render(request, 'list.html', context)

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    item = Item.objects.create(text=request.POST['item_text'],
                               list=list_)

    return redirect('/lists/{}/'.format(list_.id))


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/{}/'.format(list_.id))
