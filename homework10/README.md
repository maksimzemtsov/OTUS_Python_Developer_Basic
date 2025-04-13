## Homework 10

### Описание  
Проект простого интернет-магазина на Django с использованием Class-Based Views и автотестами на pytest.

### Что реализовано:
- Отображение списка товаров (ListView)
- Детальный просмотр товара (DetailView)
- Создание и редактирование товаров (CreateView, UpdateView)
- Удаление товара (DeleteView)
- Покрытие базовыми тестами моделей и представлений

### Как запустить:
1. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

2. Применить миграции:
   ```bash
   python manage.py migrate
   ```

3. Создать суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```

4. Запустить сервер:
   ```bash
   python manage.py runserver
   ```

5. Перейти в админку по адресу `http://127.0.0.1:8000/admin/`


