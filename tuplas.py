# irmã da lista, porém imutável, após a criação não é possível alterar

frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

print(frutas, letras, numeros, pais)

# também é possível fazer matriz com tupla para não alterar

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)
print(matriz[0])      # [1, "a", 2]
print(matriz[0][0])   # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1]) # "c"

# Fatiamento também da mesma forma SSS Start Stop Step

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:]) # ('t', 'h', 'o', 'n')
print(tupla[:2]) # ('p', 'y')
print(tupla[1:3]) # ('y', 't')
print(tupla[0:3:2]) # ('p', 't')
print(tupla[::]) # ('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1]) # ('n', 'o', 'h', 't', 'y', 'p')

# Iterando

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)


# Tupla é possível os métodos .Count .index e .len