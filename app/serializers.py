from app.models import Media_Amplitude,imr,p,u
from rest_framework import serializers
class CartaXr(serializers.ModelSerializer):
    class Meta:
        model = Media_Amplitude
        fields = ['id',
                  'media',
                  'dp',
                  'created_at',
                  'data',
                  'media_geral',
                  'amplitude',
                  'lic_media',
                  'lsc_media',
                  'dp_geral',
                  'media_amplitude',
                  'lic_amp',
                  'lsc_amp']
class CartaIMR(serializers.ModelSerializer):
    class Meta:
        model = imr
        fields = [
                  'id',
                  'media',
                  'dp',
                  'created_at',
                  'data',
                  'dp_geral',
                  'lc',
                  'lic',
                  'lsc',
                  'amplitude_movel'


        ]
class CartaP(serializers.ModelSerializer):
    class Meta:
        model = p
        fields = [
                  'id',
                  'media',
                  'dp',
                  'created_at',
                  'data',
                  'dp_geral',
                  'lc',
                  'lic',
                  'lsc'
        ]
class CartaU(serializers.ModelSerializer):
    class Meta:
        model = u
        fields = [
                  'id',
                  'media',
                  'dp',
                  'created_at',
                  'data',
                  'dp_geral',
                  'lc',
                  'lic',
                  'lsc',
                  'taxa'
        ]

