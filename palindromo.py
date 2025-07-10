def isPalindrome(s: str) -> str:
    return "Palindromo" if s == s[::-1] else "No palindromo"

if __name__ == "__main__":
    print("Palíndromos (Ingrese una palabra o 'salir'):")
    while True:
        s = input("> ")
        if s == "salir": break
        print(f"isPalindrome(\"{s}\") = {isPalindrome(s)}")