import unittest
from data import *


class TodoItemTester(unittest.TestCase):

    def test_constructor(self):

        first_test = ToDoItem("Zrobić zakupy", "Kupić bułki, kalafiór, szynke babuni i fante")
        second_test = ToDoItem("Kupić gry na Playstation 2", "Oddac je potrzebującym dzieciom z Afganistanu", True)

        self.assertEqual(first_test.name, "Zrobić zakupy.", "TEST OBLANY")
        self.assertEqual(first_test.description, "Kupić bułki, kalafiór, szynke babuni i fante.", "TEST OBLANY")
        self.assertEqual(first_test.is_done, False, "TEST OBLANY")
        self.assertEqual(second_test.name, "Kupić gry na playstation 2.", "TEST OBLANY")
        self.assertEqual(second_test.description, "Oddac je potrzebującym dzieciom z afganistanu.", "TEST OBLANY")
        self.assertEqual(second_test.is_done, True, "TEST OBLANY")

    def test__str__(self):

        first_test = ToDoItem("Zrobić zakupy", "Kupić bułki, kalafiór, szynke babuni i fante")
        self.assertEqual(type(first_test.__str__()), str, "TEST OBLANY")


def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
