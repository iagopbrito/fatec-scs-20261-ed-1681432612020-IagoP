'''
*-------------------------------------------------------------------*
*                Fatec São Cartano do Sul                           *
*    Autor:1681432612020 - Nome: Iago Prado de Brito                *
*    Objetivo: Trabalhar o básico de Python                         *
*    Data: 24/02/2026                                               *
*-------------------------------------------------------------------*
'''
  
catalogo = {}

def adicionar_files(id_filme, titulo, diretor):
    if id_filme in catalogo:
        print("ID já foi cadastrado\n")
    else:
        catalogo[id_filme] = {
            "Titulo": titulo,
            "Diretor": diretor
        }


def buscar_filme(id_filme):
    if id_filme in catalogo: 
        print(catalogo.get(id_filme))    
    else: 
        print("Erro ao buscar o filme desejado\n")
    

def remover_filme(id_filme):
    if id_filme in catalogo: 
        catalogo.pop(id_filme)
    else:
        print("Erro ao remover\n")


def listar_todos():
    if not catalogo:
        print("\nO catalogo está vazio\n")
    else: 
        print("\n--- Listagem de Filmes ---\n")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Titulo: {dados['titulo']} | Diretor: {dados['diretor']}")

r = 0 
while r != 5:
    r = int(input(
        "Menu do cátlogo:\n" \
        "1: Adicionar Filme no catálogo\n" \
        "2: Buscar Filme do catálogo\n" \
        "3: Remover Filme do catálogo\n" \
        "4: Listar Todos Filmes\n" \
        "5: Sair\n"))
    match r:
        case 1: 
                titulo = input("Insira o Titulo do filme\n")
                id_filme = input("Insira o ID do filme\n")
                diretor = input("Insira o Diretor do filme\n")
                adicionar_files(id_filme, titulo, diretor)

        case 2: 
                id_filme = input("Insira o ID do filme para buscar\n")
                buscar_filme(id_filme)

        case 3:
                id_filme = input("Insira o ID do filme para remove-lo\n")
                remover_filme(id_filme)

        case 4:
                listar_todos()
    





    
    
