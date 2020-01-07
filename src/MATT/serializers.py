from rest_framework import serializers
from .models import Printer


class PrinterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Printer
        fields = ['printer_name']

class

