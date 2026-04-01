"""
Модуль токенизатора - разбивает строку выражения на отдельные токены.
Токены - это числа, операторы и скобки.
"""

import re
from typing import List, Union


class Tokenizer:
    """
    Преобразует строку математического выражения в список токенов.

    Пример:
        "2 + 3 * 4" -> [2.0, '+', 3.0, '*', 4.0]
        "(2+3)*4" -> ['(', 2.0, '+', 3.0, ')', '*', 4.0]
    """

    def __init__(self):
        # Регулярное выражение для поиска чисел и символов
        # \d+(?:\.\d+)? - находит целые и дробные числа
        # [+\-*/^()] - находит операторы и скобки
        self.token_pattern = re.compile(
            r'\d+(?:\.\d+)?|[+\-*/^()]'
        )

    def tokenize(self, expression: str) -> List[Union[str, float]]:
        """
        Разбивает строку выражения на токены.

        Args:
            expression: Строка с математическим выражением

        Returns:
            Список токенов (числа float, операторы и скобки как строки)

        Raises:
            ValueError: Если выражение пустое или не содержит валидных токенов
        """
        # Удаляем все пробелы для упрощения
        expression = expression.strip()

        # Проверка на пустое выражение
        if not expression:
            raise ValueError("Выражение не может быть пустым")

        tokens = []

        # Ищем все совпадения в выражении
        for match in self.token_pattern.finditer(expression):
            token = match.group()

            # Если токен похож на число (цифры и точка), преобразуем в float
            if token.replace('.', '').isdigit():
                tokens.append(float(token))
            else:
                # Иначе это оператор или скобка
                tokens.append(token)

        # Проверяем, нашли ли хоть что-то
        if not tokens:
            raise ValueError("Выражение не содержит валидных символов")

        return tokens