import bcrypt

def hash_passwords():
    salt_rounds = 12

    # Plain text passwords
    tester1_password = "Pc4RM0AMKy5aSGfD"
    tester2_password = "4LWs6xnc1t32BzXA"

    # Hash passwords
    tester1_hashed = bcrypt.hashpw(tester1_password.encode('utf-8'), bcrypt.gensalt(salt_rounds)).decode('utf-8')
    tester2_hashed = bcrypt.hashpw(tester2_password.encode('utf-8'), bcrypt.gensalt(salt_rounds)).decode('utf-8')

    # Print hashed passwords
    print({"tester1Password": tester1_hashed, "tester2Password": tester2_hashed})

if __name__ == "__main__":
    hash_passwords()
