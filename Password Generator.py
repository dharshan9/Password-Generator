import random
import string

class PasswordGenerator:
    def __init__(self, length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
        self.length = length
        self.use_uppercase = use_uppercase
        self.use_numbers = use_numbers
        self.use_special_chars = use_special_chars
        self.lowercase_chars = string.ascii_lowercase
        self.uppercase_chars = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = string.punctuation

    def _generate_char_set(self):
        char_set = self.lowercase_chars
        if self.use_uppercase:
            char_set += self.uppercase_chars
        if self.use_numbers:
            char_set += self.digits
        if self.use_special_chars:
            char_set += self.special_chars
        return char_set

    def generate_password(self):
        char_set = self._generate_char_set()
        if len(char_set) == 0:
            raise ValueError("Character set is empty. Please enable at least one type of characters.")
        password = ''.join(random.choice(char_set) for _ in range(self.length))
        return password

# Example usage:
if __name__ == "__main__":
    # Create a PasswordGenerator object
    password_gen = PasswordGenerator(length=16, use_uppercase=True, use_numbers=True, use_special_chars=True)

    # Generate a password
    new_password = password_gen.generate_password()

    # Print the generated password
    print("Generated Password:", new_password)
