from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.conf.urls import url
from .models import Product


class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    template_name = 'products/details.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()



class ProductListView(ListView):
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
            'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):

    template_name = 'products/details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("product doesn't exist")
        return instance

def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    # print(args)
    # print(kwargs)
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('No Products here')
    #     raise Http404("product doesn't exists")
    # except:
    #     print("huh?")

    qs  = Product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("product doesn't exists")

    # print(instance)
    context = {
            'object': instance
    }
    return render(request, "products/details.html", context)
