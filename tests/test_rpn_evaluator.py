"""
Тесты для вычислителя RPN.
"""

import pytest
from src.rpn_evaluator import RPNEvaluator


class TestRPNEvaluator:
    """Тесты для класса RPNEvaluator."""

    def setup_method(self):
        """Создаем экземпляр перед каждым тестом."""
        self.evaluator = RPNEvaluator()

    def test_addition(self):
        """Тест сложения."""
        result = self.evaluator.evaluate([2.0, 3.0, '+'])
        assert result == 5.0

    def test_subtraction(self):
        """Тест вычитания."""
        result = self.evaluator.evaluate([5.0, 3.0, '-'])
        assert result == 2.0

    def test_multiplication(self):
        """Тест умножения."""
        result = self.evaluator.evaluate([4.0, 5.0, '*'])
        assert result == 20.0

    def test_division(self):
        """Тест деления."""
        result = self.evaluator.evaluate([10.0, 2.0, '/'])
        assert result == 5.0

    def test_power(self):
        """Тест возведения в степень."""
        result = self.evaluator.evaluate([2.0, 3.0, '^'])
        assert result == 8.0

    def test_complex_expression(self):
        """Тест сложного выражения."""
        result = self.evaluator.evaluate([2.0, 3.0, 4.0, '*', '+'])
        assert result == 14.0

    def test_division_by_zero(self):
        """Тест деления на ноль."""
        with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
            self.evaluator.evaluate([5.0, 0.0, '/'])

    def test_insufficient_operands(self):
        """Тест с недостаточным количеством операндов."""
        with pytest.raises(ValueError, match="Недостаточно операндов"):
            self.evaluator.evaluate([2.0, '+'])

    def test_unknown_operator(self):
        """Тест с неизвестным оператором."""
        with pytest.raises(ValueError, match="Неизвестный оператор"):
            self.evaluator.evaluate([2.0, 3.0, '%'])

    def test_invalid_expression_extra_values(self):
        """Тест с лишними значениями в стеке."""
        with pytest.raises(ValueError, match="Некорректное выражение"):
            self.evaluator.evaluate([2.0, 3.0, 4.0])
