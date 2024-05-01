#nome = input("Digite seu nome ")
#print("Olá ", nome, " Tudo Bem? ")
lista = [1,2,3,4,5,]
lista.pop()
print(lista)
try:
    lista.remove(6)
    print(lista)
except:
    print('não existe o número pedido')
lista1 = [1,2,3,4,5] #TUPLAS, não pode se alterado
print('Tupla ',lista1)
#del lista1
try:
    print('Tupla ',lista1)
except:
    print('lista1  foi deletada ')
print('tupla posição 2',lista1[2])

for n in lista1:
    print('n = ',n)
lista.append(12)
print('lista ',lista)
print('tamanho ',len(lista))
dicionario = {"nome":"João","idade":20}
print("nome ",dicionario["nome"])

dicionario["idade"] =40
print(dicionario["idade"])
dicionario["email"] = "eron.oliveira12@gmail.com"
print(dicionario)

dicionario.popitem()
print(dicionario)

dicionario.pop("nome")
print(dicionario)
print('''olá mundo
olá mundo
olá mundo''')

exemplo = """olá mundo
olá mundo
bem vindo ao mundo pythone"""
print(exemplo)
print(exemplo[0])
exemplo = exemplo + " Brazil" + " São Paulo"
print(exemplo)
if "Brazil" in exemplo:
    print("frase encontrada")
else:
    print("frase não encontrada")

frutas = ["limão","banana","morango"]
frutas.append("abacaxi")
frutas.append("abacate")
frutas2 =[]
for i in range(2):
    frutas.pop()
    frutas2.append(frutas[i])
print(frutas2)

print("fim")
frutas = ["limão","banana","morango"]
frutas.append("abacaxi")
for i in range(2):
    frutas.pop()
print(frutas)

dicionario = {"nome":"Joao da Silva","idade":25,"email":"joão@gmail.com"}
dicionario.popItem("email")
print(dicionario)




    


    
    
    
    




