def integerSort(inputArray: list) -> list:
    resultArray = inputArray.copy()
    n = len(resultArray)
    for i in range(n):
        for j in range(0, n - i - 1):
            if resultArray[j] > resultArray[j + 1]:
                resultArray[j], resultArray[j + 1] = resultArray[j + 1], resultArray[j]
    return resultArray

if __name__ == "__main__":
    print("Ingresa números enteros separados por espacios (o 'salir' para terminar):")
    while True:
        entrada = input("> ")
        if entrada.lower() == "salir":
            break
        try:
            inputArray = [int(x) for x in entrada.split()]
            if not inputArray:
                print("La lista está vacía. Ingresa al menos un número.")
                continue
            resultado = integerSort(inputArray)
            print(f"integerSort({inputArray}) = {resultado}")
        except ValueError:
            print("Por favor, ingresa números enteros separados por espacios.")