import math
from collections import Counter

def calcular_entropia(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as f:
            dados = f.read()
        
        if not dados:
            return 0.0

        tamanho = len(dados)
        # Conta a frequência de cada byte (0-255)
        contagem_bytes = Counter(dados)
        
        entropia = 0
        for contagem in contagem_bytes.values():
            # Probabilidade de cada byte aparecer
            p_x = contagem / tamanho
            # Fórmula de Shannon: H(X) = -sum(P(xi) * log2(P(xi)))
            entropia -= p_x * math.log2(p_x)
            
        return entropia

    except FileNotFoundError:
        return "Arquivo não encontrado."

# Teste simples
if __name__ == "__main__":
    arquivo = input("Digite o caminho do arquivo para analisar: ")
    resultado = calcular_entropia(arquivo)
    print(f"Entropia: {resultado:.4f}")