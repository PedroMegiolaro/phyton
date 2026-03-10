# n1 = float (input("digite um número: "))
# n2 = float (input("digite outro número: "))
# if  n1 > n2 : 
#     print("O primeiro número é maior", n1)
# if  n1 < n2 : 
#     print("O segundo número é maior", n2)


# a = float(input("digite um número: "))
# if a >= 0 :
#     print("positivo", a)
# else : 
#     print("negativo", a)

# dia = 2
# if dia == 1 :
#     print("- ", dia, " - Domingo")
# if dia == 2 :
#     print("- ", dia, " - Segunda")
# if dia == 3 :
#     print("- ", dia, " - Terça")
# if dia == 4 :
#     print("- ", dia, " - Quarta... e assim por diante")

# salario = int(input("Digite o seu salário: "))
# if salario > 1250 :
#     aumentoMenor = salario * 1.1
#     print("Seu novo salário é: ", aumentoMenor)
# if salario < 1250 : 
#     aumentoMaior = salario * 1.15
#     print("Seu novo salário é: ", aumentoMaior)

# anoAtual = int(input("digite o ano atual: "))
# anoNasc = int(input("digite o ano de nascimento: "))
# idade = anoAtual - anoNasc
# if idade >= 18 :
#     print("você pode tirar CNH")

# idade = int(input("Quantos anos tem o carro?"))

# if idade < 3 :
#     print(("seu carro é novo"))
# else :
#         print(("seu carro é velho"))


# distancia = float(input("Digite a distancia da viagem em km: "))

# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45

# print("Preço da passagem: R$", preco)

# Programa que calcula a quantidade de latas e o custo para pintar um tanque cilíndrico

# # Dados
# pi = 3.1415

# # Entrada
# raio = float(input("Digite o raio do cilindro (m): "))
# altura = float(input("Digite a altura do cilindro (m): "))

# # Cálculo das áreas
# area_base = pi * (raio ** 2)
# perimetro = 2 * pi * raio
# area_lateral = altura * perimetro

# area_total = area_base + area_lateral

# # Cada litro cobre 3 m²
# litros_necessarios = area_total / 3

# # Cada lata tem 5 litros
# latas = litros_necessarios / 5

# # Arredondar para cima (precisa comprar lata inteira)
# import math
# latas = math.ceil(latas)

# # Definir preço unitário (decisão completa)
# if latas == 1:
#     preco_unitario = 50
# else:
#     if latas == 2:
#         preco_unitario = 48
#     else:
#         if latas == 3:
#             preco_unitario = 46
#         else:
#             preco_unitario = 45

# # Cálculo do custo total
# custo_total = latas * preco_unitario

# # Saída
# print("Área total a ser pintada:", round(area_total, 2), "m²")
# print("Quantidade de latas necessárias:", latas)
# print("Custo total: R$", round(custo_total, 2))

# precoP = int(input("Digite o preço do produto: "))
# codP = int(input("Digite o preço do codigo: "))
# if codP == 1:
#     print(precoP, "SUL")
# if codP == 2:
#     print(precoP, "NORTE")
# if codP == 3:
#     print(precoP, "LESTE")
# if codP == 4:
#     print(precoP, "OESTE")
# if codP == 6 or 5:
#     print(precoP, "NORDESTE")
# if codP == 7 or 8 or 9 :
#     print(precoP, "SUDESTE")
# if codP > 9 and codP >= 20 :
#     print(precoP, "CENTRO-OESTE")
# if codP > 24 and codP >= 30 :
#     print(precoP, "NORDESTE")
# else: 
#     print("produto importado")

# n1 = print(input("digite 1 numero"))
# n2 = print(input("digite outro numero"))
# n3 = print(input("digite mais um numero"))

# if n1 > n2 and n1 > n3 :
#     print("")
#     if n1 > n2=3 and n3 > n2 :

# if n1 > n2 and n1 > n3 :

# if n1 > n2 and n1 > n3 :

# if n1 > n2 and n1 > n3 :

# numero = int(input("Digite um número: "))

# for i in range(1, numero + 1):
#     if i % 2 != 0:
#         print(i)

# # de 1 a 50 de 1 em 1
# for i in range(1, 51):
#     print(i)

# # de 52 a 100 de 2 em 2
# for i in range(52, 101, 2):
#     print(i)

# i = 1

# while i <=100:
#     print(i)
#     if i < 50:
#         i += 1
#     else:
#         1 += 2
#         print(i)

# numero = int(input("Digite um número para ver sua tabuada: "))

# print(f"\nTabuada do {numero}:\n")
# for i in range(1, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")
    
# maior = 0

# for i in range(6):
#     numero = int(input("Digite um número: "))
    
#     if numero > maior:
#         maior = numero

# print("O maior número é:", maior)



# numero = int(input("Digite um número entre 0 e 10: "))

# while numero < 0 or numero > 10:
#     print("Valor inválido! Tente novamente.")
#     numero = int(input("Digite um número entre 0 e 10: "))

# print("Número aceito!")

# numero = int(input("Digite um número: "))

# while numero != 0 :
#     print
    
# soma = 0
# quantidade = 0

# numero = int(input("Digite um número (0 para parar): "))

# while numero != 0:
#     soma = soma + numero
#     quantidade = quantidade + 1
#     numero = int(input("Digite um número (0 para parar): "))

# if quantidade > 0:
#     media = soma / quantidade
# else:
#     media = 0

# print("Quantidade de números:", quantidade)
# print("Soma:", soma)
# print("Média:", media)


# maior = None

# for i in range(6):
#     numero = int(input(f"Digite o {i+1}º número inteiro positivo: "))
    
#     # Verifica se o número é positivo
#     if numero <= 0:
#         print("Número inválido! Digite apenas inteiros positivos.")
#         exit()
    
#     # Atualiza o maior número
#     if maior is None or numero > maior:
#         maior = numero

# print(f"O maior número digitado foi: {maior}")

# soma = 0
# quantidade = 0

# while quantidade < 10:
#     numero = int(input(f"Digite o {quantidade+1}º número: "))
#     quantidade += 1
#     soma += numero
# print("A soma dos numeros é", soma)    



# soma = 0

# while True:
#     numero = int(input("Digite um número (0 para encerrar): "))
    
#     if numero == 0:
#         break  # encerra o loop quando o usuário digita 0
    
#     soma += numero  # acumula o valor

# print(f"A soma dos números digitados é: {soma}")


n = int(input("Digite um valor inteiro positivo n: "))

if n <= 0:
    print("Erro: o valor deve ser inteiro positivo.")
else:
    soma = 0
    for i in range(1, n + 1):
        soma += 1 / i
    
    print(f"A soma S até 1/{n} é: {soma:.4f}")