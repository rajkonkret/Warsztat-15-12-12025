# pandas - dane tabelaryczne
import pandas as pd

df = pd.DataFrame(
    {"Osoba": ["Michał JAkub", "Ewa Noga", "Krzysztof Zapadka"],
     "Wynik":[15, 38, 21]}
)

def sprawdz(punkty):
    if punkty > 20:
        return "zdany"
    else:
        return "oblany"

print(df)
#                Osoba  Wynik
# 0       Michał JAkub     15
# 1           Ewa Noga     38
# 2  Krzysztof Zapadka     21

df.Wynik = df.Wynik.apply(sprawdz)
print(df)
#                Osoba   Wynik
# 0       Michał JAkub  oblany
# 1           Ewa Noga   zdany
# 2  Krzysztof Zapadka   zdany

print(df.columns) # Index(['Osoba', 'Wynik'], dtype='object')
df.to_csv("wynik.csv")
df.to_excel("wyniki.xlsx")