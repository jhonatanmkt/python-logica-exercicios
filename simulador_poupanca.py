deposito = float(input("Depósito inicial: R$ "))
juros = float(input("Taxa de juros (%): ")) / 100
for mes in range(1, 25):
    deposito += deposito * juros
    print(f"Mês {mes}: R$ {deposito:.2f}")
