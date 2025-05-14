"""print("break:")

for i in range(1, 10):
    if i == 5:
        print("i = 5,")
        break
    print(i)"""
print("\ncontinue örneği:")

for i in range(1, 10):
    if i == 5:
        print("i = 5, bu tur atlanıyor.")
        continue
    print(f"i: {i}")

