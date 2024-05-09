from pizza import Pizza  # Importar la clase de pizza.py

# Requerimiento a: Mostrar los valores de los atributos de clase de la clase importada
print("Ingredientes de pizza:")
print("Ingredientes de carne:", Pizza.ingredientes_carne)
print("Ingredientes vegetales:", Pizza.ingredientes_vegetales)
print("Tipos de masa:", Pizza.tipos_masa)

# Requerimiento b: Validar si un elemento está en una lista de valores posibles
print("¿La salsa de tomate está presente en la lista?", Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Requerimiento c: Crear una instancia de la clase pizza y solicitar un pedido
mi_pizza = Pizza()
mi_pizza.hacer_pedido()

# Requerimiento d: Mostrar los ingredientes, el tipo de masa y si la pizza es válida
print("Ingredientes vegetales:", mi_pizza.ingrediente_vegetal1, ",", mi_pizza.ingrediente_vegetal2)
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("¿Es una pizza válida?", mi_pizza.es_valido)
