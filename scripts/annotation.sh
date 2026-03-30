# Purpose: Annotate variants using bcftools

INPUT_VCF="results/filtered_variants.vcf"
OUTPUT_VCF="results/annotated_variants.vcf"

bcftools annotate -x ID $INPUT_VCF -o $OUTPUT_VCF

echo "Annotation complete: $OUTPUT_VCF"
