print("testando o comando if (digite um num menor de 18:")
valor = int(input("qual sua idade? "))
if valor < 18:
    print("voce ainda nao pode dirigir!")
#-----------------------------#
print("\n")
print("testando o comando if .. ELSE (se..senão)")
valor = int(input("qual sua idade? "))
if valor < 18:
    print("voce ainda nao pode dirigir!")
else:
    print("voce pode dirigir!")
#------------------------------------------------------
print("\n")
print("testando o comando IF..ELIF..ELSE (se..senao..senao se)")
valor = int(input("qual sua idade? "))
if valor < 6:
    print("que coisa fofa!")
elif valor < 18:
    print("voce ainda nao pode dirigir!")
elif valor > 60:
    print("voce esta na meljor idade!")
else:
    print("voce pode dirigir!")
