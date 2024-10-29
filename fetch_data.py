import requests

from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

print()
print(f'{Fore.MAGENTA}REQUESTS{Style.RESET_ALL}')
print()

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
dados = response.json()
taxa_dolar = dados['USDBRL']['bid']
print(f'1 Dólar = {Fore.GREEN}{taxa_dolar} Real{Style.RESET_ALL}')
print()