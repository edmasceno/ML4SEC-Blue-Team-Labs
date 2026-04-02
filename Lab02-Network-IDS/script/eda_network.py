import pandas as pd

# Caminho do arquivo
caminho = "data/cicids2017_cleaned.csv"

print("⌛ Carregando dataset... (Como o arquivo tem 717MB, pode levar uns 30 segundos)")
# Lendo apenas as primeiras 500 mil linhas para ser mais rápido agora
df = pd.read_csv(caminho, nrows=500000) 


# Verificando os nomes reais das colunas
print("\n🔍 Lista de colunas encontradas:")
print(df.columns.tolist())

# Limpando nomes de colunas (Sempre bom garantir)
df.columns = df.columns.str.strip()

print(f"\n✅ Dataset carregado! Total de colunas: {len(df.columns)}")

# O que a IA vai tentar prever
print("\n📊 Distribuição de Tráfego (Benigno vs Ataques):")

print(df['Attack Type'].value_counts())

# Analisando as portas mais visadas
print("\n🎯 Portas de Destino mais frequentes:")
print(df['Destination Port'].value_counts().head(10))