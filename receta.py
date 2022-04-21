import json

class Receta:
    
    FILE_RECETAS = "recetas.txt"
    
    def __existe_receta(self, nombre_receta):
        with open(self.FILE_RECETAS,"r") as file:
            for receta_json in file:
                receta = json.loads(receta_json)
                if receta["nombre"] == nombre_receta:
                    return True
            return False

    def __print_receta(self, receta):
        result = f"Nombre: {receta['nombre']}\n"
        result += f"Tiempo: {receta['tiempo']} minutos \n"
        result += "Ingredientes:\n"
        for ingrediente in receta["ingredientes"]:
            result += f"* {ingrediente}\n"
        return result

    def mostrar_receta(self, nombre_receta):
        if self.__existe_receta(nombre_receta):
            with open(self.FILE_RECETAS, "r") as file:
                recetas = file.readlines()                  # Leemos líneas a lista
                for receta_json in recetas:                 # la líneas del fichero contienen texto en formato json
                    receta = json.loads(receta_json)        # pasamos la línea a diccionario
                    if receta["nombre"] == nombre_receta:
                        return self.__print_receta(receta)
                
        return False

    

    def __lista_en_lista(self, lista, lista_buscar):
        """Comprueba si todos los elementos de lista están en lista_buscar """
        
        for item in lista:
            if item not in lista_buscar:
                return False
        return True

    def mostrar_receta_ingredientes(self, lista_ingredientes):
        with open(self.FILE_RECETAS,"r") as file:
            recetas = file.readlines()
            for receta_json in recetas:                 
                receta = json.loads(receta_json)
                ingredientes_receta = receta["ingredientes"]   # Extraemos los ingredientes de la receta que estamos recorriendo
                
                # Comprobamos si todos los ingredientes que buscamos están en la receta
                if self.__lista_en_lista(lista_ingredientes, ingredientes_receta):
                    self.mostrar_receta(receta["nombre"])
                    
    # mostrar_receta_ingredientes(["aceite", "sal", "huevos"])

    

    def nueva_receta(self, nombre_receta, tiempo, lista_ingredientes): 
        if not self.__existe_receta(nombre_receta):
            receta = {
                "nombre": nombre_receta,
                "tiempo": tiempo,
                "ingredientes": lista_ingredientes
            }
            with open(self.FILE_RECETAS, "a") as file:
                file.write("\n" + json.dumps(receta))
            return True
        return False


    def __escribir_recetas(self, recetas):
        with open(self.FILE_RECETAS, "w") as file:
            for i in range(len(recetas) - 1):
                file.write(json.dumps(recetas[i]) + "\n")
            file.write(json.dumps(recetas[-1])) # No incluimos el \n al final

    def añadir_ingrediente(self, nombre_receta, ingrediente):
        if self.__existe_receta(nombre_receta):
            # Leemos las recetas y localizamos la que queremos modificar
            with open(self.FILE_RECETAS, "r") as file:
                recetas_json = file.readlines()
                recetas = []
                for receta_json in recetas_json:
                    receta = json.loads(receta_json)
                    if receta["nombre"] == nombre_receta:
                        if ingrediente not in receta["ingredientes"]:
                            receta["ingredientes"].append(ingrediente)
                        else:
                            return False    # El ingrediente ya existe
                    recetas.append(receta)
            
            self.__escribir_recetas(recetas)
            return True
        return False    # La receta no existe


    def eliminar_receta(self, nombre_receta):
        if self.__existe_receta(nombre_receta):
            # Leemos las recetas y localizamos la que queremos eliminar
            with open(self.FILE_RECETAS, "r") as file:
                recetas_json = file.readlines()
                recetas = []
                for receta_json in recetas_json:
                    receta = json.loads(receta_json)
                    if receta["nombre"] != nombre_receta:
                        recetas.append(receta)
            
            self.__escribir_recetas(recetas)
            return True
        return False    # La receta no existe

   