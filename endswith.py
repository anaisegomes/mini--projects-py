numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Break ao encontrar 5:")
for num in numeros:
    if num == 5:
        break  # Sai do loop
    print(num)
# Saída: 1, 2, 3, 4

print("\nContinue para números pares:")
for num in numeros:
    if num % 2 == 0:
        continue  # Pula o resto do loop
    print(num)
# Saída: 1, 3, 5, 7, 9