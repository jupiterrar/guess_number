from unittest.mock import Mock
from src.player import Player

class TestPlayer:
    def test_initial_attempts(self):
        p = Player("Test", Mock())
        assert p.attempts == 0

    def test_increment_attempts(self):
        p = Player("Test", Mock())
        p.increment_attempts()
        assert p.attempts == 1

    def test_make_guess_valid(self):
        ui = Mock()
        ui.get_input.return_value = "42"
        p = Player("Test", ui)
        assert p.make_guess() == 42

    def test_make_guess_invalid_then_valid(self):
        ui = Mock()
        ui.get_input.side_effect = ["abc", "42"]
        p = Player("Test", ui)
        assert p.make_guess() == 42
        assert ui.get_input.call_count == 2