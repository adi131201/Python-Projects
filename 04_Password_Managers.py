def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Enter username: ")
    password = input("Enter password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name+"|"+password+"\n")
    print("-"*30)

while True:
    mode = input("\nWhat would you like to do: \n\n->Type 'view' to view existing passwords.\n->Type 'add' to add a new password.\n\nPress 'q' to exit...\n\n").lower()

    if mode == 'q': break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalide mode.")