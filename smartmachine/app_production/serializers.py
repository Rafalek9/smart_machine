from rest_framework import serializers
from .models import Product, Process, ProcessDataField, ProcessDataValue, Image
from app_machine.models import Station, Pallet
from app_reference.models import Reference


class ProcessDataFieldSerializer(serializers.ModelSerializer):
    """
    Serilizator dodatkowych pól procesowych
    """
    class Meta:
        model = ProcessDataField
        fields = ['station', 'name', ]


class ProcessDataValueSerializer(serializers.ModelSerializer):
    """
    Serilizator wartości do dodatkowych pól procesowych
    """
    field = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        queryset=ProcessDataField.objects.all(),
        slug_field='name')

    class Meta:
        model = ProcessDataValue
        fields = ['field', 'value', ]

    def create(self, validated_data):
        return ProcessDataValue.objects.create(**validated_data)


class ProcessSerializer(serializers.ModelSerializer):
    """
    Serializator procesu produkcyjnego
    """
    extended_data = ProcessDataValueSerializer(source='proc', many=True, )
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
        fields = ['station', 'pallet', 'start_process', 'end_process', 'operator', 'status', 'extended_data']
        depth = 1


class FullSerializer(serializers.ModelSerializer):
    """
    Serializator kompletnego produktu z informacjami dziedziczonymi
    """
    process = ProcessSerializer(source='prod', many=True, )
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
        read_only=False,
        queryset=Reference.objects.all(),
        slug_field='name')

    class Meta:
        model = Product
        fields = ['id', 'status', 'reference', 'start', 'end', ]


class OnlyProcessSerializer(serializers.ModelSerializer):
    """
    Serializator procesów - bez informacji o produkcie końcowym
    """
    extended_data = ProcessDataValueSerializer(source='proc', many=True, )
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
        fields = ['station', 'pallet', 'start_process', 'end_process', 'operator', 'status', 'extended_data', ]
        depth = 1


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
