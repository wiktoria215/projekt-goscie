goscie = ["ania", "asia", "gosia", "Bartek", "Adam" ]

print(f"Lista wszystkich gości: {goscie}")

potwierdzeni = []

for gosc in goscie:
    odpowiedz = input(f"Czy {gosc} potwierdza przybycie? (tak/nie): ")
    if odpowiedz == "tak":
        potwierdzeni.append(gosc)

print("---")
print(f"Ostateczna lista potwierdzonych gości: {potwierdzeni}")
print(f"Liczba potwierdzonych gości: {len(potwierdzeni)}")
