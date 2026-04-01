"""
Модуль преобразования инфиксной записи в обратную польскую нотацию (ОПН).
Использует алгоритм сортировочной станции Эдсгера Дейкстры.
"""

from typing import List, Union, Dict


class ShuntingYard:
    """
    Преобразует выражение из инфиксной формы (2+3) в постфиксную (2 3 +).

    Алгоритм:
    1. Читаем токены слева направо
    2. Числа сразу отправляем в выход
    3. Операторы помещаем в стек, учитывая приоритет
    4. Скобки обрабатываем особым образом
    """

    # Приоритеты операций (чем больше число, тем выше приоритет)
    # 3 уровня приоритета:
    #   Уровень 1: + и -
    #   Уровень 2: * и /
    #   Уровень 3: ^ (возведение в степень)
    PRECEDENCE: Dict[str, int] = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,  # Наивысший приоритет
    }

    # Ассоциативность операций
    # L - левоассоциативные (вычисляем слева направо)
    # R - правоассоциативные (вычисляем справа налево)
    ASSOCIATIVITY: Dict[str, str] = {
        '+': 'L',
        '-': 'L',
        '*': 'L',
        '/': 'L',
        '^': 'R',  # Степень вычисляется справа налево: 2^3^2 = 2^(3^2)
    }

    def infix_to_rpn(self, tokens: List[Union[str, float]]) -> List[Union[str, float]]:
        """
        Преобразует список инфиксных токенов в RPN.

        Args:
            tokens: Список токенов в инфиксной форме

        Returns:
            Список токенов в обратной польской нотации

        Raises:
            ValueError: При непарных скобках или других ошибках
        """
        output = []  # Выходная очередь (результат)
        stack = []  # Стек для операторов и скобок

        for token in tokens:
            # 1. Если токен - число, добавляем его в выход
            if isinstance(token, float):
                output.append(token)

            # 2. Если токен - оператор
            elif token in self.PRECEDENCE:
                # Пока в стеке есть операторы с большим или равным приоритетом
                # (для левоассоциативных операций)
                while (stack and stack[-1] != '(' and
                       self._should_pop_operator(stack[-1], token)):
                    output.append(stack.pop())
                stack.append(token)

            # 3. Если токен - левая скобка
            elif token == '(':
                stack.append(token)

            # 4. Если токен - правая скобка
            elif token == ')':
                # Выталкиваем операторы из стека до левой скобки
                while stack and stack[-1] != '(':
                    output.append(stack.pop())

                # Проверяем, нашли ли левую скобку
                if not stack:
                    raise ValueError("Непарные скобки: закрывающая скобка без открывающей")

                stack.pop()  # Удаляем левую скобку из стека

        # 5. Выталкиваем все оставшиеся операторы из стека
        while stack:
            if stack[-1] in '()':
                raise ValueError("Непарные скобки: остались незакрытые скобки")
            output.append(stack.pop())

        return output

    def _should_pop_operator(self, stack_op: str, current_op: str) -> bool:
        """
        Определяет, нужно ли вытолкнуть оператор из стека.

        Args:
            stack_op: Оператор в стеке
            current_op: Текущий оператор

        Returns:
            True если нужно вытолкнуть, False если нет
        """
        # Если приоритет оператора в стеке выше, чем у текущего
        if self.PRECEDENCE[stack_op] > self.PRECEDENCE[current_op]:
            return True

        # Если приоритеты равны и текущий оператор левоассоциативный
        if (self.PRECEDENCE[stack_op] == self.PRECEDENCE[current_op] and
                self.ASSOCIATIVITY[current_op] == 'L'):
            return True

        return False