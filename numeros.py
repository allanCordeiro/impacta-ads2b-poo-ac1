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


def conta_primos(s: list):
    s.sort()
    contador = {}
    for numero in s:
        if eh_primo(numero):
            qtd = contador.get(numero, 0)
            contador[numero] = qtd + 1

    return contador


def calcula_armstrong(n):
    separa_digito = [int(i) for i in str(n)]
    calcula = 0
    qte_digitos = len(separa_digito)
    for numero in separa_digito:
        calcula += numero ** qte_digitos
    return calcula


def eh_armstrong(n):
    calcula = calcula_armstrong(n)
    if calcula == n:
        return True
    return False


def eh_quase_armstrong(n):
    calcula = calcula_armstrong(n)
    if calcula != n:
        diff = calcula - n
        if diff == -1 or diff == 1:
            return True
    return False


def lista_armstrong(n):
    array_armstrong = []
    for item in range(1, n):
        if eh_armstrong(item):
            array_armstrong.append(item)
    return array_armstrong


def eh_perfeito(n):
    resultado = 0
    for item in range(1, n):
        if n % item == 0:
            resultado += item
    if resultado == n:
        return True
    return False


def lista_perfeitos(n):
    array_perfeitos = []
    for item in range(2, n):
        if eh_perfeito(item):
            array_perfeitos.append(item)
    return array_perfeitos

