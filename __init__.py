from datetime import datetime


def is_validate_date(date):
    fields = date.split("/")
    contains_all_fields = len(fields) == 3
    all_fields_are_integers = all([field.isdigit() for field in fields])
    return contains_all_fields and all_fields_are_integers


def get_date():
    while True:
        date = input("Enter date (dd/mm/yyyy): ")
        if is_validate_date(date):
            day, month, year = [int(field) for field in date.split("/")]
            try:
                date = datetime(year, month, day)
                return date
            except ValueError:
                print("The date you entered doesn't exist, let's try that again...")
        else:
            print("Isme bhi ni he agle me doondlo")LOL XD
