# Append (adiciona um item na lista)

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, 'Python', [40, 30, 20]]

lista.clear() # limpa a lista

print(lista)

# Método Copy vide copy.py

# Count

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# Extend (para quando quer juntar novos elementos na lista ao invés do append)

linguagens = ["python", "js", "c"]

print(linguagens) # ['python', 'js', 'c']

linguagens.extend(["java", "csharp"])

print(linguagens) # ['python', 'js', 'c', 'java', 'csharp']

# Index (indica a posição da primeira ocorrência do elemento na lista)

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java")) # 3
print(linguagens.index("python")) # 0

# pop (pilha coleta o último elemento da pilha adicionado)

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop()) # csharp
print(linguagens.pop()) # java
print(linguagens.pop()) # c
print(linguagens.pop(0)) # python

# Remove (tira itens da lista - passar o elemento)

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens) # ['python', 'js', 'java', 'csharp']

# Reverse (mostra a lista de forma espelhada)

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens) # ['csharp', 'java', 'c', 'js', 'python']

# Sort (ordena a lista)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens) # ['c', 'csharp', 'java', 'js', 'python']

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens) # ['python', 'js', 'java', 'csharp', 'c']

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # lambda é uma função anônima, onde x indica cada elemento, e len o tamanho de cada elemento
print(linguagens) # ['c', 'js', 'java', 'python', 'csharp']

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens) # ['python', 'csharp', 'java', 'js', 'c']

# len (informa o tamanho da lista)

linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens)) # 5

# Sorted (também funciona para ordernar iteráveis)

linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x))) # ['c', 'js', 'java', 'python', 'csharp']

print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ['python', 'csharp', 'java', 'js', 'c']

print(sorted(linguagens)) # ['c', 'csharp', 'java', 'js', 'python']