"""
Модуль для вычисления выражений в обратной польской нотации.
"""

from typing import List, Union
import math


class RPNEvaluator:
    """
    Вычисляет значение выражения, записанного в обратной польской нотации.

    Алгоритм:
    1. Создаем стек
    2. Читаем токены слева направо
    3. Если токен - число, помещаем в стек
    4. Если токен - оператор, извлекаем два числа из стека,
       применяем операцию и результат помещаем обратно в стек
    """

    def evaluate(self, rpn_tokens: List[Union[str, float]]) -> float:
        """
        Вычисляет RPN выражение.

        Args:
            rpn_tokens: Список токенов в RPN формате

        Returns:
            Результат вычисления

        Raises:
            ValueError: При некорректном выражении
            ZeroDivisionError: При делении на ноль
        """
        stack = []

        for token in rpn_tokens:
            # Если число - кладем в стек
            if isinstance(token, float):
                stack.append(token)

            # Если оператор - вычисляем
            else:
                # Для бинарного оператора нужно два числа
                if len(stack) < 2:
                    raise ValueError(
                        f"Недостаточно операндов для оператора {token}"
                    )

                # Извлекаем два верхних числа (порядок важен!)
                b = stack.pop()  # Второй операнд
                a = stack.pop()  # Первый операнд

                # Применяем операцию
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Деление на ноль")
                    result = a / b
                elif token == '^':
                    result = math.pow(a, b)
                else:
                    raise ValueError(f"Неизвестный оператор: {token}")

                # Результат кладем обратно в стек
                stack.append(result)

        # В конце в стеке должен остаться один результат
        if len(stack) != 1:
            raise ValueError(
                "Некорректное выражение: в стеке осталось несколько значений"
            )

        return stack[0]
