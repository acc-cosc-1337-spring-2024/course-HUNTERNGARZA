import unittest
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory
from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog2_only, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog2_not_prog_1

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


    PROG1 = {'Student1', 'Student2', 'Student3'}
    PROG2 = {'Student3', 'Student4', 'Student5'}

    def test_get_students_who_took_prog1_and_prog2(self):
        self.assertEqual(get_students_who_took_prog1_and_prog2(self.PROG1, self.PROG2), {'Student3'})

    def test_get_students_who_took_prog2_only(self):
        self.assertEqual(get_students_who_took_prog2_only(self.PROG1, self.PROG2), {'Student3', 'Student4', 'Student5'})

    def test_get_students_who_took_prog1_not_prog_2(self): 
        self.assertEqual(get_students_who_took_prog1_not_prog_2(self.PROG1, self.PROG2), {'Student1', 'Student2'})

    def test_get_students_who_took_prog2_not_prog_1(self):
        self.assertEqual(get_students_who_took_prog2_not_prog_1(self.PROG1, self.PROG2), {'Student4', 'Student5'})
