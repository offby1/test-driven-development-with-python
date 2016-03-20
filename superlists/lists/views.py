from django.shortcuts import render
from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        item = Item.objects.create(text=request.POST['item_text'])
        item.save()

    return render(request, 'home.html', {'items': Item.objects.all()})
