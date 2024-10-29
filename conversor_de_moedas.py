from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

print()
print(f'{Fore.MAGENTA}CONVERSOR DE MOEDAS{Style.RESET_ALL}')
print()
taxa_euro = 0.16
taxa_iene = 26.79
print()
print(f'{Fore.MAGENTA}TAXAS:{Style.RESET_ALL}')
print(f'1 Euro = {Fore.GREEN}{taxa_euro} Dólar{Style.RESET_ALL}')
print(f'1 Iene = {Fore.GREEN}{taxa_iene} Dólar{Style.RESET_ALL}')
print()
valor_real = float(input('Digite o valor em reais: '))
print()
print(f'Euro: {Fore.GREEN}{(valor_real) * taxa_euro}{Style.RESET_ALL}')
print(f'Iene: {Fore.GREEN}{(valor_real) * taxa_iene}{Style.RESET_ALL}')
print()