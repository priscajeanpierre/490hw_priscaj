# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def read_records(record_file):
    record_list = []
    with open(record_file) as fileIO:
        for record in fileIO:
            record_list.append(record.strip())
    print(record_list)
    return record_list


def get_cart_total(cart: list, state: str):
    # determine sales tax based on state
    tax = 0.0
    if state == "NJ":
        tax = 0.066
    elif state == "PA":
        tax = 0.06

    price_total = 0.0
    for item in cart:
        record_fields = item.split()
        print(record_fields)
        item_name: str = record_fields[0]
        item_price = float(record_fields[1])
        item_type = record_fields[2]
        if item_type == 'wic_eligible_food':
            price_total += item_price
        elif item_type == 'clothing':
            if 'fur' in item_name and state == 'NJ':
                price_total += item_price + (item_price * tax)
            else:
                price_total += item_price
        else:
            price_total += item_price + (item_price * tax)

    return round(price_total, 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    record_list = read_records("product_records.txt")
    cart_total = get_cart_total(record_list, "PA")
    print(cart_total)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
