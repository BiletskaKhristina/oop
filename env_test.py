import os

# Використовуємо .get(), щоб замість помилки отримати None, якщо змінної немає
it_test_value = os.environ.get('IT_TEST')

if it_test_value:
    print(f"Значення змінної IT_TEST = {it_test_value}")
else:
    print("❌ Змінна IT_TEST не знайдена в системі.")
    print("Підказка: Спробуй виконати 'export IT_TEST=hello' у терміналі перед запуском.")