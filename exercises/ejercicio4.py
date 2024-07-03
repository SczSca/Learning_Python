def encontrar_primos(limite):
    '''
        Dado el limite, devolver la cantidad de numeros primos encontrados. del 2 al limite (ambos limites incluidos)
        :param limite: int. Ej: 5
        :return: 3

    '''
    primes = []
    is_prime = True
    for n in range(2,limite + 1):
        is_prime = True

        for prime in primes:
            if n % prime == 0:
                is_prime = False
                break

        primes.append(n) if is_prime else None

    print(primes)
    return len(primes)
print(encontrar_primos(100))