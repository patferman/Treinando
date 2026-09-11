#Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.
def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
    n = int(input("Digite 10 números entre 0 e 9: "))
    if len(str(n)) != 10:
        print("Por favor, digite exatamente 10 números.")

        

