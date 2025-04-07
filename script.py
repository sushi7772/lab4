import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm import weights as mcdm_weights
import matplotlib.pyplot as plt

def custom_minmax_normalization(matrix, cost_flags):
    """Ręczna normalizacja min-max z uwzględnieniem kryteriów kosztowych."""
    normalized = np.zeros_like(matrix, dtype=float)
    for idx, is_cost in enumerate(cost_flags):
        col = matrix[:, idx]
        min_val, max_val = np.min(col), np.max(col)
        if max_val == min_val:
            normalized[:, idx] = 0  # brak zmienności = neutralne podejście
        elif is_cost:
            normalized[:, idx] = (max_val - col) / (max_val - min_val)
        else:
            normalized[:, idx] = (col - min_val) / (max_val - min_val)
    return normalized

# Etap 1: Zbieramy nasze dane decyzyjne
alternatives = ['A1', 'A2', 'A3', 'A4']
criteria = ['Koszt', 'Wydajność', 'Ryzyko']
decision_matrix = np.array([
    [100, 50, 0.2],
    [150, 70, 0.5],
    [80,  40, 0.1],
    [120, 60, 0.3]
])

# Etap 2: Definiujemy, co minimalizujemy, a co maksymalizujemy
types = np.array([-1, 1, -1])         # -1 = koszt, 1 = zysk
cost_flags = (types == -1)           # pomocniczy dla normalizacji

# Etap 3: Wagi - Entropia
weights = mcdm_weights.entropy_weights(decision_matrix)
print(f"\n Wagi (entropia): {weights.round(4)}")

# Etap 4: Normalizacja danych
normalized = custom_minmax_normalization(decision_matrix, cost_flags)

# Etap 5: TOPSIS
topsis = TOPSIS()
topsis_scores = topsis(normalized, weights, types)
topsis_rank = np.argsort(-topsis_scores) + 1
print("\n TOPSIS")
for alt, score, rank in zip(alternatives, topsis_scores, topsis_rank):
    print(f"{alt}: wynik = {score:.4f}, miejsce = {rank}")

# Etap 6: SPOTIS (z oryginalną macierzą + bounds)
bounds = np.column_stack((np.min(decision_matrix, axis=0), np.max(decision_matrix, axis=0)))
spotis = SPOTIS(bounds)
spotis_scores = spotis(decision_matrix, weights, types)
spotis_rank = np.argsort(-spotis_scores) + 1
print("\n SPOTIS")
for alt, score, rank in zip(alternatives, spotis_scores, spotis_rank):
    print(f"{alt}: wynik = {score:.4f}, miejsce = {rank}")


# Etap 7: VIKOR

vikor = VIKOR()
vikor_scores = vikor(normalized, weights, types)
vikor_rank = np.argsort(vikor_scores) + 1
print("\n VIKOR")
for alt, score, rank in zip(alternatives, vikor_scores, vikor_rank):
    print(f"{alt}: wynik = {score:.4f}, miejsce = {rank}")


# Etap 8: Wizualizacja

plt.figure(figsize=(10, 6))
plt.plot(alternatives, topsis_scores, marker='o', label='TOPSIS')
plt.plot(alternatives, spotis_scores, marker='s', label='SPOTIS')
plt.plot(alternatives, vikor_scores, marker='^', label='VIKOR')
plt.title(" Porównanie wyników metod MCDM", fontsize=14)
plt.xlabel("Alternatywy")
plt.ylabel("Wartości ocen")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('wyniki_porownanie.png')
plt.show()


# Etap 9: Podsumowanie rankingów

print("\n Podsumowanie rankingów:")
for i in range(len(alternatives)):
    print(f"{alternatives[i]} ➤ TOPSIS: {topsis_rank[i]}, SPOTIS: {spotis_rank[i]}, VIKOR: {vikor_rank[i]}")

