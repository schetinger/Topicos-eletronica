from django.db import models
import statistics

class Carta(models.Model):
    data = models.JSONField(default=dict)
    media = models.JSONField(default=0)
    dp = models.JSONField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    dp_geral = models.FloatField(default=0)

    class Meta:
        abstract = True
    def dados (self, *args, **kwargs):
        calcular_media = {}
        calcular_dp = {}
        for chave, lista_numeros in self.data.items():
            if isinstance(lista_numeros,list) and len(lista_numeros)>1:
                
                calcular_media[chave] = statistics.mean(lista_numeros)
                calcular_dp[chave] = statistics.stdev(lista_numeros)
                

            elif isinstance(lista_numeros,list) and len(lista_numeros)==1:
                calcular_media[chave] = lista_numeros[0]
                calcular_dp[chave] = 0.0
        calcular_dp_geral = statistics.mean(list(calcular_dp.values()))
        self.dp_geral = calcular_dp_geral
        self.media = calcular_media
        self.dp = calcular_dp
       


    def save(self, *args, **kwargs):
        self.dados()
        super().save(*args, **kwargs)

class Media_Amplitude(Carta):
            media_geral = models.FloatField(default=0)
            amplitude = models.JSONField(default=dict)
            media_amplitude = models.FloatField(default=0)
            lsc_media = models.FloatField(default=0)
            lsc_amp = models.FloatField(default=0)
            lic_media = models.FloatField(default=0)
            lic_amp = models.FloatField(default=0)
            #d4 para 5 valores
            d4 = 2.114
            #d3 para 5 valores
            d3 = 0
            
            

            def dados(self, *args, **kwargs):

                super().dados()
                calcular_amplitude = {}
                for chave, lista_numeros in self.data.items():
                        if isinstance(lista_numeros,list) and len(lista_numeros)>1:
                            calcular_amplitude[chave] = max(lista_numeros)-min(lista_numeros)
                        elif isinstance(lista_numeros,list) and len(lista_numeros)==1:
                            calcular_amplitude[chave] = 0
                 
                self.media_geral = statistics.mean(list(self.media.values()))
                self.media_amplitude = statistics.mean(list(self.amplitude.values()))
                self.lic_media = self.media_geral - 3*self.dp_geral
                self.lsc_media = self.media_geral + 3*self.dp_geral
                self.lic_amp = self.media_amplitude*self.d3
                self.lsc_amp = self.media_amplitude*self.d4
                self.amplitude = calcular_amplitude

    
    
