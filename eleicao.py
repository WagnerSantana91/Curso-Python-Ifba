idade = int(input("Digite uma idade: "));

if (idade < 16):
    print("Não pode votar");
elif(idade >= 18 and idade<70):
    print("Obrigatorio");
else:
    print("Facultativo");