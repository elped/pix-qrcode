import os
import unittest

from pixqrcode import PixQrCode, PixError


class PixTestCase(unittest.TestCase):

    def test_validation_fail(self):
        key = "123"
        pix = PixQrCode(
            name="Joao Carlos",
            key=key,
            amount="255.00",
            city="São Paulo",
        )
        try:
            pix.is_valid()
        except Exception as e:
            self.assertEqual(type(e), PixError)
            self.assertEqual(str(e), "Chave pix inválida {0}".format(key))

    def test_validation_success(self):
        pix = PixQrCode(
            name="Joao Carlos",
            key="(85) 98695-9807",
            amount="255.00",
            city="São Paulo",
        )
        self.assertTrue(pix.is_valid())

    def test_generate_code(self):
        pix = PixQrCode(
            name="Joao Carlos",
            key="488.617.308-08",
            amount="255.00",
            city="Santa Branca",
        )
        self.assertIsNotNone(pix.generate_code())

    def test_export_base64(self):
        pix = PixQrCode(
            name="Joao Carlos",
            key="(85) 98695-9807",
            amount="255.00",
            city="São Paulo",
        )
        self.assertIsNotNone(pix.export_base64())

    def test_save_file(self):
        pix = PixQrCode(
            name="Joao Carlos",
            key="00834420228",
            amount="255.00",
            city="São Paulo",
        )
        self.assertTrue(pix.save_qrcode("pix-joao"))
        self.assertTrue(os.path.exists("./pix-joao.png"))
        os.remove("./pix-joao.png")

    def test_valid_keys(self):
        keys_list = [
            "(85) 98695-9807",
            "85986959807"
            "carolina-nogueira85@econe.com.br",
            "318.727.125-17",
            "31872712517",
            "11.110.312/0001-74",
            "11110312000174",
            "1c33467b-be1b-4db6-aa18-296849cf85bb"
        ]

        for key in keys_list:
            pix = PixQrCode(
                name="Joao Carlos",
                key=key,
                amount="255.00",
                city="São Paulo",
            )
            self.assertTrue(pix.is_valid())


if __name__ == '__main__':
    unittest.main()
