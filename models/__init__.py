#!/usr/bin/python3
""" Init file"""
from models.engine import file_storage.FileStorage


storage = FileStorage()
storage.reload()
