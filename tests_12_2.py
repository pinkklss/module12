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

    def test_tournament_order(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertEqual(list(results.keys()), [1, 2, 3])
        self.assertEqual(results[1].name, "Усэйн")
        self.assertEqual(results[2].name, "Андрей")
        self.assertEqual(results[3].name, "Ник")
        self.all_results['test_tournament_order'] = results

    def test_tournament_results(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.assertIn(1, results)
        self.assertIn(2, results)
        self.assertIn(3, results)
        self.all_results['test_tournament_results'] = results
    
    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(f'{key}:')
            for place in sorted(cls.all_results[key].keys()):
                print(f'  {place}: {cls.all_results[key][place]}')


if __name__ == '__main__':
    unittest.main()
