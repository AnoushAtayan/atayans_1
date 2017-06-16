# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Store
from django.views.generic import ListView

from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    return render(request, 'shop/index.html')



class StoreListView(ListView):
    queryset = Store.objects.all()
    context_object_name = 'stores'
    paginate_by = 4
    template_name = 'shop/store_list.html'







#     page = request.GET.get('page')
#     try:
#         stores = paginator.page(page)
#     except PageNotAnInteger:
#         stores = paginator.page(1)
#     except EmptyPage:
#         stores = paginator.page(paginator.num_pages)
#
#     query = request.GET.get("q")
#
#     if query:
#         stores = stores_list.filter(
#             Q(store_name__icontains=query)|
#             Q(store_type__icontains=query)).distinct()
#
#
#     return render(request, 'shop/store_list.html', {'page':page, 'stores': stores})