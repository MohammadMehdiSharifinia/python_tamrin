# -*- coding: utf-8 -*-
"""
سیستم ساده مدیریت رستوران با برنامه‌ریزی هفتگی و پیگیری سفارشات
- 14 غذا (7 ایرانی، 7 بین‌المللی)
- روز پخت هر غذا
- ثبت سفارش، پرداخت، تحویل
- هشدار برای سفارش غذاهای غیرقابل سرو امروز
"""
from datetime import datetime

# Person base class
class Person:
    def __init__(self, id, name, role, perm=None, password=None):
        self.id = id
        self.name = name
        self.role = role
        self.perm = perm
        self.password = password

    def darkhast_merakhasi(self, date):
        return f"{self.name} darkhast merakhasi baraye {date}"

# Manager class
class Manager(Person):
    def __init__(self, id, name, password):
        super().__init__(id, name, "Manager", perm="All", password=password)
        self.food_menu = {}
        self.schedule = Schedule()

    def set_food(self, food):
        self.food_menu[food.name] = food
        return f"{food.name} ezafe shod"

    def report_menu(self):
        return {name: {'category': f.category, 'days': f.schedule} for name, f in self.food_menu.items()}

# Employee class
class Employee(Person):
    def __init__(self, id, name, password):
        super().__init__(id, name, "Employee", perm="Limited", password=password)

# Food class
class Food:
    def __init__(self, name, category, schedule_days):
        self.name = name
        self.category = category
        self.schedule = schedule_days  # list of weekdays
        self.quantity_available = 0

    def update_quantity(self, qty):
        self.quantity_available = qty
        return f"mojoodi {self.name}: {qty}"

    def decrement(self, qty):
        self.quantity_available = max(0, self.quantity_available - qty)
        return f"mojoodi {self.name} be {self.quantity_available} kashesh yaft"

# Schedule class
class Schedule:
    def __init__(self):
        self.plan = {}  # rooz: [food_names]

    def add(self, day, food_name):
        self.plan.setdefault(day, []).append(food_name)

    def get(self, day):
        return self.plan.get(day, [])

# check availability
def is_available_today(food_name, schedule, today):
    return food_name in schedule.get(today)

# Order class
class Order:
    def __init__(self, id, customer, food_name, qty, manager):
        self.id = id
        self.customer = customer
        self.food_name = food_name
        self.qty = qty
        self.order_time = datetime.now()
        self.paid = False
        self.status = 'sabt shode'
        self.manager = manager

    def pay(self):
        self.paid = True
        return f"sefaresh {self.id} pardakht shod"

    def deliver(self):
        if not self.paid:
            return "ebtedaa pardakht anjam shavad"
        food = self.manager.food_menu[self.food_name]
        self.status = 'tahvil shode'
        dec_msg = food.decrement(self.qty)
        return f"sefaresh {self.id} tahvil shod. {dec_msg}"

# Customer class
class Customer(Person):
    def __init__(self, id, name):
        super().__init__(id, name, "Customer")
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)
        return f"{self.name} sefaresh {order.id} sabt kard"

# Mesal estefade
if __name__ == "__main__":
    mgr = Manager(1, "Ali", "admin123")
    # tarif 14 ghaza va barnamerizi haftegi
    iranian = ['Tahchin','KashkBademjan','GhormehSabzi','Gheimeh','SabziPolo','Fesenjan','ZereshkPolo']
    international = ['Pizza','Burger','Sushi','Pasta','Tacos','Curry','Paella']
    schedule_map = {
        'Saturday': [iranian[0], international[0]],
        'Sunday': [iranian[1], international[1]],
        'Monday': [iranian[2], international[2]],
        'Tuesday': [iranian[3], international[3]],
        'Wednesday': [iranian[4], international[4]],
        'Thursday': [iranian[5], international[5]],
        'Friday': [iranian[6], international[6]]
    }
    for day, items in schedule_map.items():
        for name in items:
            cat = 'Iranian' if name in iranian else 'International'
            food = Food(name, cat, [day])
            food.update_quantity(10)
            mgr.set_food(food)
            mgr.schedule.add(day, name)

    # gozaresh menu
    menu = mgr.report_menu()
    print("------ menu kamel ------")
    for name, info in menu.items():
        print(f"{name}: category={info['category']}, rooz pokht={info['days']}")

    # tashkhis emrooz
    today = datetime.now().strftime('%A')
    todays = mgr.schedule.get(today)
    not_todays = [name for name in menu if name not in todays]

    print(f"\nemrooz ({today}) pokht mishavad:", todays)
    print("\nghaza haii ke emrooz pokht nemishavand:")
    for name in not_todays:
        day = menu[name]['days'][0]
        print(f"- {name}: rooz pokht {day}")

    # mesal1: sefaresh va tahvil ghaza pokhte
    if todays:
        fn = todays[0]
        cust1 = Customer(100, 'Mohammad')
        if is_available_today(fn, mgr.schedule, today):
            order1 = Order(1, cust1, fn, 2, mgr)
            print(cust1.place_order(order1))
            print(order1.pay())
            print(order1.deliver())

    # mesal2: talash baraye sefaresh ghaza gheyre pokhte
    if not_todays:
        fn2 = not_todays[0]
        cust2 = Customer(101, 'Sara')
        if not is_available_today(fn2, mgr.schedule, today):
            day = menu[fn2]['days'][0]
            print(f"! emkan sefaresh {fn2} nist. rooz pokht: {day}")

    # mesal3: sefaresh pardakht shode bedone tahvil
    if not_todays:
        fn3 = not_todays[1] if len(not_todays) > 1 else not_todays[0]
        cust3 = Customer(102, 'Reza')
        if not is_available_today(fn3, mgr.schedule, today):
            order3 = Order(3, cust3, fn3, 1, mgr)
            print(cust3.place_order(order3))
            print(order3.pay())
            # deliver nakarde

    print("\npayan mesal")
