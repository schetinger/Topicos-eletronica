from app.models import Media_Amplitude
from rest_framework import serializers
class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media_Amplitude
        fields = ['id',
                  'media',
                  'dp',
                  'created_at',
                  'data','media_geral',
                  'amplitude',
                  'lic_media',
                  'lsc_media',
                  'dp_geral',
                  'media_amplitude',
                  'lic_amp',
                  'lsc_amp']