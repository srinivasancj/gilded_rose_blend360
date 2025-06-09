# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_quality_reduces_by_2_when_sellin_is_0(self):
        """
        Test if the quality of an item degrades by 2 when sellin value is 0.
        """
        items = [Item("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #must reduce by 1
        gilded_rose.update_quality() #must reduce by 2
        self.assertEqual(7, items[0].quality)

    def test_quality_reduces_by_2_when_sellin_is_0_2(self):
        """
        Test if the quality of an item degrades by 2 when sellin value is 0.
        """
        items = [Item("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #must reduce by 1
        gilded_rose.update_quality() #must reduce by 2
        gilded_rose.update_quality() #must reduce by 2
        self.assertEqual(5, items[0].quality)


     
    def test_quality_never_reduces_below_0(self):
        """
        Test if the quality of an item never goes negative (stays at 0).
        """
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality() #must reduce by 1
        gilded_rose.update_quality() #must reduce by 2 but cant go below 0
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
