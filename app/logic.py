# Кол-во тепла, отводимого от двигателя
# и передадаемого отводы к охлаждающему воздуху
# Qвозд = Qв = 184 520 Дж/с
# Средняя теплоемкость воздуха
# Свозд = 1000 Дж/(кг * К)
# Объемный расход воды, проходящей
# через радиатор, по данным №81
# Gж = 0.0044 м^3/с
# Средняя плотность воды
# (ро)ж = 1000 кг/м^3
# (дельта)Твозд = 28К
from math import sqrt, tan, atan, pi, sin, degrees, radians


# Pump - Расчет водяного насоса
# Q_engine_to_radiator: Qв(Дж/с) - кол-во тепла, отводимого от двигателя и передаваемого от воды к охлаждающему воздуху,
# С_water: Сж(Дж/кг*К) - средняя теплоемкость жидкости,
# Ro_water: ρж(кг/м^3) - средняя плотность воды,
# H_water: Pж(Па) - Напор, создаваемый насосом
# n: nви (об/мин) - Частота вращения насоса
# T: ΔT(К) - Температурный перепад воды при принудительной циркуляции
# KPD: η - коэффициент подачи насоса
# c1: c1(м/с) - скорость воды на входе в насос
# r0: r0(м) - радиус ступицы крыльчатки
# alpha2: α2(градусы) - угол между направлением скорости c2 (8-12)
# beta2: β2(градусы) - угол между направлением скорости w2 (12-50)
# KPD_pump: ηh - гидравлический КПД насоса
# z: z(шт) - кол-во лопаток
# thickness: δ(м) - толщина лопатки у входа
# KPD_m: ηм - механический КПД водяного насоса
class Pump:
    def __init__(self, Q_engine_to_radiator, C_water, Ro_water, H_water, n):
        self.Q_engine_to_radiator = Q_engine_to_radiator
        self.C_water = C_water
        self.Ro_water = Ro_water
        self.H_water = H_water
        self.n = n
        self.T = 10
        self.KPD = 0.84
        self.c1 = 1.7
        self.r0 = 0.02
        self.alpha2 = 8
        self.beta2 = 40
        self.KPD_pump = 0.66
        self.z = 6
        self.thickness = 0.004
        self.KPD_m = 0.84

    # Циркуляционный расход жидкости в системе охлаждения
    # Gж(м^3/c)
    def G_water(self) -> float:
        return round(self.Q_engine_to_radiator / (self.C_water * self.Ro_water * self.T), 4)

    # Расчетная производительность насоса
    # Gж.р(м^3/с)
    def G_water_r(self):
        return round(self.G_water() / self.KPD, 4)

    # Радиус входного отверстия крыльчатки
    # r1(м)
    def r1(self):
        return round(sqrt((self.G_water_r() / (pi * self.c1)) + self.r0 ** 2), 3)

    # Окружная скорость потока воды на выходе из колеса
    # u2(м/с)
    def u2(self):
        return round((sqrt(1 + (tan(radians(self.alpha2)) * (1 / tan(radians(self.beta2))))) * sqrt(self.H_water / (self.Ro_water * self.KPD_pump))), 2)

    # Радиус крыльчатки колеса на выходе
    # r2(м)
    def r2(self):
        return round((30 * self.u2()) / (pi * self.n), 3)

    # Окружная скорость входа потока
    # u1(м/с)
    def u1(self):
        return round((self.u2() * self.r1()) / self.r2(), 3)

    # Угол между скоростями c1 и u1 принимается = 90(градусы) при этом
    # tgβ1
    def beta1(self):
        return round(self.c1 / self.u1(), 5)

    # Ширина лопатки на входе
    # b1(м)
    def b1(self):
        return round(self.G_water_r() / (((2*pi*self.r1())-(self.z * self.thickness / sin(self.beta1())))*self.c1), 4)

    # Радиальная скорость потока на выходе из колеса
    # c2(м/с)
    def c2(self):
        return round((self.H_water * tan(radians(self.alpha2))) / (self.Ro_water * self.KPD_pump * 11.9), 2)

    # Ширина лопатки на выходе
    # b2(м)
    def b2(self):
        return round(self.G_water_r() / (((2*pi*self.r2())-(self.z * self.thickness / sin(self.beta2)))*self.c2()), 4)

    # Мощность, потребляемая водяным насосом
    # Nв.н(КВт)
    def N(self):
        return round((self.G_water_r()*self.H_water)/(1000*self.KPD_m), 3)


# Расчет поверхности охлаждения водяного радиатора
# Radiator - water radiator cooling surface
# Q_engine_to_radiator: decimal Qв(Дж/с) - кол-во тепла, отводимого от двигателя и передаваемого от воды к охлаждающему воздуху
# G_water: Gж(м^3/c) - объемный расход воды, порходящий через радиатор,
# C_air: Свозд(Дж/кг*К) - средняя теплоемкость воздуха,
# Ro_water: ρ(кг/м^3) - средняя плотность воды,
# T_air: ΔT(К) - температурный перепад воздуха в решетке радиатора
# T_water: ΔT(К) - Температурный перепад воды при принудительной циркуляции (берется из расчета насоса)
# T_average_air: Tср.возд(K) - средняя температура охлаждающего воздуха, проходящего через радиатор (325-328)
class Radiator:
    def __init__(self, Q_engine_to_radiator, G_water, Ro_water, T_water):
        # есть в расчете насоса
        self.Q_engine_to_radiator = Q_engine_to_radiator
        self.G_water = G_water
        self.Ro_water = Ro_water
        self.T_water = T_water
        self.C_air = 1000
        self.T_air = 28
        self.T_average_air = 327

    # Кол-во воздуха, проходящего через радиатор
    # G'возд(кг/c)
    def G_air(self) -> float:
        return self.Q_engine_to_radiator / (self.C_air * self.T_air)

    # Массовый расход воды, проходящий черед радиатор
    # G'ж(кг/c)
    def G_water_m(self) -> float:
        return self.G_water * self.Ro_water

    # Средняя температура воды в радиаторе
    # Tср.вод(К)
    def T_average_water(self) -> float:
        return (365 + (365 - self.T_water)) / 2

    # Поверхность охлаждения радиатора
    # F(м^2)
    def F(self) -> float:
        return round(self.Q_engine_to_radiator / (100 * (self.T_average_water() - self.T_average_air)), 0)


# G_air :G'возд(кг/c) Кол-во воздуха, проходящего через радиатор (Pump)
# T_average_air: Tср.возд(K) - средняя температура охлаждающего воздуха, проходящего через радиатор (325-328)(Pump)
# H_air: ΔPт.р.(Па) - Напор создаваемый вентилятором (конст 800Па)
# w_air: wв(м/c) - скорость воздуха перед фронтом вентилятора без учета скорости авто (конст 20м/c)
# Fi: φ - безразмерный коэффициент для плоских лопастей
class Fan():
    def __init__(self, G_air, T_average_air):
        self.G_air = G_air
        self.T_average_air = T_average_air
        self.H_air = 900
        self.w_air = 10
        self.Fi = 3.41

    # Плотность воздуха при средней его температуре в радиаторе
    # ρвозд(кг/м^3)
    def Ro_air(self):
        return round(100000/(287*self.T_average_air), 2)

    # Производительность вентилятора
    # Gвозд(м^3/с)
    def G1_air(self):
        return round(self.G_air/self.Ro_air(), 2)

    # Фронтовая поверхность радиатора
    # Fфр.рад(м^2)
    def Ff(self):
        return round(self.G1_air()/self.w_air, 2)

    # Диаметр вентилятора
    # Dвент(м)
    def D_fan(self):
        return round(2*sqrt(self.Ff()/pi), 1)

    # Окружная скорость вентилятора
    # u(м/с)
    def u(self):
        return round(self.Fi*sqrt(self.H_air/self.Ro_air()), 2)

    # Частота вращения вентилятора с раздельным приводом
    # мин-1
    def n(self):
        return round((60*self.u())/(pi*self.D_fan()), 1)

    # Мощность, затрачиваемая на привод осевого вентилятора
    # N(кВт)
    def N_fan(self):
        return round((self.G1_air()*self.H_air)/(1000*0.6), 2)


