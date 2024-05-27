def pattern_count(text, pattern):
    count = 0
    len_text = len(text)
    len_pattern = len(pattern)

    for i in range(len_text - len_pattern + 1):
        if text[i:i + len_pattern] == pattern:
            count += 1

    return count


print(pattern_count("palindrom", "ind"))
print(pattern_count("abakadabra", "ab"))
