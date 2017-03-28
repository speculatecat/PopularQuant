import unittest
from Pocker import Poker, PokerGroup


class PokerTestCase(unittest.TestCase):
    def test_poker(self):
        poker = Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.A)
        self.assertEqual(poker.poker_kind, Poker.PokerKind.SPADES)
        self.assertEqual(poker.poker_point, Poker.PokerPoint.A)

    def test_poker_sort(self):
        # same point, different kind
        poker1 = Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.A)
        poker2 = Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.A)
        self.assertTrue(Poker.poker_sort(poker1, poker2) == [poker1, poker2],
                        'The same point sort, wrong.')
        # same kind, different point
        poker3 = Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.XII)
        poker4 = Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.A)
        res = Poker.poker_sort(poker3, poker4)
        self.assertTrue(Poker.poker_sort(poker3, poker4) == [poker4, poker3],
                        'The same kind sort, wrong.')
        # different kind, different point
        poker5 = Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.XII)
        poker6 = Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.IX)
        self.assertTrue(Poker.poker_sort(poker5, poker6) == [poker6, poker5],
                        'The different kind and point sort, wrong.')


class PokerGroupTestCase(unittest.TestCase):
    royal_flush = [Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.X),
                   Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XI),
                   Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XII),
                   Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XIII),
                   Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.A)]

    flush = [Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.IX),
             Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.XI),
             Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.XII),
             Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.XIII),
             Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.A)]

    straight = [Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.IX),
                Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.X),
                Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XI),
                Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XII),
                Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.XIII)]

    four_of_a_kind = [Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.IX),
                      Poker(Poker.PokerKind.HEARTS, Poker.PokerPoint.IX),
                      Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.IX),
                      Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.IX),
                      Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.A)]

    three_of_a_kind = [Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.X),
                       Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.X),
                       Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.X),
                       Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XII),
                       Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XIII)]

    full_house = [Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.X),
                  Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.X),
                  Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.X),
                  Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XII),
                  Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XII)]

    two_pairs = [Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.X),
                 Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XII),
                 Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.X),
                 Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XII),
                 Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XI)]

    one_pair = [Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.X),
                Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XII),
                Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.X),
                Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.XIII),
                Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XI)]

    straight_flush = [Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.IX),
                      Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XI),
                      Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XII),
                      Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XIII),
                      Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.X)]

    high_card = [Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.IX),
                      Poker(Poker.PokerKind.SPADES, Poker.PokerPoint.X),
                      Poker(Poker.PokerKind.DIAMONDS, Poker.PokerPoint.A),
                      Poker(Poker.PokerKind.HEARTS, Poker.PokerPoint.XIII),
                      Poker(Poker.PokerKind.CLUBS, Poker.PokerPoint.XI)]

    def test_poker_group_royal_flush(self):
        pg_royal = PokerGroup(self.royal_flush)
        self.assertTrue(pg_royal.group_kind == PokerGroup.GroupKind.ROYAL_FLUSH, 'Royal flush, wrong')
        pg_flush = PokerGroup(self.flush)
        self.assertFalse(pg_flush.group_kind == PokerGroup.GroupKind.ROYAL_FLUSH, 'Not royal flush, wrong')

    def test_poker_group_flush(self):
        pg_flush = PokerGroup(self.flush)
        self.assertTrue(pg_flush.group_kind == PokerGroup.GroupKind.Flush, 'Flush, wrong')
        pg_straight = PokerGroup(self.straight)
        self.assertFalse(pg_straight.group_kind == PokerGroup.GroupKind.Flush, 'Not Flush, wrong')

    def test_poker_group_straight(self):
        self.assertTrue(PokerGroup.is_straight(self.straight), 'is straight.')
        self.assertTrue(PokerGroup.is_straight(self.royal_flush), 'royal_flush test.')
        self.assertFalse(PokerGroup.is_straight(self.flush), 'flush test')

    def test_four_of_a_kind(self):
        self.assertTrue(PokerGroup.is_four_of_a_kind(self.four_of_a_kind), 'is four of kind')
        self.assertFalse(PokerGroup.is_four_of_a_kind(self.three_of_a_kind), 'three of a kind is not four of a kind')
        self.assertFalse(PokerGroup.is_four_of_a_kind(self.flush), 'flush is noy four of a kine')

    def test_three_of_a_kind(self):
        self.assertTrue(PokerGroup.is_three_of_a_kind(self.three_of_a_kind), 'is three of a kind')
        self.assertTrue(PokerGroup.is_three_of_a_kind(self.full_house), 'full house is a kind of three of a kind')
        self.assertFalse(PokerGroup.is_three_of_a_kind(self.four_of_a_kind), 'four of a kind is not three of a kind')

    def test_two_pairs(self):
        self.assertTrue(PokerGroup.is_two_pairs(self.two_pairs), 'is two pairs')
        self.assertFalse(PokerGroup.is_two_pairs(self.three_of_a_kind), 'three of a kind is not two pairs')

    def test_one_pair(self):
        self.assertTrue(PokerGroup.is_one_pairs(self.one_pair), 'is one pair')
        self.assertFalse(PokerGroup.is_one_pairs(self.two_pairs), 'two pairs is not one pair')

    def test_PokerGroup_init(self):
        pg1 = PokerGroup(self.royal_flush)
        self.assertTrue(pg1.group_kind == PokerGroup.GroupKind.ROYAL_FLUSH, 'is royal flush')
        pg2 = PokerGroup(self.flush)
        self.assertTrue(pg2.group_kind == PokerGroup.GroupKind.Flush, 'is flush')
        pg3 = PokerGroup(self.full_house)
        self.assertTrue(pg3.group_kind == PokerGroup.GroupKind.FULL_HOUSE, 'is full house')
        pg4 = PokerGroup(self.straight)
        self.assertTrue(pg4.group_kind == PokerGroup.GroupKind.STRAIGHT, 'is straight')
        pg5 = PokerGroup(self.four_of_a_kind)
        self.assertTrue(pg5.group_kind == PokerGroup.GroupKind.FOUR_OF_A_KIND, 'is four of a kind')
        pg6 = PokerGroup(self.three_of_a_kind)
        self.assertTrue(pg6.group_kind == PokerGroup.GroupKind.THREE_OF_A_KIND, 'is three of a kind')
        pg7 = PokerGroup(self.two_pairs)
        self.assertTrue(pg7.group_kind == PokerGroup.GroupKind.TWO_PAIR, 'is two pairs')
        pg8 = PokerGroup(self.one_pair)
        self.assertTrue(pg8.group_kind == PokerGroup.GroupKind.ONE_PAIR, 'is one pair')
        pg9 = PokerGroup(self.straight_flush)
        self.assertTrue(pg9.group_kind == PokerGroup.GroupKind.STRAIGHT_FLUSH, 'is straight flush')
        pg10 = PokerGroup(self.high_card)
        self.assertTrue(pg10.group_kind == PokerGroup.GroupKind.HIGH_CARD, 'is high card')


if __name__ == '__main__':
    unittest.main()
