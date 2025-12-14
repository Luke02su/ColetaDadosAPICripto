import requests
import csv
import os
from datetime import datetime

# 1. Configuração
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
HEADERS = ['Nome', 'Símbolo', 'Preço_Atual_USD', 'Volume_24h', 'Capitalização_de_Mercado', 'Ultima_Atualizacao']
# O caminho deve apontar para o diretório de volume mapeado dentro do container
FILE_PATH = os.path.join('/app/data', 'cripto_dados.csv') 

# Parâmetros para a API (Top 5 moedas por capitalização de mercado)
PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 5,
    'page': 1,
    'sparkline': False
}

def fetch_and_process_data():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Iniciando coleta da API...")
    try:
        # 2. Requisição à API
        response = requests.get(API_URL, params=PARAMS)
        response.raise_for_status() # Lança exceção para códigos de status ruins (4xx ou 5xx)
        data = response.json()
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Dados recebidos com sucesso. Processando...")

        processed_data = []
        for coin in data:
            # 3. Tratamento dos Dados
            row = [
                coin.get('name', 'N/A'),
                coin.get('symbol', 'N/A').upper(),
                coin.get('current_price', 0.0),
                coin.get('total_volume', 0.0),
                coin.get('market_cap', 0.0),
                # Converte o timestamp para um formato legível
                datetime.fromisoformat(coin.get('last_updated').replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S')
            ]
            processed_data.append(row)
            print(f" - Processado: {row[0]}")
        
        # 4. Exportação para CSV (Usando o caminho do volume compartilhado)
        # Cria o diretório /app/data dentro do container se ele não existir
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        
        with open(FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(HEADERS)
            writer.writerows(processed_data)
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Sucesso! Arquivo CSV gerado em: {FILE_PATH}")
        print("Fim da execução do script.")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
    except Exception as e:
        print(f"Ocorreu um erro durante o processamento: {e}")

if __name__ == "__main__":
    fetch_and_process_data()