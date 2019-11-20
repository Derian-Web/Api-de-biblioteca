from rest_framework import viewsets
from editorial.models import Editorial
from editorial.serializers import EditorialSerializer


class EditorialViewSet(viewsets.ModelViewSet):
    """
    Editorial endpoint (viewset)
    """
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
