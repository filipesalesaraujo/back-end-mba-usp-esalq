from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

print()
print(f'{Fore.MAGENTA}OPERAÇÕES MATEMÁTICAS{Style.RESET_ALL}')
print()

# Soma +
print(f'1 + 1 = {Fore.GREEN}{1+1}{Style.RESET_ALL}')

# Subtração -
print(f'3 - 2 = {Fore.GREEN}{3-2}{Style.RESET_ALL}')

# Multiplicação *
print(f'2 * 3 = {Fore.GREEN}{2*3}{Style.RESET_ALL}')

# Divisão /
print(f'10 / 2 = {Fore.GREEN}{10/2}{Style.RESET_ALL}')

# Divisão inteira //
print(f'10 // 3 = {Fore.GREEN}{10//3}{Style.RESET_ALL}')

# Resto da divisão %
print(f'10 % 3 = {Fore.GREEN}{10%3}{Style.RESET_ALL}')

# Potência **
print(f'2 ** 3 = {Fore.GREEN}{2**3}{Style.RESET_ALL}')

# Exponenciação
print(f'2³ = {Fore.GREEN}{2**3}{Style.RESET_ALL}')

# Ordem de precedência
print(f'2 + 3 * 4 = {Fore.GREEN}{2 + 3 * 4}{Style.RESET_ALL}')

# Parênteses
print(f'(2 + 3) * 4 = {Fore.GREEN}{(2 + 3) * 4}{Style.RESET_ALL}')