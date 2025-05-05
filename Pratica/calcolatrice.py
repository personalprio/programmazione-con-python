def addizione(x, y):
    z = x + y
    return z


def sottrazione(x, y):
    z = x - y
    return z


def moltiplicazione(x, y):
    z = x * y
    return z


def divisione(x, y):
    z = x / y
    return z


def main():
    while True:
        try:
            a = float(input("Inserisci il primo numero: "))
            b = float(input("Inserisci il secondo numero: "))
            break
        except ValueError:
            print("Devi inserire un numero")

    print("Quale operazione vuoi eseguire?")

    while True:
        try:
            operazione = int(
                input(
                    "(1 - Addizione, 2 - Sottrazione, 3 - Moltiplicazione, 4 - Divisione): "
                )
            )
            match operazione:
                case 1 | 2 | 3 | 4:
                    break
                case _:
                    print("Devi inserire un numero da 1 a 4")
                    continue
        except ValueError:
            print("Devi inserire un numero da 1 a 4")

    if operazione == 1:
        risultato = addizione(a, b)
        print(f"La somma è: {risultato}")
    elif operazione == 2:
        risultato = sottrazione(a, b)
        print(f"La sottrazione è: {risultato}")
    elif operazione == 3:
        risultato = moltiplicazione(a, b)
        print(f"La moltiplicazione è: {risultato}")
    else:
        risultato = divisione(a, b)
        print(f"La divisione è: {risultato}")


main()
