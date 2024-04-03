from math import tan, degrees, sin, cos, radians

from logic import Pump, Radiator, Fan

print("Насос")
test_Pump = Pump(Q_engine_to_radiator=184520, C_water=4187, Ro_water=1000, H_water=80000, n=2000)
print(test_Pump.G_water())
print(test_Pump.G_water_r())
print(test_Pump.r1())
print(test_Pump.u2())
print(test_Pump.r2())
print(test_Pump.u1())
print(test_Pump.beta1())
print(test_Pump.b1())
print(test_Pump.c2())
print(test_Pump.b2())
print(test_Pump.N())

print("Радиатор")
test_Radiator = Radiator(Q_engine_to_radiator=184520, G_water=0.0044, Ro_water=1000, T_water=10)
print(test_Radiator.G_air())
print(test_Radiator.G_water_m())
print(test_Radiator.T_average_water())
print(test_Radiator.F())

print("Вентилятор")
test_Fan = Fan(G_air=6.59, T_average_air=327)
print(test_Fan.Ro_air())
print(test_Fan.G1_air())
print(test_Fan.Ff())
print(test_Fan.D_fan())
print(test_Fan.u())
print(test_Fan.n())
print(test_Fan.N_fan())