import pandas as pd

# Carregar uma parte do dataset
df = pd.read_csv("data/cicids2017_cleaned.csv", nrows=1000000)
df.columns = df.columns.str.strip()

# Filtrar apenas Port Scanning
scans = df[df['Attack Type'] == 'Port Scanning'].head(3)

print("🔍 EXEMPLOS REAIS DE PORT SCANNING :")
print("-" * 50)

# Selecionar as mesmas colunas que usei no treino
colunas = ['Destination Port', 'Flow Duration', 'Total Fwd Packets', 
           'Total Length of Fwd Packets', 'Fwd Packet Length Max', 'Flow Packets/s']

print(scans[colunas].to_string(index=False))