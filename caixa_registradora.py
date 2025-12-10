precos = {1: 0.50, 2: 1.00, 3: 4.00, 5: 7.00, 9: 8.00}
total = 0
while True:
    codigo = int(input("Código (0 para sair): "))
    if codigo == 0: break
    if codigo in precos:
        total += precos[codigo] * int(input("Quantidade: "))
    else:
        print("Código inválido.")
print(f"Total: R$ {total:.2f}")
