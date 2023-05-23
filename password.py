import random
import string

if __name__ == "__main__":
    # Generar 8 letras aleatorias
    letters = ''.join(random.choices(string.ascii_letters, k=8))

    # Generar 4 símbolos aleatorios
    symbols = ''.join(random.choices(string.punctuation, k=4))

    # Generar 4 números aleatorios
    numbers = ''.join(random.choices(string.digits, k=4))

    # Combinar todo en una sola contraseña
    password = letters + symbols + numbers

    # Mezclar la contraseña aleatoriamente
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    print("Tu contraseña generada es:", password)
