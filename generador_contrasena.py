import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_randon = random.choice(caracteres)
        contrasena.append(caracter_randon)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()

    print('\n ************************************* \n')
    print(' ******* GENERADOR DE PASSWORD *******')
    print('\n Tu nueva Password es: '+ contrasena)
    print('\n ************************************* \n')


if __name__ == '__main__':
    run()