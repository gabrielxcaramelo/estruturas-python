print("exemplo 01 de while - enquanto\n")
senha = "54321"
leitura = " "
while (leitura != senha):
  leitura = input("digite a senha: ")
  if leitura == senha:
      print('acesso liberado')
  else:
      print('senha incorreta. tente novamente')

#--------------------------------------------#

print("\nExemplo 02 de while - enquanto\n")
contador = 0
somador = 0 
while contador <5:
  contador = contador + 1 
  valor = float(input('digite o '+str(contador)+'º valor: ' ))
  somador = somador + valor
print('soma = ',somador)

#-------------------------------------------------------#

print("\nexemplo 01 de 'for'. encontrar a soma s = 1+4+7+10+13+16+19\n")
s = 0 
for x in range(1,20,3):
  s += x
print('soma = ',s)

#--------------------------------------------------------#

print("\nExemlo 02 de 'for'. as notas de um aluno estao armazenadas em uma lista. calcular a media dessas notas ")
listas_notas = [3.4,6.6,8,9,10,9,5,8.8,4.3]
soma = 0
for nota in listas_notas:
  soma += nota
media = soma/len(listas_notas)
print('media = %.2f'%media)