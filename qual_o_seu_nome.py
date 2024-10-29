from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

print()
print(f'{Fore.MAGENTA}QUAL O SEU NOME{Style.RESET_ALL}')
print()

nome = input('🧐 Qual é o seu nome? ')
print(f'🙂 Meu nome é {Fore.GREEN}{nome}{Style.RESET_ALL}!')