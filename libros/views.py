from rest_framework import viewsets
from editorial.models import Editorial
from libros.serializers import LibroSerializer, CreateLibroSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


from editorial.serializers import EditorialSerializer
from libros.models import Libro
from libros.serializers import LibroSerializer

class LibroViewSet(viewsets.ModelViewSet):
    """
    Libro endpoint (viewset)
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLibroSerializer
        return LibroSerializer

    @action(detail=True, methods=['GET'])
    def libros(self, request, pk=None):
        editorial = self.get_object()
        libros = editorial.objects.filter(libros__id=libros.id)
        serialized = EditorialSerializer(editorial, many=True)
        if not libros:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Este autor no tiene libros'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)