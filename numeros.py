# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
# Allan Cordeiro dos Santos
# Email Impacta: allan.cordeiro@aluno.faculdadeimpacta.com.br

def eh_primo(n):
    teste = False
    for item in range(1, n+1):
        if n == 1:
            return False
        if n % item == 0:
            if item == 1 or item == n:
                teste = True
            else:
                return False
    return teste


def lista_primos(n):
    array_primos = []
    for item in range(2, n):
        if eh_primo(item):
            array_primos.append(item)

    return array_primos

print(lista_primos(100))