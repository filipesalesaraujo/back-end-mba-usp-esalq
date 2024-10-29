from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

print()
print(f'{Fore.MAGENTA}TIPOS DE DADOS{Style.RESET_ALL}')
print()
# Str
idade = '33'
print(f'{idade} => type: {Fore.GREEN}{type(idade)}{Style.RESET_ALL}')

# Str para Int
idade = int(idade)
print(f'{idade} => type: {Fore.GREEN}{type(idade)}{Style.RESET_ALL}')

# Int + 2
idade = idade + 2
print(f'{idade} => type: {Fore.GREEN}{type(idade)}{Style.RESET_ALL}')

# Bool
casado = True
print(f'{casado} => type: {Fore.GREEN}{type(casado)}{Style.RESET_ALL}')

# Float
altura = 1.75
print(f'{altura} => type: {Fore.GREEN}{type(altura)}{Style.RESET_ALL}')

# List
amigos = ['Ana', 'Carlos', 'Maria']
print(f'{amigos} => type: {Fore.GREEN}{type(amigos)}{Style.RESET_ALL}')