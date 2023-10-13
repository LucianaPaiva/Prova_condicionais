# Primeiro, solicita a velocidade do veiculo
velocidade = float(input("Digite a velocidade do carro (em km/h): "))

# defina o limite de velocidade 
limite = 80

if velocidade > limite:
    # Calcula a quantidade de km acima do limite
    km_excedente = velocidade - limite

    # Valor da multa por cada km acima do limite
    valor_por_km = 20.0

    # Valor da multa
    valor_multa = km_excedente * valor_por_km

    # Mensagem final
    print(f"Você foi multado! Sua velocidade excedeu em {km_excedente} km/h o limite de {limite} km/h.")
    print(f"O valor da multa é de R${valor_multa:.2f}")
else:
    print("Velocidade dentro do limite permitido. Não houve multa.")

