#Mean-Variance-Standard Deviation Calculator
import math
def calculate_statistics(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_deviation = math.sqrt(variance)
    return mean, variance, std_deviation

numbers_str = input("Sayıları aralarında boşluk bırakarak girin: ")
numbers = [float(x) for x in numbers_str.split()]

mean, variance, std_deviation = calculate_statistics(numbers)

print(f"Ortalama: {mean:.2f}")
print(f"Varyans: {variance:.2f}")
print(f"Standart Sapma: {std_deviation:.2f}")
