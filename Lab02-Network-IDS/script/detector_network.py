import joblib
import pandas as pd
import os

# Caminhos dos artefatos
modelo_path = 'data/modelo_network.pkl'
encoder_path = 'data/label_encoder.pkl'

if not os.path.exists(modelo_path):
    print("❌ Erro: Modelo não encontrado. Rode o treino primeiro.")
    exit()

modelo = joblib.load(modelo_path)
le = joblib.load(encoder_path)

def testar_fluxo():
    print("\n--- 🛡️ NIDS: Simulador de Tráfego (Ajustado) ---")
    try:
        # Usando float() antes de int() para aceitar entradas como "1000.0"
        porta = int(float(input("Porta de Destino: ")))
        duracao = int(float(input("Duração (microssegundos): ")))
        pacotes = int(float(input("Total de Pacotes: ")))
        comprimento = int(float(input("Comprimento Total (Bytes): ")))
        max_len = int(float(input("Tamanho Máximo do Pacote: ")))
        pps = float(input("Pacotes por Segundo: "))
        
        print("\n--- Flags TCP (0 ou 1) ---")
        fin = int(float(input("FIN Flag Count: ")))
        psh = int(float(input("PSH Flag Count: ")))
        ack = int(float(input("ACK Flag Count: ")))

        # Lista de colunas deve ser IDÊNTICA à do treino (9 colunas)
        colunas = [
            'Destination Port', 'Flow Duration', 'Total Fwd Packets', 
            'Total Length of Fwd Packets', 'Fwd Packet Length Max', 'Flow Packets/s',
            'FIN Flag Count', 'PSH Flag Count', 'ACK Flag Count'
        ]

        # Criando a linha de dados sem a variável 'syn'
        dados = pd.DataFrame([[porta, duracao, pacotes, comprimento, max_len, pps, fin, psh, ack]], 
                             columns=colunas)

        predicao = modelo.predict(dados)
        probabilidade = modelo.predict_proba(dados)
        
        resultado = le.inverse_transform(predicao)[0]
        confianca = max(probabilidade[0]) * 100
        
        print("\n" + "="*40)
        status = "🚨 ALERTA" if resultado != "Normal Traffic" else "✅ LIMPO"
        print(f"{status} - Veredito: {resultado}")
        print(f"Confiança da IA: {confianca:.2f}%")
        print("="*40)

    except Exception as e:
        print(f"❌ Erro na entrada: {e}")

if __name__ == "__main__":
    while True:
        testar_fluxo()
        if input("\nContinuar testando? (s/n): ").lower() != 's':
            break