from pixqrcode.model.merchant_account import MerchantAccount
from pixqrcode.model.pix import Pix
from pixqrcode.utils.crc16 import crc16


class GenerateCode:
    def __init__(self):
        self.merchant = MerchantAccount()
        self.map_guis = {
            "mobile": "3600",
            "cpf": "3300",
            "cpnj": "3600",
            "uuid": "5800",
            "email": "4600"
        }

    @classmethod
    def left_zero(cls, text: str):
        return str(len(text)).zfill(2)

    def generate(self, pix: Pix):
        return f"00020126{self.map_guis[pix.method]}14{self.merchant.globally_unique_identifier}01{len(pix.key)}{pix.key}520400005303986540" \
               f"{len(pix.amount.__str__())}{pix.amount.__str__()}5802{pix.country_code}59{self.left_zero(pix.name)}" \
               f"{pix.name}60{self.left_zero(pix.city)}{pix.city}" \
               f"62{str(len(pix.reference_label) + 4).zfill(2)}05{self.left_zero(pix.reference_label)}" \
               f"{pix.reference_label}6304"

    @classmethod
    def crc16code(cls, query: str) -> str:
        return hex(crc16(query.encode())).__str__()

    def format_code(self, pix: Pix):
        hash_payment = self.generate(pix)
        return f"{hash_payment}{self.crc16code(hash_payment).upper()[2:]}".strip()
