'''
*-------------------------------------------------------------------*
*                Fatec São Cartano do Sul                           *
*    Autor:1681432612020 - Nome: Iago Prado de Brito                *
*    Objetivo: Implementar Inserção no Fim e no Meio                *
*    Data: 03/03/2026                                               *
*-------------------------------------------------------------------*
'''

# Função para verificar se o valor já existe na lista
def valorExiste(listaCabeca, valorEntrada):
    atual = listaCabeca
    while atual is not None:
        if atual["valor"] == valorEntrada:
            return True
        atual = atual["proximo"]
    return False

# Função de Inclusão no Início
def inserirInicio(listaEntrada):
    valor = input("Digite o valor: ")
    if valorExiste(listaEntrada, valor):
        print("Erro: Código de produto duplicado.")
        return listaEntrada
    
    # O novo nó aponta para onde a lista começava
    novoNo = {"valor": valor, "proximo": listaEntrada}
    print("Inserido no início com sucesso!")
    return novoNo

# Função de Inclusão no Fim
def inserirFim(listaEntrada):
    valor = input("Digite o valor: ")
    if valorExiste(listaEntrada, valor):
        print("Erro: Código de produto duplicado.")
        return listaEntrada
    
    novoNo = {"valor": valor, "proximo": None}
    
    if listaEntrada is None:
        return novoNo
    
    # Percorre até o último nó
    atual = listaEntrada
    while atual["proximo"] is not None:
        atual = atual["proximo"]
    
    # Faz o último nó apontar para o novo nó
    atual["proximo"] = novoNo
    print("Inserido no fim com sucesso!")
    return listaEntrada

# Função de Listagem
def listar(listaRecebida):
    if listaRecebida is None:
        print("\n[Lista vazia]")
        return
    
    print("\nEstado atual da lista:")
    listaAtual = listaRecebida
    while listaAtual is not None:
        print(listaAtual["valor"], end=" -> ")
        listaAtual = listaAtual["proximo"]
    print("None")

# Função de Busca
def buscar(listaRecebida):
    argumentoPesquisa = input("Informe o argumento de pesquisa: ")
    listaAtual = listaRecebida
    posicao = 1
    encontrado = False

    while listaAtual is not None:
        if listaAtual["valor"] == argumentoPesquisa:
            print(f"Valor encontrado na posição {posicao}")
            encontrado = True
            break
        listaAtual = listaAtual["proximo"]
        posicao += 1
    
    if not encontrado:
        print("Valor não encontrado.")

# Função de Exclusão
def remover(listaEntrada):
    if listaEntrada is None:
        print("Lista vazia.")
        return None
    
    valor = input("Informe o valor para remover: ")
    
    # Caso o item a ser removido seja o primeiro
    if listaEntrada["valor"] == valor:
        print(f"Item {valor} removido.")
        return listaEntrada["proximo"]
    
    # Caso esteja no meio ou fim
    atual = listaEntrada
    while atual["proximo"] is not None:
        if atual["proximo"]["valor"] == valor:
            atual["proximo"] = atual["proximo"]["proximo"]
            print(f"Item {valor} removido.")
            return listaEntrada
        atual = atual["proximo"]
    
    print("Valor não encontrado.")
    return listaEntrada

# Menu de Interação
def menu():
    lista = None
    while True:
        print("\n--- OPERAÇÕES ---")
        print("1-Inserir no Início")
        print("2-Inserir no Fim")
        print("4-Listar")
        print("5-Remover")
        print("6-Buscar")
        print("0-Sair")
        
        opcao = input("Escolha uma operacao: ")

        if opcao == '1':
            lista = inserirInicio(lista)
        elif opcao == '2':
            lista = inserirFim(lista)
        elif opcao == '4':
            listar(lista)
        elif opcao == '5':
            lista = remover(lista)
        elif opcao == '6':
            buscar(lista)
        elif opcao == '0':
            print("Obrigado por usar o sistema!")
            break
        else:
            print("**Opcao invalida**")

# Início do programa
if __name__ == "__main__":
    print("** Bem-vindo ao programa de Lista Ligada **")
    menu()
    