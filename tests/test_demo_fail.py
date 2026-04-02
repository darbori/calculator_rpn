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
        """Исправленный тест - теперь правильное ожидание."""
        result = self.calc.calculate("2+2")
        # Исправлено: 4.0 вместо 5.0
        assert result == 4.0, f"Ожидалось 4.0, но получено {result}"

    def test_division_by_zero_fail(self):
        """Исправленный тест - правильное исключение."""
        # Исправлено: ZeroDivisionError вместо ValueError
        with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
            self.calc.calculate("5/0")
