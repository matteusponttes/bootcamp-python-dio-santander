# .fromkeys atribui valor padrão a chaves

print(dict.fromkeys(["nome", "telefone"])) # {'nome': None, 'telefone': None}

print(dict.fromkeys(["nome", "telefone"], "vazio")) # {'nome': 'vazio', 'telefone': 'vazio'}

# .get segunda forma de acessar valores dentro de um dicionário

contatos.get("chave") # se não encontrar chave retorna "None"
contatos.get("chave", {}) # retorna o que colocar após a vírgula

# .items retorna uma lista de tuplas

contatos.items()

# .keys retorna só as chaves do dicionário - bom para saber todas as chaves que o dicionário tem

contatos.keys() 

# .pop remove e retorna o valor que ele removeu

resultado = contatos.pop("chave")
print(resultado)

# .popitem remove sem informar a chave

# .setdefault se não tiver no dicionário ele cria, se tiver ele ignora a atribuição

contato.setdefault("chave", "valor")

# .update atualiza valores das chaves 

# .values retorna só os valores, sem as chaves

# .in verifica se a chave existe (true or false) ou valor existe

resultado = "chave" in contatos # para chaves
resultado = "valor" in contatos["chave"] # para valores 

# .del passa o objeto que quer remover só chave, ou chave e valor (nesse caso apenas o valor é removido)

del contatos["chave"]["valor"]
del contatos["chave"]