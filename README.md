Для запуска тестов на англоязычной версии сайта:

pytest -v --tb=line --language=en test_main_page.py

Должно запуститься и успешно пройти 2 теста:
1. test_guest_can_go_to_login_page                                                                                           [ 50%]
2. test_main_page.py::test_guest_should_see_login_link
