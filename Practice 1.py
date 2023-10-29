n = 2
def is_even(number):
    if number % 2 == 0:
        return "четное"
    else:
        return "нечетное"
adasdad = is_even(n)
print(adasdad)

# ---------------

list = [1, 2, 3]
def avg(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

average = avg(list)
print(average)

# ---------------

def count_vowels(v):
    vowels = "аоиеуюяэ"
    count = 0
    for i in v.lower():
        if i in vowels:
            count += 1
    return count
dsd = input("Введите строку: ")
vowels = count_vowels(dsd)
print(vowels)