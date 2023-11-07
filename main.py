import random

WITHDRAW_VALUE_LIMIT = 500

#teste

def deposit(deposit_amount, account_balance, account_history):
    """"""
    account_balance += deposit_amount
    account_history += f"-Foi depositado:           + R${deposit_amount:5.2f} \n"
    print(f"-Foi depositado:    + R${deposit_amount:5.2f} \n")

    return account_balance, account_history


def withdraw(withdraw_value, account_balance, withdraw_quantity_limit, account_history):
    """"""
    if withdraw_quantity_limit == 0:
        print(f"Limite de saque excedido. \n")
    else:
        if withdraw_value > WITHDRAW_VALUE_LIMIT:
            print(f"Valor por saque excedido! \n")
        elif account_balance < withdraw_value:
            print("Não foi possível efetuar o saque por falta de saldo!")
        else:
            account_balance -= withdraw_value
            withdraw_quantity_limit -= 1
            account_history += f"-Foi sacado:               - R${withdraw_value:5.2f}\n"
            print(f"-Foi sacado:               - R${withdraw_value:5.2f}\n")

    return account_balance, withdraw_value, withdraw_quantity_limit, account_history


def account_history_info(account_balance, account_history):
    """"""
    print("\n====================================================")
    print(account_history)
    print(f"O seu saldo atual é de R${account_balance:5.2f}")
    print("====================================================\n")


def create_user(name, birthday, cpf, street_name, number, neighborhood, state, account_users):
    """"""

    for account in account_users:
        if cpf == account["cpf"]:
            print("The account is already exist")
            return

    user = {
        "id": random.randint(0,99999),
        "name": name,
        "birthday": birthday,
        "cpf": cpf,
        "street_name": street_name,
        "number": number,
        "neighborhood": neighborhood,
        "state": state
    }
    return user


def create_account(sequencial_number, user_id):
    """"""
    account = {
        "user_id": user_id,
        "agency_numer": "0001",
        "account_number": sequencial_number
    }
    return account

def list_user(account_users):
    """"""
    print("\n============================= \n")
    for user in account_users:
        print(f"Nome: {user['name']} | CPF: {user['cpf']}")
    print("=============================\n")


def delete_account():
    """"""
    pass


def deactivate_account():
    """"""
    pass


account_balance = 0
account_history = " "
withdraw_quantity_limit = 3
withdraw_value_limit = 500
account_users = []
accounts = []
counter = 1

while True:
    operation = input("Which operation do you want to do?\n"
                      "[1] Deposit \n"
                      "[2] Withdraw \n"
                      "[3] Account History \n"
                      "[4] Create Account \n"
                      "[5] List Users \n"
                      "[6] Logout \n")
    if operation == "1":
        deposit_amount_input = float(input("Enter the amount you wish to deposit: \n"))
        account_balance, account_history = deposit(
            deposit_amount=deposit_amount_input,
            account_balance=account_balance,
            account_history=account_history
        )

    if operation == "2":
        withdraw_value_input = float(input("Digite o valor do saque: \n"))
        account_balance, withdraw_value, withdraw_quantity_limit, account_history = withdraw(
            withdraw_value=withdraw_value_input,
            account_balance=account_balance,
            withdraw_quantity_limit=withdraw_quantity_limit,
            account_history=account_history
        )

    if operation == "3":
        account_history_info(account_balance=account_balance, account_history=account_history)

    if operation == "4":
        name = input("Digit your name: ")
        birthday = input("Digit your birthday: ")
        cpf = input("Digit your cpf: ")
        print("==Now you need to insert your address info==")
        street_name = input("Digit the street name: ")
        number = input("Digite the number: ")
        neighborhood = input("Digit the neighborhood name: ")
        state = input("Digit state name: ")

        user = create_user(
            name=name,
            birthday=birthday,
            cpf=cpf,
            street_name=street_name,
            number=number,
            neighborhood=neighborhood,
            state=state,
            account_users=account_users
        )
        if user is not None:
            account_users.append(user)
            account = create_account(sequencial_number=counter, user_id=user['id'])
            accounts.append(account)
            counter += 1
            is_another_account = True
            while is_another_account:
                result_input = input("Do you want to create another account to this User? Y/N:").lower()
                if result_input == "n":
                    account = create_account(sequencial_number=counter, user_id=user['id'])
                    accounts.append(account)
                    counter += 1
                if result_input == "n":
                    is_another_account = False

    if operation == "5":
        list_user(account_users=account_users)

    if operation == "6":
        break
