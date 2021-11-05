from django.shortcuts import render, get_object_or_404
from app_production.serializers import FullSerializer, OnlyProductSerializer, OnlyProcessSerializer
from rest_framework import viewsets
from .models import Product, Process, ProcessDataField, ProcessDataValue, Image
from app_machine.models import Station


def product_list_view(request):
    products = Product.objects.all()
    stations = Station.objects.all()

    cnt_OK = Product.objects.filter(status='2').count()
    cnt_NOK = Product.objects.filter(status='3').count()
    cnt_brak = Product.objects.filter(status='0').count()

    data = {
        'products': products,
        'stations': stations,
        'cnt_OK': cnt_OK,
        'cnt_NOK': cnt_NOK,
        'cnt_brak': cnt_brak,
    }
    return render(request, 'app_production/product_list/product_list.html', data)


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    process = Process.objects.filter(product=product).order_by('start_process', )
    process_data_value = ProcessDataValue.objects.filter(process__in=process)
    images = Image.objects.filter(process__in=process)
    data = {
        'product': product,
        'process': process,
        'process_data_value': process_data_value,
        'images': images,
    }
    return render(request, 'app_production/product_detail/product_detail.html', data)


class FullViewSet(viewsets.ModelViewSet):
    """
    API Viewset for full view of product/process/data
    """
    queryset = Product.objects.all()
    serializer_class = FullSerializer


class OnlyProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = OnlyProductSerializer


class OnlyProcessSerializer(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = OnlyProcessSerializer
