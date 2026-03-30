# Purpose: Call variants using bcftools

REFERENCE="data/reference/genome.fa"
BAM="results/aligned.bam"
VCF="results/raw_variants.vcf"

bcftools mpileup -f $REFERENCE $BAM | bcftools call -mv -o $VCF

echo "Variant calling complete: $VCF"
