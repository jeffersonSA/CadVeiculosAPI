from json import loads
from unittest import TestCase
from flask import url_for
from src.app import app
from src.db import db

class BaseCase(TestCase):
    
    def setUp(self):
        app.testing = True
        app_context = app.test_request_context()
        app_context.push()
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        """Roda depois de todos os testes."""
        db.drop_all()