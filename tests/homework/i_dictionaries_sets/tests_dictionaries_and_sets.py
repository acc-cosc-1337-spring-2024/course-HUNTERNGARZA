import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory

class Test_Config(unittest.TestCase):
    def test_add_inventory(self):
        widgets = {}

        add_inventory(widgets, "Widget1", 10)
        self.assertEqual(widgets, {"Widget1": 10})

        add_inventory(widgets, "Widget1", 25)
        self.assertEqual(widgets, {"Widget1": 35})

        add_inventory(widgets, "Widget1", -10)
        self.assertEqual(widgets, {"Widget1": 25})


    def test_remove_inventory(self):
        widgets = {"Widget1": 7, "Widget2": 86}

        remove_inventory(widgets, "Widget1")
        
        self.assertEqual(len(widgets), 1)
        self.assertIsNotNone(widgets.get("Widget2"))
