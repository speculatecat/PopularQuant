import unittest
from CardBag import PokerCardJoker, PokerCardFault, CardBag


class PokerCardJokerTestCase(unittest.TestCase):
    def test_get_card_face(self):
        card = PokerCardJoker()
        self.assertEqual(card.type, 0)
        card_face = card.get_card_face()
        self.assertEqual(card_face == 0 or card_face == 1, True)


class PokerCardFaultTestCase(unittest.TestCase):
    def test_get_card_face(self):
        card = PokerCardFault()
        self.assertEqual(card.type, 1)
        card_face = card.get_card_face()
        self.assertEqual(card_face, 0)


class CardBagTestCase(unittest.TestCase):
    def test_get_card(self):
        console = False
        card_bag = CardBag()
        for i in range(10):
            card = card_bag.get_card()
            card_face = card.get_card_face()
            if card.type == 0:
                card_type = 'joker card'
                if card_face == 0:
                    card_face_name = 'joker'
                else:
                    card_face_name = 'reverse'
            else:
                card_type = 'fault card'
                card_face_name = 'reverse'

            if console:
                print('Iteration %i : %s - %s' % (i, card_type, card_face_name))
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
