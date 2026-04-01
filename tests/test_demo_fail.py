"""
Демонстрационный тест, который будет намеренно провален.
"""

import pytest
from src.calculator import Calculator


class TestDemoFail:
    """Демонстрация провального тестирования."""
    
    def setup_method(self):
        self.calc = Calculator()
    
    def test_intentional_fail(self):
        """Этот тест намеренно провалится."""
        result = self.calc.calculate("2+2")
        # Намеренно неправильное ожидание
        assert result == 5.0, f"Ожидалось 5.0, но получено {result}"
    
    def test_division_by_zero_fail(self):
        """Демонстрация ошибки деления на ноль."""
        with pytest.raises(ValueError):  # Неправильное исключение
            self.calc.calculate("5/0")
