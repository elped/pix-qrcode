

class Pix:
    merchant_category_code = "0000"
    transaction_currency = "986"
    name = None
    city = None
    key = None
    amount = "0"
    reference_label = None
    method = None

    def __init__(self, name, key, city, amount=0, reference_label="***", country_code="BR") -> None:
        super().__init__()
        self.name = name
        self.city = city
        self.amount = amount
        self.key = key
        self.reference_label = reference_label
        self.country_code = country_code
