valor = 50
if valor > 100:
    print("Alto")
else:
    print("Baixo")

num = 10
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

idade = 13
acompanhado = False

if idade < 18:
    if acompanhado:
        print("Menor de idade, mas está acompanhado.")
    else:
        print("Menor de idade e desacompanhado.")
else:
    print("Maior de idade.")