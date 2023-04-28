
string = "target"

lista = list(string)

tamanho = len(lista)

for i in range(tamanho // 2):
    temp = lista[i]
    lista[i] = lista[tamanho - i - 1]
    lista[tamanho - i - 1] = temp

string_invertida = ''.join(lista)

print(string_invertida)
