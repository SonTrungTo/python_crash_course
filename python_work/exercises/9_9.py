# Battery Upgrade
from car import Car

print("Creating an electric car with a default battery size...")
my_electric_car = Car('tesla', 'model s', 2020)
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
print("\nUpgrading the battery...")
my_electric_car.battery.upgrade_battery()
print("\nChecking the battery size after upgrade...")
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
