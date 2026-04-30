# 🧬 Whole-Exome Sequencing (WES) Variant Analysis Pipeline (FASTQ-based)

## Project Goal
This project implements an **end-to-end bioinformatics pipeline** to process raw whole-exome sequencing (WES) data from FASTQ files, perform variant discovery, and analyze the functional consequences of genomic variation.

The objective is to replicate **real-world clinical genomics workflows** and demonstrate the ability to transform raw sequencing reads into **biologically meaningful insights**, focusing on variant characterization from human chromosome 22 (GRCh38 reference).

---

## Overview
This project presents a complete WES analysis workflow including:

- Processing of raw FASTQ sequencing reads  
- Quality control and subsampling for efficient computation  
- Read alignment to the human reference genome (GRCh38) using BWA  
- BAM processing (sorting, indexing) using SAMtools  
- Variant calling for SNPs and indels using bcftools (mpileup + call pipeline)  
- Quality-based filtering of variants  
- Functional annotation using SnpEff  
- Downstream analysis of variant impact and biological consequence  

This workflow reflects standard pipelines used in **genomics research and precision medicine**.

---

## Workflow Overview

1. FASTQ preprocessing (quality control and subsampling)  
2. Read alignment to reference genome (BWA)  
3. BAM processing (sorting, indexing)  
4. Variant calling (bcftools mpileup + call)  
5. Variant filtering (quality-based)  
6. Functional annotation (SnpEff)  
7. Variant impact and consequence analysis  

> **Note:** Duplicate marking and base quality score recalibration (BQSR) were not included in this implementation and can be incorporated in future extensions to align with clinical-grade pipelines.

---

## Key Features

- End-to-end WES pipeline from raw FASTQ data  
- Alignment using BWA  
- Variant calling using bcftools  
- Functional annotation using SnpEff  
- Automated execution via a single Bash script  
- Generation of interpretable biological summaries  
- Reproducible pipeline setup using Conda  

---

## Project Structure


wes-variant-analysis/
│── scripts/
│ └── run_fastq_wes_pipeline.sh
│
│── data/
│ ├── raw/
│ ├── raw_subsampled/
│ ├── reference/
│ └── processed/
│
│── results/
│ ├── vcf/
│ ├── annotation/
│
│── figures/
│── logs/
│── README.md


---

## Workflow Details

### FASTQ Processing
Raw sequencing reads were processed and subsampled to reduce computational cost while preserving representative variant signals.

---

### Alignment
Reads were aligned to the GRCh38 reference genome using BWA.  
SAM files were converted to BAM format, followed by sorting and indexing using SAMtools.

---

### Variant Calling
Variants (SNPs and indels) were identified using:

- bcftools mpileup  
- bcftools call  

Compressed and indexed VCF files were generated for downstream analysis.

---

### Variant Filtering
Quality-based filtering was applied to retain high-confidence variants:

- Minimum quality score: QUAL ≥ 20  

Additional filtering criteria (e.g., depth thresholds) can be incorporated for stricter variant selection.

---

### Annotation
Variants were annotated using SnpEff (GRCh38 database), classifying functional effects such as:

- Intronic  
- Missense  
- Synonymous  
- Splice-related  

---

## Results

### Variant Summary

| Metric | Value |
|------|------|
| Raw variants | ~2,551 |
| Filtered variants | ~1,363 |
| SNPs | ~1,330 |
| Indels | ~33 |

---

### Functional Impact Distribution

| Impact | Count |
|--------|------|
| MODIFIER | 6,834 |
| LOW | 75 |
| MODERATE | 49 |
| HIGH | 15 |

> **Note:** Functional impact counts exceed total variant counts because SnpEff reports annotations across multiple transcripts per variant.

---

### Top Variant Consequences

- Intronic variants dominate (~3,885), reflecting the prevalence of non-coding variation  
- Regulatory variants (upstream/downstream) are common  
- Missense variants (~49) represent functional coding changes  
- Splice-related variants (~14) may influence gene expression  

---

## Biological Insights

- Identified ~1,363 high-confidence variants after filtering  
- Majority of variants occur in non-coding regions, consistent with genome-wide expectations  
- Functional variants (missense, splice) are relatively rare but biologically important  
- High-impact variants (15 total) are uncommon, reflecting evolutionary constraints against deleterious mutations  

---

### Gene-Level Observations

Variants were observed across multiple genes, including:

- MRTFA  
- DEPDC5  
- ADA2  

These genes are associated with diverse biological processes. High-impact and coding variants within these genes may represent candidates for further functional or clinical investigation.

---

## Tools & Technologies

- Bash / Linux  
- Python  
- BWA  
- SAMtools  
- bcftools  
- SnpEff  

---

## Skills Demonstrated

- NGS data processing from raw FASTQ  
- Sequence alignment and BAM processing  
- Variant calling and filtering  
- Functional annotation of genomic variants  
- Interpretation of variant impact  
- Reproducible pipeline development  

---

## Impact

This project demonstrates workflows used in:

- Clinical genomics  
- Precision medicine  
- Variant prioritization  
- Biomarker discovery  

It highlights the ability to process raw sequencing data and identify **functionally relevant genomic variants**.

---

## Reproducibility

```bash
conda env create -f environment.yml
conda activate wes-variant-analysis

bash scripts/run_fastq_wes_pipeline.sh
```
---

## Author

- Divya Reddy
- MS Bioinformatics, Georgia Institute of Technology
