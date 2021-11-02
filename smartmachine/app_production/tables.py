from .models import Product, Process
import django_tables2 as tables


class ProductTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap.html"
        fields = ('id', 'reference', 'status', )
