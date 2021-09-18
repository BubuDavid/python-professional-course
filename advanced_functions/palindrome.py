def is_palindrome(string: str) -> bool:
    # Delete Spaces from our string
    string = string.replace(" ", "").lower()

    return string == string[::-1]

def main():
    print(is_palindrome(1000))

if __name__ == "__main__":
    main() 