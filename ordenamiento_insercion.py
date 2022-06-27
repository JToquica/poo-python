def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        print(f"indice: {indice} - valor actual: {valor_actual}")

        while indice > 0 and lista[indice - 1] > valor_actual:
            lista[indice] = lista[indice - 1]
            indice -= 1
            print(f"indice: {indice} - lista indice: {lista[indice]}")

        lista[indice] = valor_actual
        print(f"indice: {indice} - valor actual: {valor_actual}")
    
    return lista 

if __name__ == "__main__":
    lista = [7,5,3,8,1,9,8,2]
    lista_ordenada = ordenamiento_por_insercion(lista)
    print(lista_ordenada)