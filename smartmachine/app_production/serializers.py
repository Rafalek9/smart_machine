from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Product, Process, ProcessDataField, ProcessDataValue, Image
from app_machine.models import Station, Pallet
from app_reference.models import Reference


class ProcessDataFieldSerializer(serializers.ModelSerializer):
    """
    Serilizator dodatkowych pól procesowych
    """
    class Meta:
        model = ProcessDataField
        fields = ['station', 'name',]


class ProcessDataValueSerializer(WritableNestedModelSerializer): #(serializers.ModelSerializer):
    """
    Serilizator wartości do dodatkowych pól procesowych
    """
    field = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=ProcessDataField.objects.all(),
        slug_field='id')

    class Meta:
        model = ProcessDataValue
        fields = ['id','process', 'field', 'value', ]

    """ 
     def create(self, validated_data):
        return ProcessDataValue.objects.create(**validated_data) 
    """


class ProcessSerializer(serializers.ModelSerializer):
    """
    Serializator procesu produkcyjnego
    """
    process_data = ProcessDataValueSerializer(source='process_data_value', many=True,)

    station = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=Station.objects.all(),
        slug_field='number')

    pallet = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=Pallet.objects.all(),
        slug_field='number')

    class Meta:
        model = Process
        fields = ['id' ,'station', 'pallet', 'start_process', 'end_process', 'operator', 'status', 'process_data']
        depth = 1


class FullSerializer(serializers.ModelSerializer):
    """
    Serializator kompletnego produktu z informacjami dziedziczonymi
    """
    process = ProcessSerializer(source='products', many=True, ) # prod
    reference = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=Reference.objects.all(),
        slug_field='name')

    class Meta:
        model = Product
        fields = ['id', 'reference', 'status', 'start', 'end', 'process', ]


class OnlyProductSerializer(serializers.ModelSerializer):
    """
    Serializator produktu - bez połączonych procesów produkcyjnych
    """
    reference = serializers.SlugRelatedField(
        many=False,
        required=False,
        read_only=False,
        queryset=Reference.objects.all(),
        slug_field='id')

    class Meta:
        model = Product
        fields = ['id', 'status', 'reference', 'start', 'end', ]


class OnlyProcessSerializer(WritableNestedModelSerializer): #(serializers.ModelSerializer):
    """
    Serializator procesów
    """
    process_data = ProcessDataValueSerializer(source='process_data_value', many=True, required=False)

    product = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=Product.objects.all(),
        slug_field='id')

    station = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=Station.objects.all(),
        slug_field='number')

    pallet = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=Pallet.objects.all(),
        slug_field='number')

    class Meta:
        model = Process
        fields = ['id', 'product', 'station', 'pallet', 'start_process', 'end_process', 'operator', 'status', 'process_data', ]
        depth = 1

        #def create(self, validated_data):
        #    return Process.objects.create(**validated_data)

    """   
    def create(self, validated_data):
        process_data = validated_data.pop('process_data', [])
        p = Process.objects.create(**validated_data)
        for pd in process_data:
            ProcessDataValue.objects.create(process=p, **pd)
        return process
    """


class ImagesSerializer(serializers.ModelSerializer):
    """
    Serializator zdjęć z systemów wizyjnych
    """

    camera = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name')

    class Meta:
        model = Image
        fields = ['id', 'image', 'inspection', 'camera', 'process', 'status', 'save_time', ]


