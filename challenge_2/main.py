with open("passwords.txt") as f:
    passwords = [password.split() for password in f.readlines()]

    # Part 1
    passwords = [{
        "limits": password[0].split("-"),
        "letter": password[1][0],
        "pwd": password[2]
        } for password in passwords]

    valid_passwords = filter(
        lambda passwd:
        True if
        int(passwd["limits"][0]) <=
        passwd["pwd"].count(passwd["letter"]) <=
        int(passwd["limits"][1])
        else False,
        passwords)

    print(len(list(valid_passwords)))

    # Part 2
    valid_passwords = 0
    for password in passwords:
        letter = password["letter"]
        pwd = password["pwd"]
        fp = int(password["limits"][0]) - 1
        sp = int(password["limits"][1]) - 1

        if(pwd[fp] == pwd[sp]):
            continue

        if(pwd[fp] == letter or pwd[sp] == letter):
            valid_passwords += 1

    print(valid_passwords)
