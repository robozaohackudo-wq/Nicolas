from colorama import Fore, Back, init
init(autoreset=True)
import time
lista = []
def remover():
    time.sleep(0.5)
    for i, n in enumerate(lista, start=1):
        print(f"{i} - {n.strip()}")
        time.sleep(0.5)
        print()
    usuario = input(Fore.CYAN + "Digite a tarefa que deseja remover: ").strip()
    if usuario in lista:
        lista.remove(usuario)
        print(Fore.RED + Back.WHITE + f"Você tirou {usuario} da lista")
    else:
        print(Fore.RED + Back.WHITE + "essa tarefa não existe")
def adicionar():
    usuario = input(Fore.CYAN + "Qual tarefa deseja adicionar: ").strip()
    time.sleep(0.3)
    print()
    lista.append(usuario)
    print(f"Você adicionou {usuario}")                         
    time.sleep(0.2)
def listar():
    for i, n in enumerate(lista, start=1):
        print(f"{i} - {n}")
        time.sleep(0.5)
        print()
def sair():
    try:
        usuario = int(input(Fore.BLACK + Back.WHITE + "Você deseja realmente sair (aperte /1/ para sair /2/ continuar)? "))
        time.sleep(0.5)
        if usuario == 1:
            print("usuario escolheu sair")
            exit()
        elif usuario == 2:
            return "voltando"
    except ValueError:
        print(Fore.RED + "Digite apenas numeros!")
def salvar():
    try:
        usuario = input("Digite o arquivo para entrar nele: ")
        with open(usuario, "a", encoding="utf-8") as f:
            lista_limpa = [n.strip() + "\n" for n in lista]
            f.writelines(lista_limpa)
            return f"tudo salvo em {usuario}"
    except FileNotFoundError:
        print("Arquivo não foi encontrado")
def remover_tudo():
    lista.clear()
    return("Você removeu tudo da sua lista!")
def ler_conteudo():    
    try:
        usuario = input("Digite qual arquivo deseja abrir para ler: ")
        with open(usuario, "r", encoding="utf-8") as ler:
            conteudo = ler.readlines()
            for linha in conteudo:
                print(linha.strip()) 
    except FileNotFoundError:
        print("Esse arquivo não existe!")           

while True:
    print(Fore.BLACK + Back.WHITE + "==== Menu Interativo ====")
    time.sleep(0.2)
    print("1 - Adicionar")
    time.sleep(0.2)
    print("2 - listar")
    time.sleep(0.5)
    print("3 - salvar")
    time.sleep(0.2)
    print("4 - sair")
    time.sleep(0.2)
    print("5 - remover")
    time.sleep(0.3)
    print("6 - remover tudo")
    time.sleep(0.1)
    print("7 - ler arquivo: 'ler conteudo'")
    time.sleep(0.4)
    try:
        escolha = input("Digite oque deseja: ").strip()
        if escolha == "1":
            print(adicionar())
        elif escolha == "2":
            print(listar())
        elif escolha == "3":
            print(salvar())
        elif escolha == "4":
            print(sair())
        elif escolha == "5":
            print(remover())
        elif escolha == "6":
            print(remover_tudo())
        elif escolha == "7":
            print(ler_conteudo())
    except KeyboardInterrupt:
        print(Fore.RED + "Conexão encerrada pelo usuario")  
        exit()
            
