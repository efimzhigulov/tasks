import requests
import random

r = requests.get('https://api.ipify.org/')
print(r.text)


print("Я брошу кубик, угадайте, что выпадет?")
number = int(input())
x = random.randint(1,6)
true_numbers = [1,2,3,4,5,6]
if number in true_numbers:
    if x == number:
        print("Ура, вы угадали! Вот вам анекдот: ")
    else:
        print(f"К сожалению, вы не угадали. На кубике выпало {x}. Ваше число {number}")
else:
    print("Необходимо ввести число от 1 до 6")


