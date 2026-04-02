import os
import csv
from entropy_check import calcular_entropia # Importa a função que você já testou!

def gerar_dataset(pasta_alvo, label, nome_csv):
    arquivos = os.listdir(pasta_alvo)
    
    with open(nome_csv, 'a', newline='') as f:
        writer = csv.writer(f)
        # Se o arquivo estiver vazio, escreve o cabeçalho
        if f.tell() == 0:
            writer.writerow(['nome_arquivo', 'tamanho_bytes', 'entropia', 'target'])
        
        for arq in arquivos:
            caminho = os.path.join(pasta_alvo, arq)
            if os.path.isfile(caminho):
                ent = calcular_entropia(caminho)
                tamanho = os.path.getsize(caminho)
                # target 0 = Seguro, target 1 = Suspeito
                writer.writerow([arq, tamanho, ent, label])

# Exemplo de uso:
# gerar_dataset('C:/Windows/System32', 0, 'meu_dataset.csv')