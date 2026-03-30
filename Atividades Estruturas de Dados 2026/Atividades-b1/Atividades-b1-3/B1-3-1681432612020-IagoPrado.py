'''
*-------------------------------------------------------------------*
*                Fatec São Cartano do Sul                           *
*    Autor:1681432612020 - Nome: Iago Prado de Brito                *
*    Objetivo:  Simulador de Calculadora HP12c (Pilha RPN)          *
*    Data: 27/03/2026                                               *
*-------------------------------------------------------------------*
'''
  
# A solução deve implementar obrigatoriamente quatro memórias: X, Y, Z e T.
# O display reflete o valor contido em X.
pilha = [0.0, 0.0, 0.0, 0.0] 

def exibir_pilha(operacao):
    print(f"\nApós: {operacao}")
    print(f"T: {pilha[0]}")
    print(f"Z: {pilha[1]}")
    print(f"Y: {pilha[2]}")
    print(f"X: {pilha[3]} ===== Display")
    print("=" * 25)

def processar_hp12c(expressao_rpn):
    # Split() divide uma string em uma lista de substrings
    pedaco = expressao_rpn.split() 
    
    for item in pedaco:
        # Se for um número
        # replace() substitui uma parte por outra
        if item.replace('.', '', 1).isdigit():
            # "Sobe" a pilha: o que estava em Z vai para T, Y para Z, X para Y
            pilha[0] = pilha[1] # Z em T
            pilha[1] = pilha[2] # Y em Z
            pilha[2] = pilha[3] # X em Y
            pilha[3] = float(item) # Novo número entra no X
            
        # Se for um operador
        elif item in "+-*/":
            x = pilha[3]
            y = pilha[2]
            
            if item == "+": resultado = y + x
            elif item == "-": resultado = y - x
            elif item == "*": resultado = y * x
            elif item == "/": resultado = y / x
            
            # "Desce" a pilha após a conta
            pilha[3] = resultado  # Resultado vai para o X
            pilha[2] = pilha[1]   # Z para Y
            pilha[1] = pilha[0]   # T para Z

            
        exibir_pilha(item)

def converter_para_infixa(expressao):
    auxiliar = []
    for item in expressao.split():
        if item not in "+-*/":
            auxiliar.append(item)
        else:
            v2 = auxiliar.pop()
            v1 = auxiliar.pop()
            nova_frase = f"({v1} {item} {v2})"
            auxiliar.append(nova_frase)
    return auxiliar[0]


entrada = input("Digite a expressão RPN (ex: 5 1 2 + 4 * + 3 -): ")

processar_hp12c(entrada)
resultado_final = converter_para_infixa(entrada)

print(f"\nO resultado da expressão algébrica {resultado_final} é: {pilha[3]}")