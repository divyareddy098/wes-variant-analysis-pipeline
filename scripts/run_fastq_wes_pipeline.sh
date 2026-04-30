#!/bin/bash

set -e

echo "🚀 Starting FASTQ → WES Variant Pipeline"

# paths
FASTQ="data/raw_subsampled/SRR_100k_reads.fastq.gz"
REF="data/reference/chr22.fa"
OUTDIR="data/processed"
VCFDIR="results/vcf"
ANNODIR="results/annotation"
LOGDIR="logs"

mkdir -p $OUTDIR $VCFDIR $ANNODIR $LOGDIR

# Step 1: Alignment
echo "Aligning reads (BWA)..."
bwa mem $REF $FASTQ > $OUTDIR/aligned.sam 2> $LOGDIR/bwa.log


# Step 2: SAM → BAM
echo "Converting SAM → BAM..."
samtools view -bS $OUTDIR/aligned.sam > $OUTDIR/aligned.bam


# Step 3: Sorting
echo "Sorting BAM..."
samtools sort $OUTDIR/aligned.bam -o $OUTDIR/sorted.bam


# Step 4: Indexing
echo "Indexing BAM..."
samtools index $OUTDIR/sorted.bam


# Step 5: Variant Calling
echo "Calling variants..."
bcftools mpileup -f $REF $OUTDIR/sorted.bam | \
bcftools call -mv -Oz -o $VCFDIR/raw.vcf.gz

tabix -p vcf $VCFDIR/raw.vcf.gz


# Step 6: Filtering
echo "Filtering variants..."
bcftools filter -i 'QUAL>=20' $VCFDIR/raw.vcf.gz \
-Oz -o $VCFDIR/filtered.vcf.gz

tabix -p vcf $VCFDIR/filtered.vcf.gz

# Step 7: Annotation (SnpEff)
echo "Annotating variants (SnpEff)..."
snpEff -Xmx4g -noStats GRCh38.99 \
$VCFDIR/filtered.vcf.gz > $ANNODIR/annotated.vcf

bgzip -f $ANNODIR/annotated.vcf
tabix -p vcf $ANNODIR/annotated.vcf.gz

# Step 8: Summary
echo "Variant statistics..."
bcftools stats $VCFDIR/filtered.vcf.gz > $ANNODIR/variant_stats.txt

echo "done"
