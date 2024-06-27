def write_to_file(action):
    with open('users.txt', 'a') as file:
        file.write(f"{action}\n")

def write_credentials_to_file(credentials):
    with open('users.txt', 'w') as file:
        for username, password in credentials.items():
            file.write(f"Username:{username}\nPassword:{password}\n")

def read_credentials():
    credentials = {}
    try:
        with open('users.txt', 'r') as file:
            for line in file:
                if line.startswith("Username:"):
                    username_start_idx = len("Username:")
                    password_start_idx = line.find("Password:") + len("Password:")
                    username = line[username_start_idx:line.find("Password:")].strip()
                    password = line[password_start_idx:].strip()
                    credentials[username] = password
    except FileNotFoundError:
        pass  
    return credentials

def register():
    credentials = read_credentials()
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    if username in credentials:
        print(f"Existing Username\nUsername: {username}")
    else:
        credentials[username] = password
        write_credentials_to_file(credentials)
        write_to_file(f"Registered\nUsername:{username}\nPassword:{password}")
        print("Registered successfully!")

def login():
    credentials = read_credentials()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in credentials and credentials[username] == password:
        write_to_file(f"Login\nUsername:{username},Password:{password}")
        print("Login successful!")
        return True
    write_to_file(f"Login failed\nUsername:{username}\nPassword:{password}")
    print("Incorrect Credentials. Check your username or password.")
    return False

def change_password():
    credentials = read_credentials()
    username = input("Enter your username: ")
    current_password = input("Enter your current password: ")
    new_password = input("Enter your new password: ")
    if username in credentials and credentials[username] == current_password:
        credentials[username] = new_password
        write_credentials_to_file(credentials)
        write_to_file(f"Updated Password\nUsername:{username}\nNew Password:{new_password}")
        print("Password updated successfully!")
    else:
        print("Password update failed. Check your username or current password.")
        write_to_file(f"Password update failed\nUsername:{username},Current Password:{current_password}")

while True:
    print("\nMENU")
    print("1. Register")
    print("2. Login")
    print("3. Change Password")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        register()
    elif choice == '2':
        if login():
            pass
    elif choice == '3':
        change_password()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
