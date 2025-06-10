# -*- coding: utf-8 -*-


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            match item.name:
                case "Sulfuras, Hand of Ragnaros":
                    item.quality = 80
                case "Aged Brie":
                    item.quality = min(50, item.quality + 1)
                    item.sell_in -= 1
                case "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in <= 0:  # after the concert, the passes lose value
                        item.quality = 0
                    elif (
                        item.sell_in < 6
                    ):  # close to the concert, the passes go up by 3
                        item.quality = max(0, item.quality + 3)
                    elif (
                        item.sell_in < 11
                    ):  # 10 days close to the concert, the passes go up by 2
                        item.quality = max(0, item.quality + 2)
                    item.sell_in -= 1
                case "Conjured":
                    item.quality = min(50, item.quality)
                    if item.sell_in > 0:
                        item.quality = max(0, item.quality - 2)
                    else:
                        item.quality = max(0, item.quality - 4)
                    item.sell_in -= 1
                case _:  # all other items
                    item.quality = min(50, item.quality)
                    if item.sell_in > 0:
                        item.quality = max(0, item.quality - 1)
                    else:
                        item.quality = max(0, item.quality - 2)
                    item.sell_in -= 1

            """
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
            """


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
