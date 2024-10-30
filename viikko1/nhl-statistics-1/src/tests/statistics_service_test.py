import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_player(self):
        return self.assertAlmostEqual(str(self.stats.search("Semenko")), "Semenko EDM 4 + 12 = 16")
    
    def test_search_not_found(self):
        return self.assertAlmostEqual(str(self.stats.search("Selanne")), "None")
    
    def test_team(self):
        players_of_team = [str(player) for player in self.stats.team("EDM")]
        stub_players = [str(player) for player in [Player("Semenko", "EDM", 4, 12), Player("Kurri",   "EDM", 37, 53), Player("Gretzky", "EDM", 35, 89)]]
        return self.assertListEqual(players_of_team, stub_players)
    
    def test_top_points(self):
        top_players = [str(player) for player in self.stats.top(1, SortBy.POINTS)]
        stub_players = [str(Player("Gretzky", "EDM", 35, 89)), str(Player("Lemieux", "PIT", 45, 54))]
        return self.assertListEqual(top_players, stub_players)
    
    def test_top_goals(self):
        top_players = [str(player) for player in self.stats.top(0, SortBy.GOALS)]
        return self.assertEqual(top_players[0], str(Player("Lemieux", "PIT", 45, 54)))
    
    def test_top_assists(self):
        top_players = [str(player) for player in self.stats.top(0, SortBy.ASSISTS)]
        return self.assertEqual(top_players[0], str(Player("Gretzky", "EDM", 35, 89)))
    
    def test_top_bad_how(self):
        return self.assertAlmostEqual(self.stats.top(0, "points"), None)