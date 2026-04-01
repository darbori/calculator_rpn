
import pytest
from src.shunting_yard import ShuntingYard


class TestShuntingYard:
    """Тесты для класса ShuntingYard."""

    def setup_method(self):
        """Создаем экземпляр перед каждым тестом."""
        self.shunting = ShuntingYard()

    def test_simple_addition(self):
        """Тест простого сложения."""
        rpn = self.shunting.infix_to_rpn([2.0, '+', 3.0])
        assert rpn == [2.0, 3.0, '+']

    def test_subtraction(self):
        """Тест вычитания."""
        rpn = self.shunting.infix_to_rpn([5.0, '-', 3.0])
        assert rpn == [5.0, 3.0, '-']

    def test_multiplication_priority(self):
        """Тест приоритета умножения над сложением."""
        rpn = self.shunting.infix_to_rpn([2.0, '+', 3.0, '*', 4.0])
        assert rpn == [2.0, 3.0, 4.0, '*', '+']

    def test_parentheses_override_priority(self):
        """Тест приоритета скобок."""
        rpn = self.shunting.infix_to_rpn(['(', 2.0, '+', 3.0, ')', '*', 4.0])
        assert rpn == [2.0, 3.0, '+', 4.0, '*']

    def test_power_priority(self):
        """Тест приоритета возведения в степень."""
        rpn = self.shunting.infix_to_rpn([2.0, '^', 3.0, '*', 4.0])
        assert rpn == [2.0, 3.0, '^', 4.0, '*']

    def test_power_associativity(self):
        """Тест правоассоциативности степени."""
        # 2^3^4 должно быть 2^(3^4) -> 2 3 4 ^ ^
        rpn = self.shunting.infix_to_rpn([2.0, '^', 3.0, '^', 4.0])
        assert rpn == [2.0, 3.0, 4.0, '^', '^']

    def test_mixed_operators(self):
        """Тест смешанных операторов."""
        rpn = self.shunting.infix_to_rpn(
            [2.0, '+', 3.0, '*', 4.0, '-', 5.0, '/', 2.0]
        )
        assert rpn == [2.0, 3.0, 4.0, '*', '+', 5.0, 2.0, '/', '-']

    def test_nested_parentheses(self):
        """Тест вложенных скобок."""
        rpn = self.shunting.infix_to_rpn(
            ['(', 2.0, '+', '(', 3.0, '*', 4.0, ')', ')', '*', 5.0]
        )
        assert rpn == [2.0, 3.0, 4.0, '*', '+', 5.0, '*']

    def test_mismatched_parentheses_closing(self):
        """Тест лишней закрывающей скобки."""
        with pytest.raises(ValueError, match="Непарные скобки"):
            self.shunting.infix_to_rpn([2.0, '+', 3.0, ')'])

    def test_mismatched_parentheses_opening(self):
        """Тест незакрытой скобки."""
        with pytest.raises(ValueError, match="Непарные скобки"):
            self.shunting.infix_to_rpn(['(', 2.0, '+', 3.0])
