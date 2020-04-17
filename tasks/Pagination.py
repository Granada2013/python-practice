"""Модуль содержит класс Pagination, который постранично обрабатывает содержимое переданного списка"""


class Pagination:
    def __init__(self, items: list = [], page_size: int = 10):
        self.__items = items
        self.__page_size = page_size
        self.__curr_page = 1
        if len(items) % page_size == 0:
            num_of_pages = len(items) // page_size
        else:
            num_of_pages = len(items) // page_size + 1
        self.__num_of_pages = num_of_pages

    def next_page(self):
        """Осуществляет переход на следующую страницу.
        Если достингнута последняя страница - переход не осуществляется"""
        if not self.is_last_page():
            self.__curr_page += 1
        return self

    def prev_page(self):
        """Осуществляет переход на предыдущую страницу.
        Если достигнута первая страница - переход не осуществляется"""
        if self.__curr_page > 1:
            self.__curr_page -= 1
        return self

    def first_page(self):
        """Осуществляет прееход на первую страницу"""
        self.__curr_page = 1
        return self

    def last_page(self):
        """Осуществляет переход на последнюю страницу"""
        self.__curr_page = self.__num_of_pages
        return self

    def go_to_page(self, page: int):
        """Осуществляет переход на заданную страницу"""
        self.__curr_page = 1 if page < 1 else min(self.__num_of_pages, page)
        return self

    def is_last_page(self):
        """Возвращает True, если текущая страницв последняя"""
        return self.__curr_page == self.__num_of_pages

    def get_visible_items(self):
        """Возвращает элементы на текущей странице"""
        if not self.is_last_page():
            return self.__items[(self.__curr_page - 1) * self.__page_size: self.__curr_page * self.__page_size]
        return self.__items[(self.__curr_page - 1) * self.__page_size:]

    def get_items(self):
        """Возвращает переданный список элементов"""
        return self.__items

    def get_page_size(self):
        """Возвращает размер страницы"""
        return f"Page size: {self.__page_size}"

    def get_current_page(self):
        """Возвращает номер текущей страницы"""
        return f"Current page: {self.__curr_page}"

    def selftest(self):
        while True:
            print(f"{self.get_current_page()} --> {self.get_visible_items()}")
            if self.is_last_page():
                break
            self.next_page()
        print(self.get_current_page())
        self.first_page().next_page().next_page().prev_page().last_page().go_to_page(2)
        print(self.get_current_page())
        print(self.is_last_page())
        self.first_page().last_page().prev_page()
        print(self.get_current_page())


if __name__ == '__main__':
    alphabet = list('abcdefghijklmnopqrstuvwxyz' * 2)
    p = Pagination(alphabet, 8)
    p.selftest()