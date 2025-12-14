# 🚀 Pipeline de Dados: Docker, Python e Power BI (Criptomoedas)

[![Python](https://img.shields.io/badge/Processamento-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Containerização-Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Power BI](https://img.shields.io/badge/Visualização-Power_BI-F2C811?logo=power-bi&logoColor=black)](https://powerbi.microsoft.com/)

--- 

## 💡 Visão Geral do Projeto

Este projeto demonstra um fluxo de trabalho moderno de Extração, Transformação e Carregamento (ETL) de dados, utilizando um **container Docker** como ambiente isolado para executar o pipeline em Python. O resultado final é exportado como um arquivo CSV para o sistema Host e, posteriormente, transformado e visualizado no Power BI.

--

### Fluxo do Pipeline

1.  **Docker Compose:** Gerencia a construção da imagem e inicia o container.
2.  **Python Script:** Executa a requisição à API CoinGecko.
3.  **Processamento:** Os dados são tratados e formatados.
4.  **Persistência:** O arquivo `cripto_dados.csv` é salvo no volume mapeado (`./data`).
5.  **Visualização:** O CSV é importado no Power BI.

---

## ⚙️ API Utilizada

* **Nome:** CoinGecko API (v3)
* **Endpoint:** `https://api.coingecko.com/api/v3/coins/markets`
* **Dados Coletados:** Informações das 5 principais criptomoedas por capitalização de mercado (Preço, Volume 24h, Capitalização, etc.).

---

## 📁 Estrutura do Repositório
```
docker-data-pipeline/
├── data/                       # Diretório de Output (CSV será salvo aqui)
├── script_api.py               # Script Python de coleta, tratamento e exportação
├── Dockerfile                  # Define a imagem Docker (ambiente Python e dependências)
├── docker-compose.yml          # Definição do serviço para orquestração
└── README.md                   # Este arquivo de documentação
```

---

## 🛠️ Instruções de Execução

O `docker-compose.yml` automatiza a construção da imagem, a criação do container e a montagem do volume (`./data:/app/data`) usando um único comando.

### Pré-requisitos

---

Certifique-se de ter o **Docker Desktop** (ou Docker Engine) e o **Docker Compose** instalados e rodando.

---

### Passos de Execução

1.  **Ajustar Permissões (Evitando o Erro 13):**
    Para garantir que o container possa salvar o CSV no seu sistema Host (evitando o erro `Permission denied`), crie a pasta de output e garanta que ela tenha permissões de escrita:
    ```bash
    mkdir -p data && sudo chmod 777 data
    ```

2.  **Executar o Pipeline Completo:**
    O comando abaixo irá ler o `docker-compose.yml`, construir a imagem e iniciar o container, executando o script Python.
    ```bash
    docker compose up --build
    ```
    *O processo será concluído quando o log mostrar: "Sucesso! Arquivo CSV gerado em: /app/data/cripto_dados.csv".*

3.  **Finalizar e Limpar:**
    Após a execução bem-sucedida, use este comando para parar e remover o container e a rede criada.
    ```bash
    docker compose down
    ```

---

## 📊 Visualização de Dados (Power BI)

Após a execução, o arquivo `cripto_dados.csv` estará disponível na pasta `./data` para ser importado e analisado no Power BI.

O dashboard foi criado para apresentar as informações processadas de forma clara, contendo:
* **Tabela:** Detalhe das 5 criptomoedas.
* **Gráfico:** Comparação do Preço Atual por Nome.
* **Cartão de Destaque:** Valor total da Capitalização de Mercado.

---

### **🖼️ DASHBOARD DO POWER BI**

<img width="1280" height="720" alt="image" src="https://github.com/user-attachments/assets/9f5232b8-a00c-4a03-b590-3e7cf1947e15" />




