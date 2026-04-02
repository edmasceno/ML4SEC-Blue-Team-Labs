# ML4SEC - Blue Team Labs 🛡️🤖

Repositório dedicado ao estudo e desenvolvimento de soluções de **Machine Learning aplicadas à Defesa Cibernética (Blue Team)**. O objetivo é documentar a criação de modelos para detecção de anomalias, análise de ameaças e automação de processos de SOC.

---

## 🧪 Laboratórios Disponíveis

### 1. [Lab 01: Detecção de Malwares Fileless via Entropia](./Lab01-Memory-Entropy/)
Identificação de executáveis ofuscados e *packers* utilizando o algoritmo **Random Forest** e análise de **Entropia de Shannon**.
* **Status:** ✅ Concluído
* **Acurácia:** 100%
* **Destaque:** Implementação de pipeline completa de extração de telemetria bruta e treinamento de modelo supervisionado.

### 2. [Lab 02: Network IDS - Detecção de DDoS e Port Scanning](./Lab02-Network-IDS/)
NIDS (Network Intrusion Detection System) treinado com o dataset **CICIDS2017** para identificação de ataques volumétricos e sondagem.
* **Status:** ✅ Concluído
* **Acurácia:** 100% (DDoS) / 99% (Geral)
* **Destaque:** Engenharia de atributos focada em **TCP Flags** e tratamento de desbalanceamento de classes com `Random Forest (Balanced)`.

---

## 🛠️ Tech Stack & Ferramentas
- **Linguagem:** Python 3.x
- **Data Science:** Pandas, Scikit-Learn, Joblib
- **Cybersecurity:** Análise de Memória, Cálculo de Entropia, Engenharia de Malware
- **Versionamento:** Git & GitHub

---
*Este repositório documenta a evolução técnica em Cybersecurity e Ciência de Dados Aplicada.*
