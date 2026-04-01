"""
Тесты для модуля токенизатора.
"""

import pytest
from calculator_rpn.src.tokenizer import Tokenizer


class TestTokenizer:
    """Тесты для класса Tokenizer."""

    def setup_method(self):
        """Создаем экземпляр токенизатора перед каждым тестом."""
        self.tokenizer = Tokenizer()

    def test_simple_expression(self):
        """Тест простого выражения с числами и операторами."""
        tokens = self.tokenizer.tokenize("2+3")
        assert tokens == [2.0, '+', 3.0]

    def test_expression_with_spaces(self):
        """Тест выражения с пробелами."""
        tokens = self.tokenizer.tokenize(" 2 + 3 * 4 ")
        assert tokens == [2.0, '+', 3.0, '*', 4.0]

    def test_decimal_numbers(self):
        """Тест десятичных чисел."""
        tokens = self.tokenizer.tokenize("3.5*2.7")
        assert tokens == [3.5, '*', 2.7]

    def test_with_parentheses(self):
        """Тест со скобками."""
        tokens = self.tokenizer.tokenize("(2+3)*4")
        assert tokens == ['(', 2.0, '+', 3.0, ')', '*', 4.0]

    def test_with_power(self):
        """Тест с операцией возведения в степень."""
        tokens = self.tokenizer.tokenize("2^3")
        assert tokens == [2.0, '^', 3.0]

    def test_empty_expression(self):
        """Тест пустого выражения - должно быть исключение."""
        with pytest.raises(ValueError, match="Выражение не может быть пустым"):
            self.tokenizer.tokenize("")

    def test_whitespace_only(self):
        """Тест выражения только из пробелов."""
        with pytest.raises(ValueError, match="Выражение не может быть пустым"):
            self.tokenizer.tokenize("   ")

    def test_invalid_character(self):
        """Тест с недопустимым символом."""
        with pytest.raises(ValueError, match="Выражение не содержит валидных символов"):
            self.tokenizer.tokenize("abc")

    def test_complex_expression(self):
        """Тест сложного выражения."""
        tokens = self.tokenizer.tokenize("(2+3.5)*4-10/2")
        assert tokens == [
            '(', 2.0, '+', 3.5, ')', '*', 4.0, '-', 10.0, '/', 2.0
        ]
