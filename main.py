import math
from oktagon import oktagon

def main():
  NewOktagon = oktagon(10)
  perimeter, square = NewOktagon.Oktagon_data()
  radius_opis, square_opis = NewOktagon.described_circle()
  radius_vpis, square_vpis = NewOktagon.incribed_circle()
  print("Данные об октагоне")
  print(f"Периметр: {perimeter:.2f}")
  print(f"Площадь: {square:.2f}")
  print(f"\n--- Описанная окружность ---")
  print(f"Радиус: {radius_opis:.2f}")
  print(f"Площадь: {square_opis:.2f}")
  print(f"\n--- Вписанная окружность ---")
  print(f"Радиус: {radius_vpis:.2f}")
  print(f"Площадь: {square_vpis:.2f}")
  NewOktagon.draw()


if __name__=="__main__":
    main()