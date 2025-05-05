import sys

# argv è una lista che raccoglie tutti gli input dopo il comando python da terminale, quindi il primo elemento della lista è sempre il nome del file. ogni argomento è diviso dal semplice spazio vuoto
print(sys.argv)

print(f"Il nome dello script è {sys.argv[0]}")

argc = len(sys.argv) - 1
print(f"Il numero degli argomenti è: {argc}")

for arg in sys.argv[
    1:
]:  # partiamo dal secondo per evitare il nome del file. un'altra soluzione era usare range e iterare con i, stampando i+1
    print(arg)
