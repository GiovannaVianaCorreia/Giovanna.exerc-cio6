quantidade = float(input("Quantidade de itens diferentes: "))
valorTotal = 0
quantidades = []

i = 0
while i < quantidade:
    nome = input("Nome do item: " + stri(i+1) + ": ")
    quantidade = input("Quantidade deste produto: " + stri(i+1) + ": " )
    valor unitario = input("Valor unitário deste produto: " + stri(i+1) + ": " )
    valorTotal += nota
    quantidadeDicionario = {
          "nome": nome,
          "quantidade": quantidade
    }
    quantidades.append(quantidadeDicionario)
    i += 1

print("Nome | Quantidade")
for cadaElementoDaLista in notas: 
    print("{} | {}", format(quantidade["nome"], quantidade["nome"]))