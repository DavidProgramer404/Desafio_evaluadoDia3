class Pizza:
    # Definición de listas estáticas de ingredientes y tipos de masa
    ingredientes_carne = ['pollo', 'vacuno', 'vegetal']
    ingredientes_vegetales = ['tomate', 'aceitunas', 'champiñones']
    tipos_masa = ['tradicional', 'delgada']

    # Método estático para validar si un elemento está en una lista de valores posibles
    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    # Método para realizar un pedido de pizza
    def hacer_pedido(self):
        # Solicitar al usuario los ingredientes y el tipo de masa
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ").lower()
        self.ingrediente_vegetal1 = input("Ingrese el primer ingrediente vegetal: ").lower()
        self.ingrediente_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ").lower()
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional/delgada): ").lower()

        # Validar si los ingredientes y el tipo de masa son válidos
        if (self.validar_elemento(self.ingrediente_proteico, self.ingredientes_carne) and
                self.validar_elemento(self.ingrediente_vegetal1, self.ingredientes_vegetales) and
                self.validar_elemento(self.ingrediente_vegetal2, self.ingredientes_vegetales) and
                self.validar_elemento(self.tipo_masa, self.tipos_masa)):
            self.es_valido = True
        else:
            self.es_valido = False
