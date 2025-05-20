import unittest
from array_list import ArrayList
from circular_linked_list import CircularLinkedList

class BaseListTest:
    def setUp(self):
        self.list = self.list_class()

    def test_initial_length(self):
        self.assertEqual(self.list.length(), 0)

    def test_append_and_length(self):
        self.list.append('a')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'a')

    def test_insert_at_start(self):
        self.list.insert('a', 0)
        self.assertEqual(self.list.get(0), 'a')
        self.list.insert('b', 0)
        self.assertEqual(self.list.get(0), 'b')
        self.assertEqual(self.list.get(1), 'a')

    def test_insert_in_middle(self):
        self.list.append('a')
        self.list.append('c')
        self.list.insert('b', 1)
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.length(), 3)

    def test_insert_at_end(self):
        self.list.append('a')
        self.list.insert('b', 1)
        self.assertEqual(self.list.get(1), 'b')

    def test_insert_out_of_bounds_negative(self):
        with self.assertRaises(IndexError):
            self.list.insert('a', -1)

    def test_insert_out_of_bounds_large(self):
        with self.assertRaises(IndexError):
            self.list.insert('a', 1)

    def test_delete(self):
        self.list.append('a')
        self.list.append('b')
        deleted = self.list.delete(0)
        self.assertEqual(deleted, 'a')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'b')

    def test_delete_last_element(self):
        self.list.append('a')
        deleted = self.list.delete(0)
        self.assertEqual(deleted, 'a')
        self.assertEqual(self.list.length(), 0)
        with self.assertRaises(IndexError):
            self.list.get(0)

    def test_delete_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.list.delete(0)

    def test_get(self):
        self.list.append('a')
        self.list.append('b')
        self.assertEqual(self.list.get(1), 'b')

    def test_get_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.list.get(0)

    def test_deleteAll(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('a')
        self.list.deleteAll('a')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'b')

    def test_clone(self):
        self.list.append('a')
        clone = self.list.clone()
        clone.append('b')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(clone.length(), 2)

    def test_reverse(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')
        self.list.reverse()
        self.assertEqual(self.list.get(0), 'c')
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.get(2), 'a')

