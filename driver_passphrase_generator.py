import random
from words import words as common_words
def main():
    words = list(map(lambda s: s.capitalize(), common_words))

    for i in range(256):
        password = random.choice(words) + random.choice(words) + random.choice(words)
        while len(password) >= 15:
            password = random.choice(words) + random.choice(words) + random.choice(words)
        print(f"{i:3} {password:}")


if __name__ == "__main__":
    main()
