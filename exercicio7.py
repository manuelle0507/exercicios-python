#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

if __name__ == '__main__':

    print("informe o comprimento do quadrado")
    quadrado = float(input())
    area = quadrado*quadrado

    area = area*2
    print(f" o dobro da medida da area é: {area} ")

