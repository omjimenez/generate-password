import random

def generate_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # caracteres = mayusculas + minusculas + simbolos + numeros

    # range 33 to 126 decimal ascii table
    characters = [chr(dec_ascii) for dec_ascii in range(33,126)]

    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    generate_password = "".join(password)
    return generate_password


def run():
    password = generate_password()

    print('\n ************************************* \n')
    print(' ******* GENERADOR DE PASSWORD *******')
    print('\n Tu nueva Password es: '+ password)
    print('\n ************************************* \n')


if __name__ == '__main__':
    run()