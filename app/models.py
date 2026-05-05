from django.db import models
import statistics,math

class Carta(models.Model):
    data = models.JSONField(default=dict)
    media = models.JSONField(default=0)
    dp = models.JSONField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    dp_geral = models.FloatField(default=0)
    x1 = models.FloatField(default=0)
    x0= models.FloatField(default=0)
    lse = models.FloatField(default=0)
    lie = models.FloatField(default=0)
    cp = models.FloatField(default=0)
    cpk = models.FloatField(default=0)
    probabilidade = models.JSONField(default=dict)

    class Meta:
        abstract = True
    def dados (self, *args, **kwargs):
        calcular_media = {}
        calcular_dp = {}
        for chave, lista_numeros in self.data.items():
            if isinstance(lista_numeros,list) and len(lista_numeros)>1:
                
                calcular_media[chave] = round(statistics.mean(lista_numeros),3)
                calcular_dp[chave] = round(statistics.stdev(lista_numeros),3)
                

            elif isinstance(lista_numeros,list) and len(lista_numeros)==1:
                calcular_media[chave] = lista_numeros[0]
                calcular_dp[chave] = 0.0
        amostra = []
        for valores in self.data.values():
            amostra += valores
        self.dp_geral = round(statistics.stdev(amostra),3)
        self.media =calcular_media
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
                            calcular_amplitude[chave] = round(max(lista_numeros)-min(lista_numeros),3)
                        elif isinstance(lista_numeros,list) and len(lista_numeros)==1:
                            calcular_amplitude[chave] = 0
                
                self.media_geral = round(statistics.mean(list(self.media.values())),3)
                self.amplitude = calcular_amplitude
                self.media_amplitude = round(statistics.mean(list(self.amplitude.values())),3)
                self.lic_media = round( self.media_geral - 3*self.dp_geral,3)
                self.lsc_media =round( self.media_geral + 3*self.dp_geral,3)
                self.lic_amp = round( self.media_amplitude*self.d3, 3)
                self.lsc_amp = round( self.media_amplitude*self.d4, 3)
                self.cp =round(((self.lse-self.lie)/(6*self.dp_geral)),3)
                cpk_superior = (self.lse - self.media_geral) / (3 * self.dp_geral)
                cpk_inferior = (self.media_geral - self.lie) / (3 * self.dp_geral)
                self.cpk = min(cpk_superior, cpk_inferior)
                curva_normal = statistics.NormalDist(mu=self.media_geral, sigma=self.dp_geral)
                intervalo = (curva_normal.cdf(self.x1) - curva_normal.cdf(self.x0))*100
                prob_menor_x1 = curva_normal.cdf(self.x1) * 100
                prob_maior_x0 = (1 - curva_normal.cdf(self.x0)) * 100
                self.probabilidade= {"menor_x1": round(prob_menor_x1,3),
                                     "maior_x0": round(prob_maior_x0,3),
                                     "intervalo":round(intervalo,3)}
class p (Carta):
    n = 20
    lc = models.FloatField(default=0)
    lsc = models.FloatField(default=0)
    lic = models.FloatField(default=0)
    taxa = models.JSONField(default=dict)
    def dados(self):
        calcular_taxas = {}
        calcular_lc = 0
        tamanho =0
        super().dados()
        for i,valores in self.data.items():
            calcular_lc += valores[0]
            tamanho +=self.n
            calcular_taxas[i]=round(valores[0]/self.n,3)
        self.lc = calcular_lc/tamanho
        def desvio(p,n):
           return math.sqrt((p*(1-p))/n)
  
        if (self.lc-3*desvio(self.lc,self.n)>0): 
             self.lic= round(self.lc-3*desvio(self.lc,self.n),3)
        else: self.lic=0
        self.lsc = round(self.lc+3*desvio(self.lc,self.n),3)
        self.taxa = calcular_taxas
class u(Carta):
     n = 20
     lc = models.FloatField(default=0)
     lic = models.FloatField(default=0)
     lsc = models.FloatField(default=0)
     taxa = models.JSONField(default=dict)
     def dados(self):
        calcular_taxas = {}
        calcular_lc = 0
        tamanho=0
        super().dados()
        for i,valores in self.data.items():
            calcular_lc += valores[0]
            calcular_taxas[i]=round(valores[0]/self.n,3)
            tamanho +=self.n
        self.lc = calcular_lc/tamanho
        def desvio(u,n):
           return math.sqrt(u/n)
        if (self.lc-3*desvio(self.lc,self.n)>0): 
             self.lic= round(self.lc-3*desvio(self.lc,self.n),3)
        else: self.lic=0
        self.lsc = round(self.lc+3*desvio(self.lc,self.n),3)
        self.taxa = calcular_taxas
class imr(Carta):
     
     amplitude_movel = models.JSONField(default=dict)
     lc_i = models.FloatField(default=0)
     lsc_i = models.FloatField(default=0)
     lic_i = models.FloatField(default=0)
     lc_mr = models.FloatField(default=0)
     lsc_mr = models.FloatField(default=0)
     lic_mr= models.FloatField(default=0)
     am_media = models.FloatField(default=0)
     e2 = 2.66
     d3 = 0
     d4 = 3.267
     def dados (self, *args, **kwargs):
        super().dados()
        calcular_amplitudem = {}
        valores = list(self.media.values())

        for i in range (1,len(valores)):
            mr_atual = round(abs(valores[i]-valores[i-1]))
            calcular_amplitudem[i-1]=mr_atual
        
        self.amplitude_movel = calcular_amplitudem
        self.lc_i = round(statistics.mean(list(self.media.values())),3)
        self.am_media = statistics.mean(list(self.amplitude_movel.values()))
        self.lsc_i = round(self.lc_i +self.e2*self.am_media,3)
        self.lic_i = round(self.lc_i -self.e2*self.am_media,3)
        self.lic_mr = round(self.am_media*self.d3,3)
        self.lsc_mr = round(self.am_media*self.d4,3)
        self.lc_mr = self.am_media
    
    
