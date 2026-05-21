import timeit

# Доступні номінали монет
COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    """
    Функція знаходить набір монет для заданої суми
    за допомогою жадібного алгоритму.

    Жадібний алгоритм завжди бере найбільшу можливу монету.
    """
    result = {}

    for coin in COINS:
        # Рахуємо, скільки монет поточного номіналу можна взяти
        count = amount // coin

        # Якщо хоча б одну монету можна використати
        if count > 0:
            result[coin] = count

            # Зменшуємо залишок суми
            amount -= coin * count

    return result


def find_min_coins(amount):
    """
    Функція знаходить мінімальну кількість монет
    для заданої суми за допомогою динамічного програмування.
    """
    # min_coins[i] зберігає мінімальну кількість монет для суми i
    min_coins = [float("inf")] * (amount + 1)

    # Для суми 0 потрібно 0 монет
    min_coins[0] = 0

    # used_coins[i] зберігає монету, яку використали останньою для суми i
    used_coins = [0] * (amount + 1)

    # Проходимо всі суми від 1 до потрібної суми
    for current_amount in range(1, amount + 1):
        # Перевіряємо кожен номінал монети
        for coin in COINS:
            if coin <= current_amount:
                previous_amount = current_amount - coin

                # Якщо через цю монету можна отримати кращий результат
                if min_coins[previous_amount] + 1 < min_coins[current_amount]:
                    min_coins[current_amount] = min_coins[previous_amount] + 1
                    used_coins[current_amount] = coin

    result = {}
    current_amount = amount

    # Відновлюємо набір монет із used_coins
    while current_amount > 0:
        coin = used_coins[current_amount]

        # Додаємо монету в результат
        result[coin] = result.get(coin, 0) + 1

        # Зменшуємо суму на номінал використаної монети
        current_amount -= coin

    return result


if __name__ == "__main__":
    # Тестова сума з умови
    test_amount = 113

    # Велика сума для порівняння продуктивності
    large_amount = 100_000

    print(f"Сума: {test_amount}")
    print("Жадібний алгоритм:", find_coins_greedy(test_amount))
    print("Динамічне програмування:", find_min_coins(test_amount))

    # Вимірюємо час роботи жадібного алгоритму
    greedy_time = timeit.timeit(
        lambda: find_coins_greedy(large_amount),
        number=1000
    )

    # Вимірюємо час роботи алгоритму динамічного програмування
    dp_time = timeit.timeit(
        lambda: find_min_coins(large_amount),
        number=10
    )

    print("\nПорівняння часу виконання:")
    print(f"Жадібний алгоритм: {greedy_time:.6f} секунд за 1000 запусків")
    print(f"Динамічне програмування: {dp_time:.6f} секунд за 10 запусків")