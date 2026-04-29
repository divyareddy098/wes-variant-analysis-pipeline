import gzip
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

vcf_path = Path("results/annotation/chr22_region.snpeff.vcf.gz")
out_dir = Path("results/annotation")
fig_dir = Path("figures")
out_dir.mkdir(parents=True, exist_ok=True)
fig_dir.mkdir(parents=True, exist_ok=True)

records = []

with gzip.open(vcf_path, "rt") as f:
    for line in f:
        if line.startswith("#"):
            continue

        fields = line.strip().split("\t")
        chrom, pos, vid, ref, alt, qual, filt, info = fields[:8]

        ann_field = None
        for item in info.split(";"):
            if item.startswith("ANN="):
                ann_field = item.replace("ANN=", "")
                break

        if ann_field is None:
            continue

        annotations = ann_field.split(",")

        for ann in annotations:
            parts = ann.split("|")

            if len(parts) < 11:
                continue

            allele = parts[0]
            effect = parts[1]
            impact = parts[2]
            gene_name = parts[3]
            gene_id = parts[4]
            feature_type = parts[5]
            transcript_id = parts[6]
            biotype = parts[7]
            rank = parts[8]
            hgvs_c = parts[9]
            hgvs_p = parts[10]

            records.append({
                "CHROM": chrom,
                "POS": int(pos),
                "ID": vid,
                "REF": ref,
                "ALT": alt,
                "QUAL": float(qual) if qual != "." else None,
                "ALLELE": allele,
                "EFFECT": effect,
                "IMPACT": impact,
                "GENE": gene_name,
                "GENE_ID": gene_id,
                "BIOTYPE": biotype,
                "HGVS_C": hgvs_c,
                "HGVS_P": hgvs_p
            })

df = pd.DataFrame(records)

df.to_csv(out_dir / "annotated_variants_table.csv", index=False)

impact_summary = (
    df["IMPACT"]
    .value_counts()
    .reset_index()
)
impact_summary.columns = ["Impact", "Count"]
impact_summary.to_csv(out_dir / "impact_summary.csv", index=False)

effect_summary = (
    df["EFFECT"]
    .value_counts()
    .reset_index()
)
effect_summary.columns = ["Effect", "Count"]
effect_summary.to_csv(out_dir / "effect_summary.csv", index=False)

gene_summary = (
    df.groupby("GENE")
    .size()
    .reset_index(name="Variant_Count")
    .sort_values("Variant_Count", ascending=False)
)
gene_summary.to_csv(out_dir / "gene_variant_summary.csv", index=False)

plt.figure(figsize=(7, 5))
impact_summary.plot(
    x="Impact",
    y="Count",
    kind="bar",
    legend=False
)
plt.title("Predicted Variant Impact Distribution")
plt.xlabel("SnpEff Impact Category")
plt.ylabel("Variant Annotation Count")
plt.tight_layout()
plt.savefig(fig_dir / "variant_impact_distribution.png", dpi=300)
plt.close()

top_effects = effect_summary.head(10)

plt.figure(figsize=(9, 5))
top_effects.plot(
    x="Effect",
    y="Count",
    kind="bar",
    legend=False
)
plt.title("Top Variant Consequence Types")
plt.xlabel("Variant Consequence")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(fig_dir / "top_variant_effects.png", dpi=300)
plt.close()

top_genes = gene_summary.head(15)

plt.figure(figsize=(8, 6))
top_genes.plot(
    x="GENE",
    y="Variant_Count",
    kind="bar",
    legend=False
)
plt.title("Top Genes by Annotated Variant Count")
plt.xlabel("Gene")
plt.ylabel("Variant Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(fig_dir / "top_variant_genes.png", dpi=300)
plt.close()

print("Annotation summary complete")
print("Saved:")
print(" - results/annotation/annotated_variants_table.csv")
print(" - results/annotation/impact_summary.csv")
print(" - results/annotation/effect_summary.csv")
print(" - results/annotation/gene_variant_summary.csv")
print(" - figures/variant_impact_distribution.png")
print(" - figures/top_variant_effects.png")
print(" - figures/top_variant_genes.png")
