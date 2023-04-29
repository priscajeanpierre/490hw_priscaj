import pytest
from main import read_records, get_cart_total


def test_read_records():
    expected = ['charger 10.00 misc', 'blouse 5.00 clothing', 'carrots 2.50 wic_eligible_food']
    assert read_records("product_records.txt") == expected

    expected = []
    assert read_records("empty_file.txt") == expected

    with pytest.raises(FileNotFoundError):
        read_records("invalid_file.txt")


def test_get_cart_total_with_refund():
    cart = ["toy 10.00 misc", "RefundableItem 2.00 refundable", "jeans 5.00 clothing"]
    assert get_cart_total(cart, "PA") == 14.64
    cart = [
        "toy 10.00 misc",
        "Refundable Item 2.00 refundable",
        "jeans 5.00 clothing",
        "Refundable Item 4.50 refundable",
        "stamps 2.50 misc"
    ]
    assert get_cart_total(cart, "NJ") == 21.69


def test_read_records():
    expected = ['jacket 59.99 clothing', 'apples 1.99 wic_eligible_food', 'laptop 599.99 misc']
    assert read_records("product_records.txt") == expected

    expected = []
    assert read_records("empty_file.txt") == expected

    with pytest.raises(FileNotFoundError):
        read_records("invalid_file.txt")


def test_get_cart_total():
    cart = ["deodorant 10.00 misc", "blouse 5.00 clothing", "apples 2.50 wic_eligible_food"]
    assert get_cart_total(cart, "PA") == 18.1

    cart = ["barbie 10.00 misc", "socks 5.00 clothing", "Fur Coat 100.00 clothing"]
    assert get_cart_total(cart, "NJ") == 120.96

    cart = ["gum 2.50 wic_eligible_food", "chips 1.00 wic_eligible_food"]
    assert get_cart_total(cart, "NJ") == 3.21

    cart = ["nailpolish 5.00 misc", "jeans 2 10.00 clothing", "bananas 2.50 wic_eligible_food",
            "Fur Coat 100.00 clothing"]
    assert get_cart_total(cart, "PA") == 126.64

    cart = ["charger 10.00 misc", "t-shirt 5.00 clothing"]
    assert get_cart_total(cart, "PA") == 15.00
