# Purpose: Align reads to reference genome and generate BAM file

REFERENCE="data/reference/genome.fa"
FASTQ="data/sample.fastq"
OUTPUT="results/aligned.bam"

# Align reads 
bwa mem $REFERENCE $FASTQ | samtools view -Sb - > results/aligned_unsorted.bam

# Sort BAM
samtools sort results/aligned_unsorted.bam -o $OUTPUT

# Index BAM
samtools index $OUTPUT

echo "Alignment complete: $OUTPUT"
