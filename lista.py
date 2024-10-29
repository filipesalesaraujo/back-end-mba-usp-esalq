from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

print()
print(f'{Fore.MAGENTA}LISTA{Style.RESET_ALL}')
print()

numeros = [1, 2, 3, 4, 5]

print(f'{Fore.CYAN}{numeros}{Style.RESET_ALL}')

# Primeiro elemento da lista
print(f'Primeiro elemento: {Fore.GREEN}{numeros[0]}{Style.RESET_ALL}')

# Último elemento da lista
print(f'Último elemento: {Fore.GREEN}{numeros[-1]}{Style.RESET_ALL}')

# Removendo o elemento da lista
numeros.remove(3)
print(f'Lista após remover o 3: {Fore.CYAN}{numeros}{Style.RESET_ALL}')

# Para cada elemento da lista
print(f'{Fore.YELLOW}Elementos da lista:{Style.RESET_ALL}')
for numero in numeros:
    print(f'{Fore.BLUE}{numero}{Style.RESET_ALL}')

# Se o número 2 está na lista
if 2 in numeros:
    print(f'{Fore.GREEN}O número 2 está na lista{Style.RESET_ALL}')
else:
    print(f'{Fore.RED}O número 2 não está na lista{Style.RESET_ALL}')