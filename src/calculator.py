"""
Основной модуль калькулятора, объединяющий все компоненты.
"""

from src.tokenizer import Tokenizer
from src.shunting_yard import ShuntingYard
from src.rpn_evaluator import RPNEvaluator


class Calculator:
    """
    Главный класс калькулятора, который объединяет все этапы вычисления.

    Этапы вычисления:
    1. Токенизация - разбор выражения на составные части
    2. Преобразование в RPN - перевод в обратную польскую нотацию
    3. Вычисление - расчет значения по RPN
    """

    def __init__(self):
        """Инициализация всех компонентов калькулятора."""
        self.tokenizer = Tokenizer()
        self.shunting_yard = ShuntingYard()
        self.evaluator = RPNEvaluator()

    def calculate(self, expression: str) -> float:
        """
        Вычисляет математическое выражение.

        Args:
            expression: Строка с математическим выражением

        Returns:
            Результат вычисления

        Примеры:
            >>> calc = Calculator()
            >>> calc.calculate("2+3")
            5.0
            >>> calc.calculate("(2+3)*4")
            20.0
            >>> calc.calculate("2^3^2")
            512.0
        """
        # Шаг 1: Разбиваем на токены
        tokens = self.tokenizer.tokenize(expression)

        # Шаг 2: Преобразуем в обратную польскую нотацию
        rpn_tokens = self.shunting_yard.infix_to_rpn(tokens)

        # Шаг 3: Вычисляем результат
        result = self.evaluator.evaluate(rpn_tokens)

        return result

    def calculate_with_steps(self, expression: str) -> dict:
        """
        Вычисляет выражение с выводом промежуточных шагов.
        Полезно для отладки и обучения.

        Args:
            expression: Строка с математическим выражением

        Returns:
            Словарь с промежуточными результатами
        """
        tokens = self.tokenizer.tokenize(expression)
        rpn = self.shunting_yard.infix_to_rpn(tokens)
        result = self.evaluator.evaluate(rpn)

        return {
            'expression': expression,
            'tokens': tokens,
            'rpn': rpn,
            'result': result
        }
