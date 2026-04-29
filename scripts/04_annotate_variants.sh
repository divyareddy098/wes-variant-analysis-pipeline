#!/bin/bash
set -euo pipefail

mkdir -p results/annotation logs

INPUT="results/vcf/chr22_region.filtered.vcf.gz"
OUTPUT="results/annotation/chr22_region.snpeff.vcf"

echo "Annotating variants with SnpEff..."

snpEff GRCh37.75 "$INPUT" > "$OUTPUT" 2> logs/snpeff_annotation.log

bgzip -f "$OUTPUT"
tabix -p vcf "${OUTPUT}.gz"

echo "Annotation complete:"
echo " - results/annotation/chr22_region.snpeff.vcf.gz"
echo " - logs/snpeff_annotation.log"
