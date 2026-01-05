# Async Patient Data Extractor
Este é um projeto de alta performance desenvolvido em Python para a extração automatizada de dados de pacientes de sistemas web. A solução utiliza programação assíncrona para otimizar o tempo de coleta e garantir a eficiência no processamento de grandes volumes de IDs.

### Tecnologias Utilizadas

- Python 3.10+: Linguagem base do projeto.

- Asyncio & Aiohttp: Para realizar requisições HTTP concorrentes de forma ultra rápida.

- BeautifulSoup4: Para o parsing e extração precisa de informações do HTML.

- Python-dotenv: Para o gerenciamento seguro de variáveis de ambiente.

### Diferenciais Técnicos

- Processamento Assíncrono: Implementação de async/await para evitar o bloqueio do fluxo e processar múltiplos pacientes simultaneamente.

- Controle de Concorrência: Uso de asyncio.Semaphore para limitar o número de requisições simultâneas, evitando sobrecarga no servidor de destino e bloqueios de IP.

- Modularização: Divisão clara entre lógica de rede (client.py), extração (extractor.py) e persistência (writer.py).

- Segurança: Autenticação protegida via variáveis de ambiente e entrada de senha oculta no terminal.

## 1. Clonar o repositório
```
git clone https://github.com/SeuUsuario/async-patient-data-extractor.git
cd async-patient-data-extractor
```

## 2. Configurar o ambiente virtual (.venv)
```
python -m venv .venv
```

## 3. Instalar dependências
```
pip install -r requirements.txt
```

## 4. Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto com as URLs necessárias:
```
LOGIN_URL=https://exemplo.com/login
PATIENT_URL=https://exemplo.com/paciente/{}
```

## 5. Preparar os dados de entrada
Crie um arquivo ids.txt contendo o ID do paciente e a data, um por linha:
```
12345 2023-10-25
67890 2023-10-26
```

## 6. Executar
```
python main.py
```

Os dados extraídos serão salvos automaticamente no arquivo IMPORT.csv.

## 📝 Licença
Este projeto é para fins de estudo e automação de processos internos.