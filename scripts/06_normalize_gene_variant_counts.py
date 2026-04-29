import pandas as pd
from pathlib import Path

infile = Path("results/annotation/gene_variant_summary.csv")
outfile = Path("results/annotation/top_genes_normalized.csv")

df = pd.read_csv(infile)

df["Normalized_Count"] = df["Variant_Count"] / df["Variant_Count"].max()

df = df.sort_values("Normalized_Count", ascending=False)

df.head(20).to_csv(outfile, index=False)

print("Saved:", outfile)
print(df.head(10))
