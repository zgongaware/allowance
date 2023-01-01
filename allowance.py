from datetime import datetime

import gspread
import json


def insert_allowance_entries():

    # Get day of the week
    if is_friday():
        print("Allowance Day! Performing insert...")
    else:
        print("No allowance today. Ending operation.")

    # Retrieve allowance worksheet
    worksheet = get_worksheet()

    # Create allowance entries
    transaction = create_transaction()

    # Perform insert
    worksheet.append_rows(
        values=transaction,
        table_range="A1:C1"
    )
    print("Allowance inserted!")


def get_worksheet():

    # Get credentials
    gc = gspread.service_account(filename='credentials.json')

    # Return worksheet
    return gc.open("Allowance_Tracking").worksheet("Transactions")


def is_friday():
    if datetime.now().weekday() == 5:
        return True
    else:
        return False


def get_birthdays():
    with open("birthdays.json") as file:
        return json.load(file)


def create_transaction():
    transaction = []
    for kid, birthday in get_birthdays().items():
        entry = [kid.title(), datetime.now().strftime("%m/%d/%Y"), get_allowance_amount(birthday)]
        transaction.append(entry)
    return transaction


def get_allowance_amount(birthday: str):
    # Convert to datetime object
    bd = datetime.strptime(birthday, "%Y-%m-%d")

    # Return years from current date
    return (datetime.now() - bd).days // 365


if __name__ == "__main__":
    insert_allowance_entries()
