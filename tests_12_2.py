import unittest
from rannerr import Runner, Tournament


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {
            'Усэйн и Ник': {},
            'Андрей и Ник': {},
            'Усэйн, Андрей и Ник': {}
        }

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.assertEqual(result[1], self.usain)
        self.all_results['Усэйн и Ник'] = result

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.assertNotEqual(result[2], self.andrey)
        self.assertTrue(result[2] == self.nick)
        self.all_results['Андрей и Ник'] = result

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        last_runner = max(result.keys())
        self.assertEqual(last_runner, self.usain.name)
        self.all_results['Усэйн, Андрей и Ник'] = result

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(f'{key}:')
            for place in sorted(cls.all_results[key].keys()):
                print(f'  {place}: {cls.all_results[key][place]}')


if __name__ == '__main__':
    unittest.main()
