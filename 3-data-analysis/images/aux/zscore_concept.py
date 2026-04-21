"""
Generates images/zscore_concept.png — a normal distribution diagram
annotated with per-band percentages and cumulative range arrows,
styled after the classic "empirical rule" chart.

Run from the notebook's root folder:
    python images/aux/zscore_concept.py
"""

import matplotlib
matplotlib.use("Agg")   # non-interactive backend — safe for scripts
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats
from pathlib import Path

OUTPUT = Path(__file__).parent.parent / "zscore_concept.png"

# ── Data ──────────────────────────────────────────────────────────────────
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x)

sigma_ticks = [-3, -2, -1, 0, 1, 2, 3]

# Colours: progressively lighter blue toward the tails (like the reference)
band_colors = {
    (-1,  1): "#4a6fa5",   # darkest — centre bands (±1σ)
    (-2, -1): "#7a9cc7",   # medium
    ( 1,  2): "#7a9cc7",
    (-3, -2): "#b0cce0",   # lightest — outer bands
    ( 2,  3): "#b0cce0",
}
tail_color = "#d6e8f5"     # beyond ±3σ

# Per-band percentage labels
band_labels = {
    (-1,  1): ("34.1 %", "34.1 %"),   # two halves drawn separately
    (-2, -1): "13.6 %",
    ( 1,  2): "13.6 %",
    (-3, -2): "2.1 %",
    ( 2,  3): "2.1 %",
}
tail_labels = {-3.5: "0.1 %", 3.5: "0.1 %"}

# ── Figure ────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

# Fill tails beyond ±3σ
for side in [-1, 1]:
    mask = x * side > 3
    ax.fill_between(x[mask], y[mask], color=tail_color, zorder=2)

# Fill each σ band
for (lo, hi), color in band_colors.items():
    mask = (x >= lo) & (x <= hi)
    ax.fill_between(x[mask], y[mask], color=color, zorder=3)

# Bell curve outline
ax.plot(x, y, color="#1a1a2e", linewidth=2.2, zorder=5)

# Vertical lines at each σ
for s in sigma_ticks:
    ax.axvline(s, color="white", linewidth=1.2, linestyle="-", zorder=4, alpha=0.8)

# ── Band percentage labels ────────────────────────────────────────────────
label_kw = dict(ha="center", va="center", fontsize=12, fontweight="bold",
                color="white", zorder=6)

for (lo, hi), label in band_labels.items():
    mid = (lo + hi) / 2
    y_mid = stats.norm.pdf(mid) * 0.55
    if isinstance(label, tuple):
        ax.text(lo / 2, y_mid, label[0], **label_kw)   # −1 to 0
        ax.text(hi / 2, y_mid, label[1], **label_kw)   # 0 to +1
    else:
        ax.text(mid, y_mid, label, **label_kw)

# Tail labels (dark text — too little space for white)
for pos, label in tail_labels.items():
    ax.text(pos, stats.norm.pdf(pos) + 0.005, label,
            ha="center", va="bottom", fontsize=10, color="#333333", zorder=6)

# ── X-axis tick labels ────────────────────────────────────────────────────
tick_labels = [r"$-3\sigma$", r"$-2\sigma$", r"$-1\sigma$",
               r"$\mu$",
               r"$+1\sigma$", r"$+2\sigma$", r"$+3\sigma$"]
ax.set_xticks(sigma_ticks)
ax.set_xticklabels(tick_labels, fontsize=13)
ax.set_xlim(-4.2, 4.2)
ax.set_ylim(-0.105, 0.44)

# Hide spines / default y-axis
ax.set_yticks([])
for spine in ["top", "left", "right"]:
    ax.spines[spine].set_visible(False)
ax.spines["bottom"].set_linewidth(1.2)

# ── Cumulative range arrows at the bottom ────────────────────────────────
arrow_y   = [-0.034, -0.060, -0.086]
arrow_x   = [(-1, 1), (-2, 2), (-3, 3)]
pct_labels = ["68.2 %", "95.4 %", "99.7 %"]
arrow_kw  = dict(arrowprops=dict(arrowstyle="<->", color="#1a1a2e", lw=1.4),
                 color="#1a1a2e", fontsize=11, ha="center", va="center",
                 fontweight="bold")

for (x0, x1), pct, ay in zip(arrow_x, pct_labels, arrow_y):
    mid = (x0 + x1) / 2
    # arrow
    ax.annotate("", xy=(x1, ay), xytext=(x0, ay),
                arrowprops=dict(arrowstyle="<->", color="#1a1a2e", lw=1.4))
    # label
    ax.text(mid, ay - 0.009, pct, ha="center", va="top",
            fontsize=11, color="#1a1a2e", fontweight="bold")

# ── Title ─────────────────────────────────────────────────────────────────
ax.set_title("The Normal Distribution", fontsize=16, fontweight="bold",
             color="#1a1a2e", pad=14)

plt.tight_layout()
plt.savefig(OUTPUT, dpi=150, bbox_inches="tight", facecolor="white")
print(f"Saved → {OUTPUT}")
