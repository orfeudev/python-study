
# funções py

def funcao():
    print("bloco de codigo")


funcao()

# parametros


def saudacao():
    print("Hello World!")


saudacao()


def soma(a, b):
    return a+b


def resultado():
    res = soma(3, 4)
    print(res)


resultado()

# F-string


def nome(nome):
    print(f"Nome: {nome}")


nome("Joaozinho")

# valores Default


def flor(flor='rosa', cor='vermelha'):
    print(f"A cor da {flor} é {cor}")


flor()
flor("Orquídea", "Azul")

# chamada de função posicional


def monta_build(first_item='', sec_item=0, last_item=0):
    print(f"A melhor build, em sequência, é \n\t - First-Item: {first_item}\n\t - Sec-Item: {sec_item} \n\t - Last_Item= {last_item}")


monta_build('Black Cleaver', 1975, 1983)

# função posicional respeita a ordem dos parâmetros

# função *args


def concatena(*args):
    return "Todos os argumentos são: "+", ".join(args)


print(concatena("um", "dois" , "três" , "quatro" , "cinco", "seis"))

