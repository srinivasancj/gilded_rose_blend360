# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_quality_reduces_by_1_when_sellin_is_not_0(self):
        """
        Test if the quality of an item degrades by 1 when sellin value is above 0.
        """
        items = [Item("foo", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must reduce by 1
        self.assertEqual(9, items[0].quality)

    def test_quality_reduces_by_2_when_sellin_is_0(self):
        """
        Test if the quality of an item degrades by 2 when sellin value is 0.
        """
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must reduce by 2
        self.assertEqual(8, items[0].quality)

    def test_quality_reduces_by_2_when_sellin_is_0_2(self):
        """
        Test if the quality of an item degrades by 2 when sellin value is 0.
        """
        items = [Item("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must reduce by 1
        gilded_rose.update_quality()  # must reduce by 2
        gilded_rose.update_quality()  # must reduce by 2
        self.assertEqual(5, items[0].quality)

    def test_quality_never_reduces_below_0(self):
        """
        Test if the quality of an item never goes negative (stays at 0).
        """
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must reduce by 1
        gilded_rose.update_quality()  # must reduce by 2 but cant go below 0
        self.assertEqual(0, items[0].quality)

    def test_quality_never_goes_above_50(self):
        """
        Test if the quality of an item never goes above 50 (except Sulfuras)
        """
        items = [Item("foo", 1, 55)]  # item quality could be initiated above 50
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must reduce by 1 but cant be more than 50
        self.assertEqual(49, items[0].quality)

    def test_quality_never_goes_above_50_2(self):
        """
        Test if the quality of an item never goes above 50 (except Sulfuras)
        Test 'Aged Brie' as its quality increases every timestep
        """
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must increase by 1 but not beyond 50
        self.assertEqual(50, items[0].quality)

    def test_quality_never_goes_above_50_3(self):
        """
        Test if the quality of an item never goes above 50 (except Sulfuras)
        Test 'Aged Brie' as its quality increases every timestep
        """
        items = [Item("Aged Brie", 5, 55)]  # item quality could be initiate above 50
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must increase by 1 but not beyond 50
        self.assertEqual(50, items[0].quality)

    def test_quality_of_sulfuras_is_always_80_1(self):
        """
        Test if the quality of Sulfuras always has quality 80
        """
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must stay at 80
        self.assertEqual(80, items[0].quality)

    def test_quality_of_sulfuras_is_always_80_2(self):
        """
        Test if the quality Sulfuras always has quality 80, even if it is initiate with anything other than 80.
        (confirm this requirement)
        """
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must stay at 80
        self.assertEqual(80, items[0].quality)

    def test_quality_of_sulfuras_is_always_80_3(self):
        """
        Test if the quality of Sulfuras always has quality 80
        (confirm this requirement)
        """
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must stay at 80
        gilded_rose.update_quality()  # must stay at 80
        self.assertEqual(80, items[0].quality)

    def test_sellin_date_of_sulfuras_never_goes_down(self):
        """
        Test if the Sulfuras does not have a sellby date.. so sellin should stay constant.
        """
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 55)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must not reduce
        self.assertEqual(1, items[0].sell_in)

    def test_quality_of_aged_brie_goes_up_as_it_gets_old(self):
        """
        Test if the quality of Aged Brie goes up as it gets older
        """
        items = [Item("Aged Brie", 1, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # must increase by 1
        self.assertEqual(46, items[0].quality)

    def test_quality_of_backstage_passes_less_than_10_days_1(self):
        """
        Test if ‘Backstage passes’ increases in quality by 2 when sellin date is less than eq 10 days
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # q must increase by 2
        self.assertEqual(47, items[0].quality)

    def test_quality_of_backstage_passes_less_than_10_days_2(self):
        """
        Test if ‘Backstage passes’ increases in quality by 2 when sellin date is less than eq 10 days
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # q must increase by 2
        self.assertEqual(47, items[0].quality)

    def test_quality_of_backstage_passes_less_than_5_days_1(self):
        """
        Test if ‘Backstage passes’ increases in quality by 3 when sellin date is less than eq 5 days
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # q must increase by 3
        self.assertEqual(48, items[0].quality)

    def test_quality_of_backstage_passes_less_than_5_days_2(self):
        """
        Test if ‘Backstage passes’ increases in quality by 3 when sellin date is less than eq 5 days
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 45)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # q must increase by 3
        self.assertEqual(48, items[0].quality)

    def test_quality_of_backstage_passes_less_than_5_days_6(self):
        """
        Test if ‘Backstage passes’ quality reduces to 0 if sellin date is 0.
        """
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # q must go down to 0
        self.assertEqual(0, items[0].quality)

    def test_quality_of_conjured_items_1(self):
        """
        Test if 'Conjured' item quality reduces by 2 at each time step when sell_in > 0
        """
        items = [Item("Conjured", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # quality must go down by 2
        self.assertEqual(48, items[0].quality)

    def test_quality_of_conjured_items_2(self):
        """
        Test if 'Conjured' item quality reduces by 2 at each time step when sell_in = 0
        """
        items = [Item("Conjured", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # q must go down by 4
        self.assertEqual(46, items[0].quality)

    def test_quality_of_conjured_items_3(self):
        """
        Test if 'Conjured' item quality reduces by 2 at each time step when sell_in < 0
        """
        items = [Item("Conjured", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()  # q must go down by 4
        self.assertEqual(46, items[0].quality)


if __name__ == "__main__":
    unittest.main()
