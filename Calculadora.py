def calcular_nivel_ranqueadas(vitorias, derrotas):
    # Calcular o saldo de Ranqueadas
    saldo_vitorias = vitorias - derrotas

    # Determinar o nível com base no saldo de vitórias
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    elif vitorias >= 101:
        nivel = "Imortal"

    # Retornar a mensagem formatada
    return f"O Herói tem um saldo de {saldo_vitorias} está no nível de {nivel}"


# Exemplo de uso da função
resultado = calcular_nivel_ranqueadas(85, 15)
print(resultado)  # Saída esperada: "O Herói tem um saldo de 70 está no nível de Ouro"
