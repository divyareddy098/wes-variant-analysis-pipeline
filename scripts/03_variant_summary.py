import gzip
import pandas as pd
from pathlib import Path

vcf_path = Path("results/vcf/chr22_region.filtered.vcf.gz")
out_dir = Path("results/qc")
out_dir.mkdir(parents=True, exist_ok=True)

records = []

with gzip.open(vcf_path, "rt") as f:
    for line in f:
        if line.startswith("#"):
            continue

        fields = line.strip().split("\t")
        chrom, pos, vid, ref, alt, qual, filt, info = fields[:8]

        alts = alt.split(",")
        variant_type = "SNP" if len(ref) == 1 and all(len(a) == 1 for a in alts) else "INDEL/Complex"

        records.append({
            "CHROM": chrom,
            "POS": int(pos),
            "ID": vid,
            "REF": ref,
            "ALT": alt,
            "QUAL": float(qual) if qual != "." else None,
            "FILTER": filt,
            "Variant_Type": variant_type
        })

df = pd.DataFrame(records)

summary = pd.DataFrame({
    "Metric": [
        "Total variants",
        "SNPs",
        "INDEL/Complex",
        "Mean QUAL",
        "Min QUAL",
        "Max QUAL"
    ],
    "Value": [
        len(df),
        (df["Variant_Type"] == "SNP").sum(),
        (df["Variant_Type"] == "INDEL/Complex").sum(),
        round(df["QUAL"].mean(), 2) if len(df) else 0,
        round(df["QUAL"].min(), 2) if len(df) else 0,
        round(df["QUAL"].max(), 2) if len(df) else 0
    ]
})

df.to_csv("results/qc/filtered_variants_table.csv", index=False)
summary.to_csv("results/qc/variant_summary.csv", index=False)

print(summary)
print("Saved:")
print(" - results/qc/filtered_variants_table.csv")
print(" - results/qc/variant_summary.csv")
