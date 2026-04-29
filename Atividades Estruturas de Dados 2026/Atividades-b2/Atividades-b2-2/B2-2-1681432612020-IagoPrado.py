
'''
*-------------------------------------------------------------------*
*                Fatec São Cartano do Sul                           *
*    Autor:1681432612020 - Nome: Iago Prado de Brito                *
*    Objetivo: Gerenciamento de buffer de impressão                 *
*    Data: 28/04/2026                                               *
*-------------------------------------------------------------------*
'''


fila_adm = []
fila_aluno = []

def adicionar_adm():
    nome = input("Nome do arquivo ADM: ")
    paginas = int(input("Total de páginas: "))
    documento = [nome, paginas]
    fila_adm.append(documento)
    print("Arquivo da Secretaria adicionado!")

def adicionar_aluno():
    nome = input("Nome do arquivo Aluno: ")
    paginas = int(input("Total de páginas: "))
    documento = [nome, paginas]
    fila_aluno.append(documento)
    print("Arquivo do Aluno adicionado!")

def consumir_fila():
    if len(fila_adm) > 0:
        doc = fila_adm.pop(0)
        print("Imprimindo documento ADM:", doc[0])
    elif len(fila_aluno) > 0:
        doc = fila_aluno.pop(0)
        print("Imprimindo documento Aluno:", doc[0])
    else:
        print("Nenhum documento para imprimir.")

def listar_estado():
    print("\n--- STATUS ---")
    print("Fila Secretaria:", len(fila_adm), "doc(s)")
    print("Fila Alunos:", len(fila_aluno), "doc(s)")
    print("--------------\n")

def reorganizar():
    fila_adm.sort()
    fila_aluno.sort()
    print("Filas reorganizadas por nome de arquivo.")

while True:
    print("1 - Adicionar Aluno")
    print("2 - Adicionar ADM")
    print("3 - Imprimir")
    print("4 - Status")
    print("5 - Reorganizar")
    print("0 - Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        adicionar_aluno()
    elif opcao == "2":
        adicionar_adm()
    elif opcao == "3":
        consumir_fila()
    elif opcao == "4":
        listar_estado()
    elif opcao == "5":
        reorganizar()
    elif opcao == "0":
        break
    else:
        print("Invalido!")
