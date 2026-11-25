# Практична 9. Завдання 3

name = "Illia"
surname = "Basalukk"
group = "IT-31"
day = 11

# 1–2. Речення про себе
about = "I study programming at college and I like games and drawing."

print(f"{name} {surname}, {group}")
print("About:", about)
print()

# 3. Кількість слів, найдовше слово, зворотний порядок
words = about.split()

print("Number of words:", len(words))

longest_word = max(words, key=len)
print("Longest word:", longest_word)

print("Words reversed:", " ".join(words[::-1]))
print()

# 4. Кількість літер a без урахування регістру
a_count = about.lower().count("a")

print("Number of 'a':", a_count)
print()

# 5. Кожне слово з великої літери
capitalized = about.title()
print("Capitalized:", capitalized)

# Заміна пробілів на _
underscored = about.replace(" ", "_")
print("With underscores:", underscored)
print()


# 6. Функція перевірки паліндрому
def is_palindrome(text):
    cleaned = "".join(text.lower().split())
    return cleaned == cleaned[::-1]


print("Is my name palindrome:", is_palindrome(name))
print("Is 'Never odd or even' palindrome:",
      is_palindrome("Never odd or even"))
print()


# 7. Шифр Цезаря
def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("a")
            result += chr((ord(char.lower()) - base + shift) % 26 + base)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


encrypted = caesar_encrypt(name, day)
decrypted = caesar_decrypt(encrypted, day)

print("Day:", day)
print("Encrypted name:", encrypted)
print("Decrypted name:", decrypted)