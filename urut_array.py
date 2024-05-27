belum_urut = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

letters = sorted([x for x in belum_urut if isinstance(x, str)])
numbers = sorted([x for x in belum_urut if isinstance(x, int)])

urut = letters + numbers

print(urut)
