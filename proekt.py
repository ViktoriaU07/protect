import datetime

class User:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.name} {self.surname}"

    def make_order(self, service, system):
        order = Order(self, service, datetime.datetime.now())
        system.add_order(order)
        return order

class Service:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price} грн)"

class Order:
    def __init__(self, user, service, date):
        self.user = user
        self.service = service
        self.date = date

    def __str__(self):
        return f"Заказ от {self.date.strftime('%d.%m.%Y %H:%M')}: {self.user} - {self.service}"

class CNUP:
    def __init__(self):
        self.services = []
        self.users = []
        self.orders = []

    def add_service(self, service):
        self.services.append(service)
        return self

    def add_user(self, user):
        self.users.append(user)
        return self

    def add_order(self, order):
        self.orders.append(order)
        return self

    def show_orders(self):
        for order in self.orders:
            print(order)

    def delete_order(self, order):
        self.orders.remove(order)
        return self

    def get_total_revenue(self):
        total = 0
        for order in self.orders:
            total += order.service.price
        return f"Общая выручка: {total} грн"

# Пример использования
system = (CNUP()
    .add_service(Service("Оформлення паспорту України", 1000))
    .add_service(Service("Оформлення загранпаспорту", 1500))
    .add_user(User("Іван", "Дмитрієв", "ivan@mail.com", "523443"))
    .add_user(User("Олена", "Петренко", "olena@mail.com", "123456")))

user1 = system.users[0]
user2 = system.users[1]
user1.make_order(system.services[0], system)

user2.make_order(system.services[1], system)

system.show_orders()

print(system.get_total_revenue())