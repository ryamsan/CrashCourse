from car import ElectricCar, Battery

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery = Battery(100)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
