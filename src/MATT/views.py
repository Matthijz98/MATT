from .models import Printer
from .serializers import PrinterSerializer
from rest_framework import generics, viewsets

class PrinterListCreate(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer