lista = [["0", "Cachoro Quente", "X-Salada", "X-Bancon", "Toraada simples", "refrigerante"],[0, 4.00, 4.50, 5.00, 2.50, 1.50]]
print(" ==== Ola Bem vindo ao X burgão ==== \n temos 1 ----- cachorroquente ---- 4.00 \n 2 ----- X-Salada ---- 4.50 \n 3 ----- X-Bacon ---- 5.00 \n 4 ----- Toraada simples ---- 2.00 \n 5 ------ Refrigerante ---- 1.50")


pedido = int(input("Qual seu pedido(código): "))
print("perfeito seu pedido é ", lista[0][pedido])
quantidade = int(input("Qual a quantidade: "))

valor = quantidade * lista[1][pedido]

print("perfeito seu valor a pagar sera:", "R$",valor)

