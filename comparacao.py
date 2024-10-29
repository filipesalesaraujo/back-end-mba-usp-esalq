from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

print()
print(f'{Fore.MAGENTA}COMPARAÇÃO{Style.RESET_ALL}')
print()

print(f'{Fore.CYAN}{"Filipe" == "Filipe"}{Style.RESET_ALL}')
print()
if 'Filipe' == 'Filipe':
    print(f'{Fore.GREEN}Filipe é igual a Filipe{Style.RESET_ALL}')
else:
    print(f'{Fore.RED}Filipe é diferente de Filipe{Style.RESET_ALL}')
print()

if 'Filipe' != 'filipe':
    print(f'{Fore.GREEN}Filipe é diferente de filipe{Style.RESET_ALL}')
else:
    print(f'{Fore.RED}Filipe é igual a filipe{Style.RESET_ALL}')
print()

if 5 > 2:
    print(f'{Fore.GREEN}5 é maior que 2{Style.RESET_ALL}')
else:
    print(f'{Fore.RED}5 não é maior que 2{Style.RESET_ALL}')
print()

if 5 < 2:
    print(f'{Fore.RED}5 é menor que 2{Style.RESET_ALL}')
else:
    print(f'{Fore.GREEN}5 não é menor que 2{Style.RESET_ALL}')
print()