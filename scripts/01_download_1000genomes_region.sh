#!/bin/bash
set -euo pipefail

mkdir -p data/raw logs

URL="https://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz"

echo "Downloading 1000 Genomes chr22 VCF..."
curl -L "$URL" -o data/raw/chr22.1000g.vcf.gz

echo "Downloading index..."
curl -L "${URL}.tbi" -o data/raw/chr22.1000g.vcf.gz.tbi

echo "Done."
