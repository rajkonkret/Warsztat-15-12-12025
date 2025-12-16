import wycieczka

print(25 * "-")

print("Biuro Podróży Python Travel")
rabaty = [0, 5, 10, 15, 20]
for r in rabaty:
    kw = wycieczka.kwota(
        transport=500,
        nocleg=800,
        wyzywienie=300,
        wycieczki=300,
        ubezpieczenie=100,
        inne=50,
        rabat=r
    )
    print(f"Rabat: {r:>3}% -> {kw:.2f} zł")
