def digitsSum(n: int) -> int:
    n = abs(n)  
    return sum(int(d) for d in str(n)) 

if __name__ == "__main__":
    print("Suma de dígitos (Ingrese número o 'salir'):")
    while True:
        entrada = input("> ")
        if entrada.lower() == "salir": break
        try:
            n = int(entrada)
            print(f"digitsSum({n}) = {digitsSum(n)}")
        except ValueError:
            print("Ingrese números enteros.")