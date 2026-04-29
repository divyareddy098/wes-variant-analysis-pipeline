import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

infile = Path("results/annotation/annotated_variants_table.csv")
outdir = Path("results/annotation")
figdir = Path("figures")

outdir.mkdir(parents=True, exist_ok=True)
figdir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(infile)

coding_effects = [
    "missense_variant",
    "synonymous_variant",
    "stop_gained",
    "frameshift_variant",
    "start_lost",
    "stop_lost",
    "splice_acceptor_variant",
    "splice_donor_variant"
]

coding_df = df[df["EFFECT"].isin(coding_effects)].copy()

summary = (
    coding_df["EFFECT"]
    .value_counts()
    .reset_index()
)

summary.columns = ["Consequence", "Count"]

summary.to_csv(outdir / "coding_variant_consequence_summary.csv", index=False)
coding_df.to_csv(outdir / "coding_variants_table.csv", index=False)

plt.figure(figsize=(8, 5))
plt.bar(summary["Consequence"], summary["Count"])
plt.title("Coding Variant Consequence Types")
plt.xlabel("Coding Variant Consequence")
plt.ylabel("Count")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(figdir / "coding_variant_consequences.png", dpi=300)
plt.close()

print("Saved:")
print(" - results/annotation/coding_variant_consequence_summary.csv")
print(" - results/annotation/coding_variants_table.csv")
print(" - figures/coding_variant_consequences.png")
print(summary)
