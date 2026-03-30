# Purpose: Filter variants based on quality

INPUT_VCF="results/raw_variants.vcf"
OUTPUT_VCF="results/filtered_variants.vcf"

bcftools filter -i 'QUAL>30 && DP>10' $INPUT_VCF -o $OUTPUT_VCF

echo "Filtering complete: $OUTPUT_VCF"
