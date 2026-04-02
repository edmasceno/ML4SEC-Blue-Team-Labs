import pandas as pd
import joblib # Você pode precisar instalar: pip install joblib
from entropy_check import calcular_entropia
import os

# Simulando o carregamento do modelo (Para o lab, vamos treinar e usar na hora)
# Em um cenário real, salvaríamos o modelo treinado.
def detectar_ameaca(caminho_arquivo, modelo):
    if not os.path.exists(caminho_arquivo):
        return "Arquivo não encontrado."
    
    ent = calcular_entropia(caminho_arquivo)
    tam = os.path.getsize(caminho_arquivo)
    
    # Criar um pequeno DataFrame para a IA ler
    novo_dado = pd.DataFrame([[tam, ent]], columns=['filesize', 'entropy'])
    
    predicao = modelo.predict(novo_dado)
    probabilidade = modelo.predict_proba(novo_dado) # Mostra a "certeza" da IA
    
    status = "🚨 SUSPEITO (Possível Malware/Packer)" if predicao[0] == 1 else "✅ SEGURO"
    confianca = probabilidade[0][predicao[0]] * 100
    
    print(f"\n--- Análise de Segurança ---")
    print(f"Arquivo: {caminho_arquivo}")
    print(f"Entropia: {ent:.4f}")
    print(f"Veredito: {status}")
    print(f"Confiança da IA: {confianca:.2f}%")

