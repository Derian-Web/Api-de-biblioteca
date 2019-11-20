from rest_framework import serializers

from editorial.models import Editorial


class EditorialSerializer(serializers.ModelSerializer):
    """
    General purpose Editorial serializer
    """
    class Meta:
        model = Editorial
        fields = ('nombre', 'direccion', 'pagina_web', 'ciudad')