# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            # Sulfuras never changes
            if item.name == SULFURAS:
                continue

            self._update_quality_before_expiration(item)
            self._decrease_sell_in(item)
            self._update_quality_after_expiration(item)

            # Quality is always between 0 and 50
            item.quality = max(0, min(50, item.quality))

    def _decrease_sell_in(self, item):
        item.sell_in -= 1

    def _update_quality_before_expiration(self, item):
        if item.name == AGED_BRIE:
            item.quality += 1

        elif item.name == BACKSTAGE:
            item.quality += 1
            if item.sell_in <= 10:
                item.quality += 1
            if item.sell_in <= 5:
                item.quality += 1

        else:
            item.quality -= 1

    def _update_quality_after_expiration(self, item):
        if item.sell_in >= 0:
            return

        if item.name == AGED_BRIE:
            item.quality += 1

        elif item.name == BACKSTAGE:
            item.quality = 0

        else:
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

