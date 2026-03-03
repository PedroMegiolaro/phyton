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

precoP = int(input("Digite o preço do produto: "))
codP = int(input("Digite o preço do codigo: "))
if codP == 1:
    print(precoP, "SUL")
if codP == 2:
    print(precoP, "NORTE")
if codP == 3:
    print(precoP, "LESTE")
if codP == 4:
    print(precoP, "OESTE")
if codP == 6 or 5:
    print(precoP, "NORDESTE")
if codP == 7 or 8 or 9 :
    print(precoP, "SUDESTE")
if codP > 9 and codP >= 20 :
    print(precoP, "CENTRO-OESTE")
if codP > 24 and codP >= 30 :
    print(precoP, "NORDESTE")
else: 
    print("produto importado")
