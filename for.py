soma =0
for indice in range(0,501):
        if (indice % 2 !=0 and indice % 3 ==0):
            soma+= indice
print(f"soma: {soma}")