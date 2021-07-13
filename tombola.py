import random
import os

def clean_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "java" or os.name == "nt":
        os.system("cls")

def random_list():
    n = int(input("Ingresa cantidad de participantes: "))
    participants = []
    counter = 0
    while n > 0:
        counter += 1
        participants.append(input(f"Ingrese nombre de participante {counter}: "))
        n -= 1
        
    clean_screen()

    ul = random.sample(participants, len(participants))

    cont = 0
    for i in ul:
        cont+=1
        print(f"{cont} : {i}")
    
        
if __name__ == "__main__":
    random_list()
         