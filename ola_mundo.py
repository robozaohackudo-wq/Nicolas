lista = []
def controle(acao):
    if acao == "remover":
        usuario = input("Digite a tarefa que deseja remover: ").strip()
        if usuario in lista:
            lista.remove(usuario)
            print(f"Você tirou {usuario} da lista")
        else:
            return "essa tarefa não existe"
    elif acao == "adicionar":
        usuario = input("Qual tarefa deseja adicionar: ").strip()
        lista.append(usuario)
        return f"Você adicionou {usuario}"
    elif acao == "listar":
        for i, n in enumerate(lista, start=1):
            print(f"{i} - {n}")
    elif acao == "sair":
        try:
            usuario = int(input("Você deseja realmente sair (aperte /1/ para sair /2/ continuar)? "))
            if usuario == 1:
                return "usuario escolheu sair"
                exit()
            elif usuario == 2:
                return "voltando"
        except ValueError:
            print("Digite apenas numeros!")
    elif acao == "salvar":
        try:
            usuario = input("Digite o arquivo para entrar nele: ")
            with open(usuario, "a", encoding="utf-8") as f:
                lista_limpa = [n.strip() + "\n" for n in lista]
                f.writelines(lista_limpa)
                print(f"guardado em {usuario}")
        except FileNotFoundError:
            print("Arquivo não foi encontrado")
    else:
        print("Erro")
while True:
    acao = input("Digite oque deseja 'remover', 'adicionar', 'salvar', 'sair' ou 'listar': ")
    print(controle(acao))
          
         
