s = input()

def Vowels(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in s:
        if i.lower() in vowel:
            count += 1

    return count

print(f"Vowels: {Vowels(s)}")
print(f"Consonants: {len(s) - Vowels(s)}")
print(f"Reversed: {s[::-1]}")