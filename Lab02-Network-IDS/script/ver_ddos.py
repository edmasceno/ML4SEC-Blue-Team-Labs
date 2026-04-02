import pandas as pd

df = pd.read_csv("data/cicids2017_cleaned.csv", nrows=1000000)
df.columns = df.columns.str.strip()

# Filtrando um exemplo real de DDoS
ddos_sample = df[df['Attack Type'] == 'DDoS'].head(1)

print("🚀 VALORES REAIS PARA TESTAR DDOS NO DETECTOR:")
colunas = [
    'Destination Port', 'Flow Duration', 'Total Fwd Packets', 
    'Total Length of Fwd Packets', 'Fwd Packet Length Max', 'Flow Packets/s',
    'FIN Flag Count', 'PSH Flag Count', 'ACK Flag Count'
]
print(ddos_sample[colunas].to_string(index=False))