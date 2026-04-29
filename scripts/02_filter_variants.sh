#!/bin/bash
set -euo pipefail

mkdir -p results/vcf logs

INPUT="data/raw/chr22.1000g.vcf.gz"
REGION="22:20000000-21000000"

echo "Extracting region: $REGION"

bcftools view \
  -r "$REGION" \
  "$INPUT" \
  -Oz \
  -o results/vcf/chr22_region.raw.vcf.gz

tabix -p vcf results/vcf/chr22_region.raw.vcf.gz

echo "Filtering high-confidence variants..."

bcftools filter \
  -i 'QUAL>=30' \
  results/vcf/chr22_region.raw.vcf.gz \
  -Oz \
  -o results/vcf/chr22_region.filtered.vcf.gz

tabix -p vcf results/vcf/chr22_region.filtered.vcf.gz

echo "Done."
