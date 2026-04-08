import io
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_da_carta(dados_brutos):
    # 1. Cria uma "tela" em branco para o gráfico
    plt.figure(figsize=(8, 6))
    # 2. Prepara os dados do seu JSON para o Seaborn entender
    # Ele gosta de duas listas: uma com os números e outra com os nomes (eixos X e Y)
    valores = []
    nomes_das_listas = []
    for chave, lista_numeros in (dados_brutos or {}).items():
        for numero in lista_numeros:
            valores.append(numero)
            nomes_das_listas.append(f"Lista {chave}")       
    # 3. Pede pro Seaborn desenhar o Boxplot
    sns.boxplot(x=nomes_das_listas, y=valores)
    # Dá um título bacana
    plt.title("Distribuição das Listas (Amplitude e Concentração)")
    plt.ylabel("Valores")
    plt.xlabel("Listas da Carta")
    # 4. Salva o gráfico na memória RAM (em vez de salvar no HD)
    # Isso é perfeito para injetar direto em um gerador de PDF depois!
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    # Fecha o gráfico para liberar a memória do servidor
    plt.close() 
    # Volta o "ponteiro" do buffer para o começo e retorna os dados da imagem
    buffer.seek(0)
    return buffer

def grafico_media(carta):
    plt.figure(figsize=(8, 6))
    # 1. Puxamos apenas a Lista "1" do seu JSON
    # Se a lista "1" não existir, pegamos uma lista vazia para não quebrar
    lista_1 = list(carta.media.values())
    
    if len(lista_1) > 0:
        # 2. Fazemos os cálculos rápidos
        limite_superior = carta.lsc_media
        limite_inferior = carta.lic_media
        # Criamos um eixo X falso só para espalhar os pontos 
        # (vai ser: 1, 2, 3, 4, 5... dependendo do tamanho da lista)
        eixo_x = range(1, len(lista_1) + 1)
        
        # 3. Desenhamos os PONTOS (Gráfico de Dispersão / Scatter)
        # zorder=5 faz os pontos ficarem por cima das linhas
        plt.scatter(eixo_x, lista_1, color='blue', s=100, label='Pontos da Lista 1', zorder=5)
        
        # 4. Desenhamos as LINHAS HORIZONTAIS (axhline = Axis Horizontal Line)
        # Linha da Média (Vermelha e sólida)
        plt.axhline(y=carta.media_geral, color='red', linestyle='-', linewidth=2, label=f'Média ({carta.media_geral:.2f})')
        
        # Linhas dos Limites (Verdes e tracejadas)
        plt.axhline(y=limite_superior, color='green', linestyle='--', label=f'Limite Sup ({limite_superior})')
        plt.axhline(y=limite_inferior, color='green', linestyle='--', label=f'Limite Inf ({limite_inferior})')

    # 5. Perfumaria: Deixando o gráfico bonito e fácil de ler
    plt.title("Análise de Controle - Media", fontsize=14, fontweight='bold')
    plt.xlabel("Ordem de amostras")
    plt.ylabel("Valores")
    plt.legend() # Mostra a caixinha com os significados das cores
    plt.grid(True, linestyle=':', alpha=0.6) # Coloca uma grade de fundo suave

    # 6. Salva na memória e devolve para a View (Igualzinho fizemos antes)
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    
    buffer.seek(0)
    return buffer

def grafico_amplitude(carta):
    plt.figure(figsize=(8, 6))
    # 1. Puxamos apenas a Lista "1" do seu JSON
    # Se a lista "1" não existir, pegamos uma lista vazia para não quebrar
    lista_1 = list(carta.amplitude.values())
    
    if len(lista_1) > 0:
        # 2. Fazemos os cálculos rápidos
        limite_superior = carta.lsc_amp
        limite_inferior = carta.lic_amp
        # Criamos um eixo X falso só para espalhar os pontos 
        # (vai ser: 1, 2, 3, 4, 5... dependendo do tamanho da lista)
        eixo_x = range(1, len(lista_1) + 1)
        
        # 3. Desenhamos os PONTOS (Gráfico de Dispersão / Scatter)
        # zorder=5 faz os pontos ficarem por cima das linhas
        plt.scatter(eixo_x, lista_1, color='blue', s=100, label='Pontos da Lista 1', zorder=5)
        
        # 4. Desenhamos as LINHAS HORIZONTAIS (axhline = Axis Horizontal Line)
        # Linha da Média (Vermelha e sólida)
        plt.axhline(y=carta.media_amplitude, color='red', linestyle='-', linewidth=2, label=f'Média ({carta.media_amplitude:.2f})')
        
        # Linhas dos Limites (Verdes e tracejadas)
        plt.axhline(y=limite_superior, color='green', linestyle='--', label=f'Limite Sup ({limite_superior})')
        plt.axhline(y=limite_inferior, color='green', linestyle='--', label=f'Limite Inf ({limite_inferior})')

    # 5. Perfumaria: Deixando o gráfico bonito e fácil de ler
    plt.title("Análise de controle - Amplitude", fontsize=14, fontweight='bold')
    plt.xlabel("Ordem de amostras")
    plt.ylabel("Valores")
    plt.legend() # Mostra a caixinha com os significados das cores
    plt.grid(True, linestyle=':', alpha=0.6) # Coloca uma grade de fundo suave

    # 6. Salva na memória e devolve para a View (Igualzinho fizemos antes)
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    
    buffer.seek(0)
    return buffer