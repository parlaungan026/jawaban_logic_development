def hitung(str):
    n = {}

    for char in str:
        if char.isalpha():
            if char in n:
                n[char] += 1
            else:
                n[char] = 1

    sorted_counts = {k: v for k, v in sorted(n.items(), key=lambda item: item[0])}

    return sorted_counts


print(hitung("Hello World"))
print(hitung("Bismillah"))  
