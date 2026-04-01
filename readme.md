
# ML4SEC Blue Team Labs 🛡️🤖

Este repositório contém laboratórios práticos focados na intersecção entre Machine Learning e Defesa Cibernética (Blue Team).

## 🧪 Lab 01: Análise de Entropia de Memória para Detecção de Malware Fileless

### Objetivo
Detectar injeções de código em processos legítimos (como `lsass.exe` ou `svchost.exe`) utilizando modelos de Machine Learning treinados com dados de entropia de seções de memória.

### Estrutura do Lab
1. **Coleta:** Dump de RAM utilizando Volatility/Process Hacker.
2. **Extração:** Script Python para extrair features (Entropia, permissões de página, tamanho da seção).
3. **Análise:** Treinamento de modelo para detecção de anomalias.

### Status
[🚧] Coleta de dados e extração de telemetria.

---

em desenvolvimento...
