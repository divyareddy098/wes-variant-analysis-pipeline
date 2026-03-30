# 🧬 Whole-Exome Variant Analysis Pipeline (1000 Genomes)

## Project Goal
Built a complete bioinformatics pipeline to process whole-exome sequencing (WES) data from the 1000 Genomes Project, perform variant calling, and annotate coding variants for downstream genomic analysis.

---

## Overview
This project implements an end-to-end WES analysis workflow using standard NGS tools. The pipeline processes raw sequencing data through alignment, variant calling, filtering, and functional annotation.

The workflow reflects real-world pipelines used in clinical genomics and precision medicine applications.

---

## Workflow Overview

1. Read alignment to reference genome  
2. BAM processing and quality control  
3. Variant calling (SNVs and indels)  
4. Variant filtering  
5. Functional annotation of coding variants  

---

## Key Features

- Alignment of sequencing reads to reference genome  
- Variant calling for SNPs and indels using bcftools/GATK  
- Filtering of high-confidence variants based on quality metrics  
- Functional annotation of coding variants  
- End-to-end command-line pipeline using Bash and Linux tools  

---

## Project Structure

wes-variant-analysis/  
│── scripts/  
│── data/  
│── results/  
│── logs/  
│── README.md  

---

## Workflow Details

### 1️⃣ Alignment
- Aligned sequencing reads to the human reference genome (GRCh38)  
- Generated sorted and indexed BAM files using samtools  

### 2️⃣ BAM Processing
- Performed sorting and indexing  
- Assessed alignment quality  

### 3️⃣ Variant Calling
- Called variants (SNVs and indels) using bcftools / GATK  
- Generated VCF files  

### 4️⃣ Filtering
- Applied quality filters to retain high-confidence variants  
- Removed low-quality and low-depth calls  

### 5️⃣ Annotation
- Annotated variants to identify coding and functional impact  
- Generated annotated variant tables for downstream analysis  

---

## Outputs

- BAM files (aligned reads)  
- VCF files (raw and filtered variants)  
- Annotated variant datasets  
- Summary tables of coding variants  

---

## Tools & Technologies

- Bash / Linux  
- Python  
- samtools  
- bcftools  
- GATK (optional components)  

---

## Skills Demonstrated

- NGS data processing  
- Variant calling and filtering  
- Genomic data analysis  
- Command-line bioinformatics workflows  
- Pipeline development and reproducibility  

---

## Impact

This project demonstrates practical experience with variant analysis pipelines used in:

- Clinical genomics  
- Precision medicine  
- Variant interpretation and biomarker discovery  

---

## Author

Divya Reddy  
MS Bioinformatics, Georgia Institute of Technology  
