import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Carregar Dados (Lendo 1 milhão para ter mais amostras de ataques)
print("⌛ Carregando 1.000.000 de linhas do dataset...")
caminho = "data/cicids2017_cleaned.csv"
df = pd.read_csv(caminho, nrows=1000000)
df.columns = df.columns.str.strip()

# 2. Pré-processamento
le = LabelEncoder()
df['Attack Type'] = le.fit_transform(df['Attack Type'])


features = [
    'Destination Port', 'Flow Duration', 'Total Fwd Packets', 
    'Total Length of Fwd Packets', 'Fwd Packet Length Max', 'Flow Packets/s',
    'FIN Flag Count', 'PSH Flag Count', 'ACK Flag Count' 
]

X = df[features]
y = df['Attack Type']

# 3. Dividir Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinar com Pesos Balanceados (O ajuste principal)
print("🧠 Treinando modelo balanceado (isso pode demorar um pouco mais)...")
modelo_network = RandomForestClassifier(
    n_estimators=100, 
    random_state=42, 
    class_weight='balanced' # <-- Corrigindo o vício em tráfego normal
)
modelo_network.fit(X_train, y_train)

# 5. Avaliar
y_pred = modelo_network.predict(X_test)
print(f"\n🎯 Acurácia Geral: {accuracy_score(y_test, y_pred):.2f}")
print("\n📝 Relatório por Categoria de Ataque:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

# 6. Salvar artefatos na pasta data
joblib.dump(modelo_network, 'data/modelo_network.pkl')
joblib.dump(le, 'data/label_encoder.pkl')
print("\n✅ IA Re-treinada e salva em 'data/'.")