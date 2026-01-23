"""
Plot Distances
Visualize distance to C across the domain [0, 35].

Run: python plot_distances.py
Requires: matplotlib (pip install matplotlib)
"""
import matplotlib.pyplot as plt

C = [0, 1, 2, 3, 5, 7, 9, 12, 15, 23, 30, 35]

def distance_to_C(x):
    return min(abs(x - c) for c in C)

# Generate data
xs = [i/10 for i in range(351)]
ds = [distance_to_C(x) for x in xs]

# Plot
plt.figure(figsize=(12, 4))
plt.plot(xs, ds, 'b-', linewidth=0.8)
plt.xlabel('Value')
plt.ylabel('Distance to nearest C element')
plt.title('Coralia Classification: Distance Landscape')

# Mark C elements
for c in C:
    plt.axvline(c, color='green', alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('distance_plot.png', dpi=150)
plt.show()

print("Saved: distance_plot.png")
