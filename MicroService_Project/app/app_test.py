import unittest
from app import test_table

class TestTasks(unittest.TestCase):

    def test_tasks(self):
        expected_results = [{'login': 'admin','mdp':'admin'}, {'login': 'user', 'mdp': 'user'}]

if __name__ == 'main':
    unittest.main()