#!/usr/bin/python3
"""Unittests for BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """SetupClassmethod"""

        cls.my_model = BaseModel()
        cls.my_model.name = "My First Model"
        cls.my_model.my_number = 89

    def test_creation(self):
        """Test Creation"""

        self.assertIsInstance(self.my_model, BaseModel)

    def test_attributes(self):
        """ Test Atributes """

        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_str_representation(self):
        """ Str repr """

        print(self.my_model)

    def test_save_method(self):
        """Save method"""

        self.my_model.save()

    def test_to_dict_method(self):
        """ To dict merhod """

        my_model_dict = self.my_model.to_dict()
        print(my_model_dict)

if __name__ == '__main__':
    unittest.main()

