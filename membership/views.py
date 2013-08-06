from django.http import HttpResponse
from django.shortcuts import render

from membership.models import Shop

def index(request):
    shop_list = Shop.objects.order_by('-name')
    context = {'shop_list' : shop_list}
    return render(request, 'membership/index.html', context)
