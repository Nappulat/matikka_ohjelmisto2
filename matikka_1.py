import numpy as np

# Viikon Python osuus

a = 2.493
b = 0.911
c = 137.7
d = 62.3

print("Muunna radiaaneista asteiksi 1, Tehtävät 1.1, s 8-9:")
print(f"{a} rad = {np.degrees(a)} astetta, eli pyöristettynä {np.degrees(a):.1f} astetta")
print(f"{b} rad = {np.degrees(b)} astetta, eli pyöristettynä {np.degrees(b):.1f} astetta")
print(f"{c} rad = {np.radians(c)} rad, eli pyöristettynä {np.radians(c):.1f} rad")
print(f"{d} rad = {np.radians(d)} rad, eli pyöristettynä {np.radians(d):.1f} rad")
print("")

lista = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
for i in lista:
    print(f"{i} astetta = {np.radians(i):.2f} rad")
print("")

print("""Ratkaise hypotenuusan pituus 2, Tehtäviä 2.2.1, s 20:""")
np.hypot(1.6, 2.3, )
print(f"Suorakulmaisen kolmion kateetit ovat 1,6 m ja 2,3 m.")
print(f"Hypotenuusa on {np.hypot(1.6, 2.3)} m eli {np.hypot(1.6, 2.3):.2f} m")
print("")

print(np.degrees(np.arctan(2/3)))
x = (np.arctan(2/3))
print(f"kateetti 1: {np.sin(x)*6.4}, eli noin {np.sin(x)*6.4:.2f} m")
print(f"kateetti 2: {np.cos(x)*6.4}, eli noin {np.cos(x)*6.4:.2f} m")


