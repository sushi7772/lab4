# Raport z analizy metodami MCDM

## 1. Konfiguracja analizy

- **Zastosowane metody**:  
  - TOPSIS  
  - SPOTIS  
  - VIKOR

- **Opis kryteriów**:  
  - Kryterium 1: Koszt (minimalizacja)  
  - Kryterium 2: Wydajność (maksymalizacja)  
  - Kryterium 3: Ryzyko (minimalizacja)

- **Alternatywy**:  
  - A1: [100, 50, 0.2]  
  - A2: [150, 70, 0.5]  
  - A3: [80, 40, 0.1]  
  - A4: [120, 60, 0.3]

- **Wagi wyznaczone metodą entropii**:  
  `[0.13649705, 0.1083927, 0.75511025]`  
  (największe znaczenie przypisano ryzyku)

---

## 2. Wyniki rankingów

| Alternatywa | TOPSIS | SPOTIS | VIKOR |
|-------------|--------|--------|--------|
| A1          | 3      | 3      | 3      |
| A2          | 1      | 1      | 1      |
| A3          | 4      | 4      | 4      |
| A4          | 2      | 2      | 2      |

---

## 3. Wnioski

Analiza metodami wielokryterialnymi (MCDM) wykazała wysoką zgodność rankingów pomiędzy zastosowanymi metodami: TOPSIS, SPOTIS i VIKOR. Alternatywa A2 osiągnęła najwyższe wyniki we wszystkich trzech metodach, co sugeruje, że jest to najkorzystniejszy wybór według zadanych kryteriów i wag.

Alternatywa A3  uzyskała najniższe wyniki, co wskazuje na jej nieatrakcyjność w kontekście analizowanych cech.

Zastosowanie wag entropicznych uwypukliło znaczenie  Ryzyka, które najbardziej różnicowało alternatywy i tym samym miało największy wpływ na końcowe decyzje.

