# Set é uma coleção que elimina itens duplicados

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)

# Conjuntos em Python não suportam indexação e nem fatiamento. Converter para lista.

numeros = {1, 2, 3, 2}

numeros = list(numeros) # transformando em lista para apresentar o indíce (sem isso "object is not subscriptable")

print(numeros[0])

# é possível usar o enumerate

# Métodos do SET
# .Union une

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

# .Intersection (o que são iguais)

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

# .difference (tudo que é diferente)

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}

# .symmetric_difference (o contrário da intersecção)

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

# .issubset 

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b)) # True (o conjunto A tem todos os itens do conjunto B)
print(conjunto_b.issubset(conjunto_a)) # False (o conjunto B não tem todos do conjunto A)

# .issuperset o contrário do issubset

# .isdisjoint indica se tem intersecção (true or false)

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # True não tem nenhum valor igual ao outro
print(conjunto_a.isdisjoint(conjunto_c)) # False o número 1 está em a, então tem intersecção

# .add adiciona um elemento

sorteio = {1, 23}
sorteio.add(25)
print(sorteio)
sorteio.add(42)
print(sorteio)
sorteio.add(25) # se adicionar um que já existe é ignorado
print(sorteio)

# .clear vai limpar o set

sorteio.clear()

# .copy 

sorteio.copy()

# .discard deleta um item do set

numeros.discard(1) # descartaria o número 1 no set
numeros.discard(45) # descartaria o numero 45 se existir, se não existir ele continua sem apresentar erro.

# .pop sempre vai tirar um valor do set

print(numeros.pop()) # remove o primeiro item
print(numeros.pop()) # remove o segundo item
print(numeros.pop()) # remove o terceiro item..

# .remove parecido com o discard remove o item, a diferença é que se o item não existir ele apresenta erro.

numeros.remove(0) #remove o zero

# .len indica o tamanho do set contando apenas os que não estão duplicados
len(numeros)

# .in verifica se o item está no set (true or false)

1 in numeros 
10 in numeros