from django.db import models
import statistics

class Carta(models.Model):
    data = models.JSONField(default=dict)
    media = models.JSONField(default=0)
    dp = models.JSONField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    lsc = models.JSONField(default=dict)
    lic = models.JSONField(default=dict)

    class Meta:
        abstract = True
    def dados (self, *args, **kwargs):
        calcular_media = {}
        calcular_dp = {}
        calcular_lsc = {}
        calcular_lic = {}
        for chave, lista_numeros in self.data.items():
            if isinstance(lista_numeros,list) and len(lista_numeros)>1:
                
                calcular_media[chave] = statistics.mean(lista_numeros)
                calcular_dp[chave] = statistics.stdev(lista_numeros)
                calcular_lsc[chave]= calcular_media[chave] + 3*calcular_dp[chave]
                calcular_lic [chave]= calcular_media[chave] - 3*calcular_dp[chave]

            elif isinstance(lista_numeros,list) and len(lista_numeros)==1:
                calcular_media[chave] = lista_numeros[0]
                calcular_dp[chave] = 0.0
        self.media = calcular_media
        self.dp = calcular_dp
        self.lic = calcular_lic
        self.lsc = calcular_lsc


    def save(self, *args, **kwargs):
        self.dados()
        super().save(*args, **kwargs)

class Media_Amplitude(Carta):
            media_geral = models.FloatField(default=0)
            amplitude = models.JSONField(default=dict)

            def dados(self, *args, **kwargs):

                super().dados()
                calcular_media = 0
                for chave, lista_numeros in self.media.items():
                
                        calcular_media += lista_numeros
                self.media_geral = calcular_media/len(self.media)

                calcular_amplitude = {}
                for chave, lista_numeros in self.data.items():
                        if isinstance(lista_numeros,list) and len(lista_numeros)>1:
                            calcular_amplitude[chave] = max(lista_numeros)-min(lista_numeros)
                        elif isinstance(lista_numeros,list) and len(lista_numeros)==1:
                            calcular_amplitude[chave] = 0
                self.amplitude = calcular_amplitude

    
    
