class Operation:
    def __init__(self, x, y, operator):
        self.x = x
        self.y = y
        self.operator = operator

    def __str__(self):
        return f"Risultato: {self.result()}"

    @staticmethod
    def check_number():
        while True:
            try:
                return float(input("Inserisci un numero: "))
            except ValueError as e:
                print("Errore, non hai inserito un valore corretto")
                continue

    @staticmethod
    def check_operator():
        valid_operators = ["+", "-", "*", "/"]

        while True:
            operator = input("Inserisci un operatore (+, -, *, /): ")
            try:
                assert operator in valid_operators, (
                    "non hai inserito un valido operatore"
                )
                return operator
            except AssertionError as e:
                print(f"Errore, {e}")
                continue

    def result(self):
        match self.operator:
            case "+":
                return self.x + self.y
            case "-":
                return self.x - self.y
            case "*":
                return self.x * self.y
            case "/":
                try:
                    return self.x / self.y
                except ZeroDivisionError:
                    return "Non puoi dividere per 0"

    @classmethod
    def get(cls):
        """
        Chiede all'utente di inserire due valori numerici e un operatore tra +, -, *, /.
        """
        x = cls.check_number()
        operator = cls.check_operator()
        y = cls.check_number()

        return cls(x, y, operator)


def main():
    risultato1 = Operation.get()
    print(risultato1)


if __name__ == "__main__":
    main()
