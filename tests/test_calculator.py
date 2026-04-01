"""
Интеграционные тесты для калькулятора.
"""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Интеграционные тесты для класса Calculator."""

    def setup_method(self):
        """Создаем калькулятор перед каждым тестом."""
        self.calc = Calculator()

    # Базовые операции
    def test_addition(self):
        """Тест сложения."""
        assert self.calc.calculate("2+3") == 5.0

    def test_subtraction(self):
        """Тест вычитания."""
        assert self.calc.calculate("5-3") == 2.0

    def test_multiplication(self):
        """Тест умножения."""
        assert self.calc.calculate("4*5") == 20.0

    def test_division(self):
        """Тест деления."""
        assert self.calc.calculate("10/2") == 5.0

    def test_power(self):
        """Тест возведения в степень."""
        assert self.calc.calculate("2^3") == 8.0

    # Приоритет операций
    def test_multiplication_priority(self):
        """Тест: умножение должно выполняться раньше сложения."""
        assert self.calc.calculate("2+3*4") == 14.0

    def test_power_priority(self):
        """Тест: степень имеет наивысший приоритет."""
        assert self.calc.calculate("2+3^2*4") == 38.0  # 2 + (9*4) = 38

    def test_power_associativity(self):
        """Тест: степень правоассоциативна."""
        assert self.calc.calculate("2^3^2") == 512.0  # 2^(3^2) = 2^9 = 512

    # Скобки
    def test_parentheses(self):
        """Тест: скобки меняют приоритет."""
        assert self.calc.calculate("(2+3)*4") == 20.0

    def test_nested_parentheses(self):
        """Тест: вложенные скобки."""
        assert self.calc.calculate("(2+(3*4))*5") == 70.0

    # Сложные выражения
    def test_complex_expression(self):
        """Тест: сложное выражение со всеми операциями."""
        assert self.calc.calculate("(2+3)*4-5/2") == 17.5

    def test_complex_with_power(self):
        """Тест: сложное выражение со степенью."""
        assert self.calc.calculate("(2+3)^2*4-10/2") == 95.0  # 5^2*4-5 = 25*4-5=100-5=95

    # Десятичные числа
    def test_decimal_numbers(self):
        """Тест: десятичные числа."""
        assert self.calc.calculate("3.5*2") == 7.0

    def test_decimal_result(self):
        """Тест: результат с десятичной частью."""
        assert self.calc.calculate("10/4") == 2.5

    # Отрицательные результаты
    def test_negative_result(self):
        """Тест: отрицательный результат."""
        assert self.calc.calculate("3-5") == -2.0

    # Ошибки
    def test_division_by_zero(self):
        """Тест: деление на ноль."""
        with pytest.raises(ZeroDivisionError):
            self.calc.calculate("5/0")

    def test_empty_expression(self):
        """Тест: пустое выражение."""
        with pytest.raises(ValueError):
            self.calc.calculate("")

    def test_invalid_parentheses(self):
        """Тест: непарные скобки."""
        with pytest.raises(ValueError):
            self.calc.calculate("(2+3")

    # Дополнительные тесты
    def test_calculate_with_steps(self):
        """Тест: метод с выводом шагов."""
        result = self.calc.calculate_with_steps("2+3*4")
        assert result['expression'] == "2+3*4"
        assert result['tokens'] == [2.0, '+', 3.0, '*', 4.0]
        assert result['rpn'] == [2.0, 3.0, 4.0, '*', '+']
        assert result['result'] == 14.0