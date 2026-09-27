from src.game import Game

class TestGame:
    def test_check_guess_too_low(self):
        g = Game()
        g._secret = 50
        assert g.check_guess(30) == "Больше!"

    def test_check_guess_too_high(self):
        g = Game()
        g._secret = 50
        assert g.check_guess(70) == "Меньше!"

    def test_check_guess_correct(self):
        g = Game()
        g._secret = 50
        assert g.check_guess(50) == "Угадали!"

    def test_secret_property(self):
        g = Game()
        assert isinstance(g.secret, int)