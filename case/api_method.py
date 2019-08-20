import unittest
from common.md5_openapi import openApi
from .read_ import data


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.x=openApi()

    def tearDown(self):
        pass

    def test_01(self):
        data1={
            "parcelNoType": "1000",
            "parcelNo": "e1299ea376564485961898a991457b15",
            "relatedNo": "20190428111"
        }
        r1=self.x.call(data1, "open/api/v1/provider/parcel/international/delivery/no")
        print(data1)
        print(r1)

        self.assertTrue(self.x.is__success("success"))

    def test_02(self):
        r=self.x.call(data, "open/api/v1/ecommerce/parcel/upload")
        print(data)
        print(r)


if __name__ == '__main__':
    unittest.main()
