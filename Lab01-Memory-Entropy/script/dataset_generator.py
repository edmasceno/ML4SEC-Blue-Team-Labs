import os
import csv
from entropy_check import calcular_entropia

def build_dataset():
    # Definição das classes
    categorias = {
        'SAMPLES_SAFE': 0,      # 0 = Seguro
        'SAMPLES_SUSPICIOUS': 1 # 1 = Suspeito/Anômalo
    }
    
    with open('process_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['filename', 'filesize', 'entropy', 'label'])
        
        for pasta, label in categorias.items():
            if not os.path.exists(pasta): continue
            
            for arq in os.listdir(pasta):
                caminho = os.path.join(pasta, arq)
                if os.path.isfile(caminho):
                    ent = calcular_entropia(caminho)
                    tamanho = os.path.getsize(caminho)
                    writer.writerow([arq, tamanho, ent, label])
                    
    print("✅ Dataset 'process_data.csv' gerado com sucesso!")

if __name__ == "__main__":
    build_dataset()