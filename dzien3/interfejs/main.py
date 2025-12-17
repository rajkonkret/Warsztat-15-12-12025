from pojazd import Pojazd

p1 = Pojazd("Analiza spalania dla pojazdu z silnikiem 1.9 tdi")

odl = 587
jedn = 51
cj = 6.57

print(f"Spalanie [l/100km]: {p1.spalanie(odl, jedn):.2f}")
print(f"Koszt przejazdu na odcinku {odl} km wynosi: {p1.koszty_przejazdu(odl, jedn, cj):2f} pln")
# Spalanie [l/100km]: 8.69
# Koszt przejazdu na odcinku 587 km wynosi: 335.070000 pln
# https://naukapythona.com.pl/
