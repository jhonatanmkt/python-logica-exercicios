velocidade = float(input("Velocidade do carro (km/h): "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Multado! Valor: R$ {multa:.2f}")
else:
    print("Dentro do limite.")
