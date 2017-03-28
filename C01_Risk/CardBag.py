# -*- coding: utf-8 -*-
# Author:Yan (speculate_cat)
# email:yan@wosdata.com

from random import random


class PokerCardJoker(object):
    def __init__(self):
        # joker -> 1 reverse -> 0
        self._face = 0
        # joker card -> 0
        self.type = 0

    def get_card_face(self):
        rd = random()
        if rd > 0.5:
            self._face = 1
        else:
            self._face = 0
        return self._face

    def overturn(self):
        if self._face == 0:
            self._face = 1
            return self._face
        else:
            self._face = 0
            return self._face


class PokerCardFault(object):
    def __init__(self):
        # each side is the same
        self._face = 0
        # fault card type -> 1
        self.type = 1

    def get_card_face(self):
        return self._face

    def overturn(self):
        return self._face


class CardBag(object):
    def __init__(self):
        self.card_1 = PokerCardJoker()
        self.card_2 = PokerCardFault()

    def get_card(self):
        rd = random()
        if rd > 0.5:
            return self.card_1
        else:
            return self.card_2
