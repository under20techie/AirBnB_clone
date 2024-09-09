import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.all_objs = self.storage.all()
        self.model = BaseModel()

    def test_has_attr(self):
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

    def test_path_exists(self):
        self.assertIsNotNone(self.storage._FileStorage__file_path)

    def test_storage_all(self):
        self.assertIsInstance(self.all_objs, dict)

    def test_storage_save(self):
        self.model.save()
        self.assertIn(f"BaseModel.{self.model.id}", self.all_objs.keys())
