import unittest
from models.base_model import BaseModel
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_instance_attributes(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        # Check if id is generated and is a string
        self.assertIsInstance(self.model.id, str)

    def test_created_at_type(self):
        # Check if created_at is a datetime object
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        # Check if updated_at is a datetime object
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        # Check if __str__ method returns the expected string format
        expected_str = "[{}] ({}) {}".format(self.model.__class__.__name__, self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        # Check if save updates the updated_at attribute
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        # Check if to_dict returns the expected dictionary format
        model_dict = self.model.to_dict()

        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

        self.assertEqual(model_dict['__class__'], self.model.__class__.__name__)
        self.assertEqual(model_dict['id'], self.model.id)

        created_at_str = self.model.created_at.isoformat()
        updated_at_str = self.model.updated_at.isoformat()

        self.assertEqual(model_dict['created_at'], created_at_str)
        self.assertEqual(model_dict['updated_at'], updated_at_str)

if __name__ == '__main__':
    unittest.main()
