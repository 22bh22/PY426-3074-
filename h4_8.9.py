#Спроектировать классы самолетов, по аналоги с автомобилями.
#У нас могут быть самолеты региональных,
#магистральный и дальних перелетов.
#Задайте атрибуты классов и экземпляров.
#Реализуйте методы для взлета, посадки и крейсерского полета
#+ возможность учета взет-посадок, и пройденой дистанции самолетами.
#Реализуйте логику учета потребляемого топлива каждым самолетом.

class Plane():
	brand = 'Airbus'
	takeoff_distance = 1
	landing_distance = 1
#12345678901234567890123456789012345678901234567890123456789012345678901
#11111111112222222222333333333344444444445555555555666666666677777777771
	def __init__(self, model=None):
		self.model = model
		self.fuel_level = 0
		self.total_distance = 0

	def to_landing(self, fuel_level, fuel_per_km):
		if fuel_per_km * self.landing_distance < fuel_level:
			self.total_distance += self.landing_distance
			self.fuel_level -= fuel_per_km * self.landing_distance
#12345678901234567890123456789012345678901234567890123456789012345678901
#11111111112222222222333333333344444444445555555555666666666677777777771
	def to_takeoff(self, fuel_level, total_distance, fuel_per_km):
		if fuel_per_km * self.takeoff_distance < fuel_level:
			self.total_distance += self.takeoff_distance
			self.fuel_level -= fuel_per_km * self.takeoff_distance
		
	def to_fly(self, fuel_level, fly_distance, fuel_per_km):
		if fuel_per_km * self.total_distance < fuel_level:
			self.total_distance += fly_distance
			self.fuel_level -= fuel_per_km * fly_distance
	
	def to_load_fuel(self, fuel_tank_capacity):
		self.fuel_tank_capacity = fuel_tank_capacity
		self.fuel_level = fuel_tank_capacity

class Regional(Plane):
	
	def __init__(self, model):
		super().__init__(model)
		self.type = 'Regional'
		self.fuel_per_km = 3
		self.fuel_tank_capacity = 3000
		self.fuel_level = self.fuel_level

class Magistral(Plane):
	def __init__(self, model):
		super().__init__(model)
		self.type = 'Magistral'
		self.fuel_per_km = 2
		self.fuel_tank_capacity = 10000
		self.fuel_level = self.fuel_level

class High_Range(Plane):
	def __init__(self, model):
		super().__init__(model)
		self.type = 'High_Range'
		self.fuel_per_km = 1
		self.fuel_tank_capacity = 20000
		#nonlocal fuel_level
		#self.fuel_level = fuel_level

golfstream = High_Range('golfstream-1')
#12345678901234567890123456789012345678901234567890123456789012345678901
#11111111112222222222333333333344444444445555555555666666666677777777771
print('Тип самолёта: ', golfstream.type, "\n",
'Расход топлива: ', golfstream.fuel_per_km, " л/км\n",
'Объём бака: ', golfstream.fuel_tank_capacity, " л", sep = "")
print('Производитель самолёта:', golfstream.brand)
print('Модель самолёта:', golfstream.model)
print('Текущий уровень топлива:', golfstream.fuel_level)
print('Пробег самолёта:', golfstream.total_distance)
golfstream.to_load_fuel(golfstream.fuel_tank_capacity)
print('Произведена заправка самолёта\nТекущий уровень топлива:',
golfstream.fuel_level)
print('Длинна взлётной полосы:', golfstream.takeoff_distance)
golfstream.to_takeoff(golfstream.fuel_level,
golfstream.total_distance, golfstream.fuel_per_km)
print('Взлёт\nТекущий уровень топлива:', golfstream.fuel_level,
'Пробег самолёта:', golfstream.total_distance)
golfstream.to_fly(golfstream.fuel_level, 1000, golfstream.fuel_per_km)
print('Полетели\nТекущий уровень топлива:', golfstream.fuel_level,
'Пробег самолёта:', golfstream.total_distance)
golfstream.to_landing(golfstream.fuel_level, golfstream.fuel_per_km)
print('Сели\nТекущий уровень топлива:', golfstream.fuel_level,
'Пробег самолёта:', golfstream.total_distance)
k1 = Magistral('111')
print(k1.total_distance)







input('Для завершения нажмите клавишу Enter...')
