'''
*-------------------------------------------------------------------*
*                Fatec São Cartano do Sul                           *
*    Autor: 1681432612020 - Nome: Iago Prado de Brito               *
*    Objetivo: Explorando a Anatomia da Árvore Binária              *
*    Data: 12/05/2026                                               *
*-------------------------------------------------------------------*
'''

from collections import deque


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def analisar_arvore(self, valor_busca):
        print("=" * 55)
        print("       ANÁLISE GERAL DA ÁRVORE BINÁRIA DE BUSCA")
        print("=" * 55)

        if self.raiz is None:
            print("\nÁrvore vazia.")
            return

        print(f"\n[RAIZ] Valor: {self.raiz.valor}  |  ID: {id(self.raiz)}")

        print("\n[NÓS INTERNOS] (possuem pelo menos 1 filho):")
        self.imprimir_nos_internos()

        print("\n[NÓS EXTERNOS / FOLHAS] (grau zero):")
        self.imprimir_folhas()

        print("\n[ORGANIZAÇÃO POR NÍVEIS]:")
        self.imprimir_niveis()

        print("\n" + "=" * 55)
        print(f"   DIAGNÓSTICO ESPECÍFICO → nó buscado: {valor_busca}")
        print("=" * 55)

        no_alvo = self._buscar(self.raiz, valor_busca)
        if no_alvo is None:
            print(f"\nValor {valor_busca} não encontrado na árvore.")
            return

        grau = (1 if no_alvo.esq else 0) + (1 if no_alvo.dir else 0)
        print(f"\n[GRAU] Nó {valor_busca} possui {grau} filho(s).")

        print(f"\n[ANCESTRAIS] Caminho de {valor_busca} até a raiz:")
        self.imprimir_ancestrais(valor_busca)

        print(f"\n[DESCENDENTES] Todos os nós abaixo de {valor_busca}:")
        self.imprimir_descendentes(valor_busca)

        print(f"\n[ALTURA]       do nó {valor_busca}: {self.calcular_altura(no_alvo)}")
        print(f"[PROFUNDIDADE] do nó {valor_busca}: {self.calcular_profundidade(valor_busca)}")
        print(f"[ID/ENDEREÇO]  do nó {valor_busca}: {id(no_alvo)}")
        print("=" * 55)

    def imprimir_nos_internos(self):
        resultado = []
        self._nos_internos_rec(self.raiz, resultado)
        for no in resultado:
            filhos = []
            if no.esq:
                filhos.append(f"esq={no.esq.valor}")
            if no.dir:
                filhos.append(f"dir={no.dir.valor}")
            print(f"  Nó {no.valor} → filhos: {', '.join(filhos)}")

    def _nos_internos_rec(self, no, lista):
        if no is None:
            return
        if no.esq or no.dir:
            lista.append(no)
        self._nos_internos_rec(no.esq, lista)
        self._nos_internos_rec(no.dir, lista)

    def imprimir_folhas(self):
        resultado = []
        self._folhas_rec(self.raiz, resultado)
        print("  " + ", ".join(str(no.valor) for no in resultado))

    def _folhas_rec(self, no, lista):
        if no is None:
            return
        if no.esq is None and no.dir is None:
            lista.append(no)
        self._folhas_rec(no.esq, lista)
        self._folhas_rec(no.dir, lista)

    def imprimir_niveis(self):
        if self.raiz is None:
            return
        fila = deque([(self.raiz, 0)])
        nivel_atual = -1
        linha = []
        while fila:
            no, nivel = fila.popleft()
            if nivel != nivel_atual:
                if linha:
                    print(f"  Nível {nivel_atual}: {', '.join(linha)}")
                linha = []
                nivel_atual = nivel
            linha.append(str(no.valor))
            if no.esq:
                fila.append((no.esq, nivel + 1))
            if no.dir:
                fila.append((no.dir, nivel + 1))
        if linha:
            print(f"  Nível {nivel_atual}: {', '.join(linha)}")

    def calcular_altura(self, no):
        if no is None:
            return -1
        return 1 + max(self.calcular_altura(no.esq), self.calcular_altura(no.dir))

    def calcular_profundidade(self, valor):
        return self._prof_rec(self.raiz, valor, 0)

    def _prof_rec(self, no, valor, prof):
        if no is None:
            return -1
        if no.valor == valor:
            return prof
        if valor < no.valor:
            return self._prof_rec(no.esq, valor, prof + 1)
        return self._prof_rec(no.dir, valor, prof + 1)

    def imprimir_ancestrais(self, valor):
        ancestrais = []
        self._ancestrais_rec(self.raiz, valor, ancestrais)
        if ancestrais:
            print("  " + " → ".join(str(a.valor) for a in ancestrais))
        else:
            print("  (é a raiz, sem ancestrais)")

    def _ancestrais_rec(self, no, valor, lista):
        if no is None:
            return False
        if no.valor == valor:
            return True
        if self._ancestrais_rec(no.esq, valor, lista) or \
                self._ancestrais_rec(no.dir, valor, lista):
            lista.insert(0, no)
            return True
        return False

    def imprimir_descendentes(self, valor):
        no_alvo = self._buscar(self.raiz, valor)
        if no_alvo is None:
            print("  (nó não encontrado)")
            return
        desc = []
        self._desc_rec(no_alvo.esq, desc)
        self._desc_rec(no_alvo.dir, desc)
        if desc:
            print("  " + ", ".join(str(d.valor) for d in desc))
        else:
            print("  (folha — sem descendentes)")

    def _desc_rec(self, no, lista):
        if no is None:
            return
        lista.append(no)
        self._desc_rec(no.esq, lista)
        self._desc_rec(no.dir, lista)

    def _buscar(self, no, valor):
        if no is None:
            return None
        if no.valor == valor:
            return no
        if valor < no.valor:
            return self._buscar(no.esq, valor)
        return self._buscar(no.dir, valor)
