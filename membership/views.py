from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from membership.models import Shop

def index(request):
    shop_list = Shop.objects.order_by('-name')
    context = {'shop_list' : shop_list}
    return render(request, 'membership/index.html', context)

def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'membership/shop_detail.html', {'shop': shop})
