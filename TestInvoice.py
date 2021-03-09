import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5}, 'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10} }

    return products

@pytest.fixture()
def invoice():
     invoice = Invoice()
     return invoice


def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice = Invoice()
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_canCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

def test_canCalulateTax(invoice, products):
    invoice = Invoice()
    invoice.addTax(products)
    assert invoice.addTax(products) == 4.86

def test_canCalculateTotalPurePriceWithTaax(invoice, products):
    invoice.totalPurePriceWithTax(products)
    assert invoice.totalPurePriceWithTax(products) == 74






