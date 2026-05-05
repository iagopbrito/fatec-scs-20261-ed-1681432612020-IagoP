from datetime import datetime, date

fila_1 = []
log_descartes = []

def formatar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return data.strftime("%d/%m/%Y")
    except ValueError:
        return None

def gerar_produto():
    print("\n=== Equipe 03: Entrada de Estoque ===")
    print("Missão: Simular o recebimento de mercadorias no armazém.\n")

    while True:
        id_sku_str = input("Digite o SKU (id_sku): ").strip()
        if id_sku_str.isdigit():
            id_sku = int(id_sku_str)
            break
        print("  SKU inválido. Digite apenas números.")

    while True:
        nome_produto = input("Digite o nome do produto: ").strip()
        if nome_produto:
            break
        print("  Nome não pode ser vazio.")

    while True:
        data_str = input("Digite a data de validade (DD/MM/AAAA): ").strip()
        data_validade = formatar_data(data_str)
        if data_validade:
            data_obj = datetime.strptime(data_validade, "%d/%m/%Y").date()
            if data_obj < date.today():
                produto_descarte = {
                    "id_sku": id_sku,
                    "nome_produto": nome_produto,
                    "data_validade": data_validade,
                }
                log_descartes.append(produto_descarte)
                print(f"\n  Produto vencido! Logado como Perda. Não inserido na Fila 1.")
                return None
            break
        print("  Data inválida. Use o formato DD/MM/AAAA.")

    produto = {
        "id_sku": id_sku,
        "nome_produto": nome_produto,
        "data_validade": data_validade,
    }
    fila_1.append(produto)
    saida = f"SKU: {id_sku}, Produto: {nome_produto}, Validade: {data_validade}"
    print(f"\n✔ Produto inserido na Fila 1 (Entrada de Carga):")
    print(f"  {saida}")
    return produto

def exibir_fila():
    if not fila_1:
        print("\n  Fila 1 está vazia.")
        return
    print(f"\n=== Fila 1 — Entrada de Carga ({len(fila_1)} produto(s)) ===")
    for i, p in enumerate(fila_1, start=1):
        print(f"  [{i}] SKU: {p['id_sku']}, Produto: {p['nome_produto']}, Validade: {p['data_validade']}")

def exibir_descartes():
    if not log_descartes:
        print("\n  Nenhum descarte registrado.")
        return
    print(f"\n=== Log de Descartes — Produtos Vencidos ({len(log_descartes)} produto(s)) ===")
    for i, p in enumerate(log_descartes, start=1):
        print(f"  [{i}] SKU: {p['id_sku']}, Produto: {p['nome_produto']}, Validade: {p['data_validade']} → Perda")

def main():
    while True:
        print("\n--- Menu ---")
        print("1. Adicionar produto à Fila 1")
        print("2. Visualizar Fila 1")
        print("3. Visualizar Log de Descartes")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            gerar_produto()
        elif opcao == "2":
            exibir_fila()
        elif opcao == "3":
            exibir_descartes()
        elif opcao == "4":
            print("Encerrando. Até logo!")
            break
        else:
            print("  Opção inválida.")

if __name__ == "__main__":
    main()
