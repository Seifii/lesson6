# words = ["apple", "banana", "cherry", "date"]
# try:
#     index = int(input("Введіть індекс: "))
#     word = words[index]
#     print("Слово за індексом", index, ":", word)
# except IndexError:
#     print("Занадто довгий список")
# except ValueError:
#     print("Не є числом")
#
# raise

correct_password = "1234"
attempt = 3
while attempt > 0:
    try:
        password = input("Input password: ")
        if password == correct_password:
            print("Yaaaay")
            break
        else:
            attempt -= 1
        print(f"X ne correct pass")

        if attempt == 0:
            raise PermissionError("Usyo")


    except PermissionError as error:
        print(error)