# =================== IMPORTS ===================

from random import choice
import re
from colorama import Fore, Back, Style

#=========== TEMA 1: INSTRUMENTOS ===========

with open ('instrumentos.txt') as instrumentos:
    linhas = instrumentos.read()
    lista_instrumentos = linhas.split('\n')

#=========== TEMA 3: COMIDAS ===========

with open ('comidas.txt') as comidas:
    linhas = comidas.read()
    lista_comidas = linhas.split('\n')

#=========== TEMA 3: PAÍSES ===========

with open ('paises.txt') as paises:
    linhas = paises.read()
    lista_paises = linhas.split('\n')

#=========== TEMA 4: ALEATÓRIO ===========

with open ('aleatorio.txt') as aleatorio:
    linhas = aleatorio.read()
    lista_aleatorio = linhas.split('\n')


#=================== VARIÁVEIS GLOBAIS ===================



def forca():
    if chance == 0:
        print("__________")
        print("|         |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("Qual é a palavra?", "".join(resposta))

    elif chance == 1:
        print("__________")
        print("|         |")
        print("|         O")   
        print("|")
        print("|")
        print("|")
        print("Qual é a palavra?", "".join(resposta))

    elif chance == 2:
        print("__________")
        print("|         |")
        print("|         O")   
        print("|         |")
        print("|")
        print("|")
        print("Qual é a palavra?", "".join(resposta))

    elif chance == 3:
        print("__________")
        print("|         |")
        print("|         O")   
        print("|        /|")
        print("|")
        print("|")
        print("Qual é a palavra?", "".join(resposta))

    elif chance == 4:
        print("__________")
        print("|         |")
        print("|         O")   
        print("|        /|\\")
        print("|")
        print("|")
        print("Qual é a palavra?", "".join(resposta))

    elif chance == 5:
        print("__________")
        print("|         |")
        print("|         O")   
        print("|        /|\\")
        print("|        /")
        print("|")
        print("Qual é a palavra?", "".join(resposta))

    elif chance == 6:
        print("__________")
        print("|         |")
        print("|         O")   
        print("|        /|\\")
        print("|        / \\")
        print("|")
        print("Qual é a palavra?", "".join(resposta))

#=================== JOGO DA FORCA ===================

print(f'''   ___                            _           __                           
  |_  |                          | |         / _|                          
    | |  ___    __ _   ___     __| |  __ _  | |_   ___   _ __   ___   __ _ 
    | | / _ \  / _` | / _ \   / _` | / _` | |  _| / _ \ | '__| / __| / _` |
/\__/ /| (_) || (_| || (_) | | (_| || (_| | | |  | (_) || |   | (__ | (_| |
\____/  \___/  \__, | \___/   \__,_| \__,_| |_|   \___/ |_|    \___| \__,_|
                __/ |                                                      
               |___/                                                       
''')


while True:
    entrada_usuario  = input(f'Por favor, digite seu nome: ')
    print('')

    if re.match(r'^[a-zA-Z]+$', entrada_usuario):
        break
    else:
        print(f'{Fore.RED}Insira um caractere válido.{Style.RESET_ALL}')

print(f'Olá, {entrada_usuario.upper()}!')
print('')

while True:
    intro = input(f'Você sabe como jogar o jogo da forca? [S/N]: ').upper()

    if intro == "S" :
        print('')
        print('||============================================||')
        print('||        Muito bem, vamos continuar!         ||')
        print('||============================================||')
        break
    elif intro == "N":
        print('')
        print('=============================================')
        print(f'Deixa eu te explicar como o jogo da forca funciona!')
        print('')
        print(f'Na próxima etapa, você poderá escolher um dos temas disponíveis na biblioteca, e a partir dele você receberá uma palavra para adivinhar.')
        print(f'Você terá o total de 7 chances para tentar acertar a palavra secreta, mas não se preocupe, todas as letras que você sugerir serão mostradas na tela!')
        print(f'O jogo termina quando você acertar a palavra. Mas caso perca, sempre há a oportunidade de tentar uma palavra nova!')
        print(f'')
        print(f'Vamos lá!')
        print('=============================================')
        break
    else:
        print(f'{Fore.RED}Insira um caractere válido.{Style.RESET_ALL}')     
    
print('')
print(f'Atualmente, essa versão do jogo da forca disponibiliza os temas: {Fore.YELLOW}Instrumentos musicais{Style.RESET_ALL}, {Fore.YELLOW}comidas{Style.RESET_ALL} e {Fore.YELLOW}países{Style.RESET_ALL}.')
print(f'Se preferir, você também pode optar pelo {Fore.YELLOW}modo aleatório!{Style.RESET_ALL}')
print(f'')

while True:

#============== Variáveis ==============

    chance = 0
    erros = 6
    letras_usadas = []

#=======================================

    while True:
        tema = input(f'Qual tema você deseja jogar agora? {Fore.YELLOW}[INSTRUMENTOS | COMIDAS | PAÍSES | ALEATÓRIO]{Style.RESET_ALL}: ').upper()
        if tema == 'instrumentos'.upper():
            print(f'Você escolheu o tema "{Fore.YELLOW}{tema.upper()}{Style.RESET_ALL}".')
            palavra = choice(lista_instrumentos).upper()
            resposta = ['_'] * len(palavra)
            break
        elif tema == 'comidas'.upper():
            print(f'Você escolheu o tema "{Fore.YELLOW}{tema.upper()}{Style.RESET_ALL}".')
            palavra = choice(lista_comidas).upper()
            resposta = ['_'] * len(palavra)
            break
        elif tema == 'paises'.upper() or tema == 'países'.upper():
            print(f'Você escolheu o tema "{Fore.YELLOW}{tema.upper()}{Style.RESET_ALL}".')
            palavra = choice(lista_paises).upper()
            resposta = ['_'] * len(palavra)
            break
        elif tema == 'aleatorio'.upper() or tema == 'aleatório'.upper():
            print(f'Você escolheu o tema "{Fore.YELLOW}{tema.upper()}{Style.RESET_ALL}".')
            palavra = choice(lista_aleatorio).upper()
            resposta = ['_'] * len(palavra)
            break
        else:
            print(f'{Fore.RED}Insira uma opção válida.{Style.RESET_ALL}')
    forca()
    
    while chance < erros and "".join(resposta) != palavra:
        letra = input('Insira o seu palpite: ').upper()
        if letra in letras_usadas:
            print(f'{Fore.RED}Você já tentou essa letra, tente novamente.{Style.RESET_ALL}')
            continue
        elif len(letra) > 1:
            print(f'{Fore.RED}Por favor, tente apenas uma letra por vez.{Style.RESET_ALL}')
            continue
        elif not letra.isalpha():
            print(f'{Fore.RED}Por favor, utilize apenas letras de A a Z.{Style.RESET_ALL}')
            continue
        letras_usadas.append(letra) 
        if letra in palavra:
            print(f'{Fore.GREEN}Parabéns, você acertou!{Style.RESET_ALL}')
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    resposta[i] = letra
        else:
            print(f'{Fore.RED}Sinto muito, você errou. Tente novamente!{Style.RESET_ALL}')
            print(f'Você ainda tem {erros - chance} tentativas.')
            chance += 1
        forca()
        print(f'Seus palpites até agora: {Fore.YELLOW}{",".join(letras_usadas)}{Style.RESET_ALL}.')

    if chance == erros and chance > 0:
        print(f'{Fore.RED}Sinto muito, {entrada_usuario}! Você perdeu a partida.{Style.RESET_ALL}')    
    else:
        print(f'{Fore.GREEN}Parabéns, {entrada_usuario}, você ganhou a partida!{Style.RESET_ALL}')
        print(f'A palavra era: {Fore.YELLOW}{palavra}{Style.RESET_ALL}')
        print(f'')

#===================== RECOMEÇAR JOGO ===============================
    reset = input(f'Deseja jogar novamente? [S/N]: ').upper()
    while reset not in ["S","N"]:
        print('Insira somente S ou N.')
        reset = input(f'Deseja jogar novamente? [S/N]: ').upper()

        
    if reset == "S":
        continue
    elif reset == "N":
        break
print('''
||=========================================|| 
||                                         || 
||               GAME OVER!                || 
|| Se mudar de ideia, reinicie o terminal. || 
||                                         || 
||=========================================||''')