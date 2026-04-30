# 🧬 Whole-Exome Variant Analysis Pipeline (FASTQ-based)

## Project Goal
This project implements a complete end-to-end bioinformatics pipeline to process raw whole-exome sequencing (WES) data from FASTQ files, perform variant discovery, and analyze functional consequences of genomic variation.

The objective is to replicate real-world variant analysis workflows used in clinical genomics and derive biologically meaningful insights from sequencing data.

---

## Overview
This project presents a full WES analysis pipeline covering:

- Processing of raw FASTQ sequencing reads  
- Read alignment to the human reference genome (GRCh38) using BWA  
- BAM processing (sorting, indexing) using SAMtools  
- Variant calling for SNPs and indels using bcftools  
- Quality-based filtering of variants  
- Functional annotation using SnpEff  
- Downstream analysis of variant impact and consequence  

The workflow reflects standard pipelines used in research and precision medicine.

---

## Workflow Overview

1. FASTQ preprocessing (subsampling for efficient analysis)  
2. Read alignment to reference genome (BWA)  
3. BAM processing (sorting, indexing)  
4. Variant calling (bcftools)  
5. Variant filtering  
6. Functional annotation (SnpEff)  
7. Variant impact and consequence analysis  

---

## Key Features

- End-to-end WES pipeline from raw sequencing reads  
- Alignment using BWA  
- Variant calling using bcftools  
- Functional annotation using SnpEff  
- Automated pipeline execution via a single Bash script  
- Generation of biologically interpretable results  

---

## Project Structure


wes-variant-analysis/
│── scripts/ # Pipeline scripts
│ └── run_fastq_wes_pipeline.sh
│
│── data/
│ ├── raw/ # Original FASTQ files
│ ├── raw_subsampled/ # Subsampled FASTQ for efficient processing
│ ├── reference/ # Reference genome (chr22)
│ └── processed/ # BAM files
│
│── results/
│ ├── vcf/ # Variant call files
│ ├── annotation/ # Annotated variants and summaries
│
│── figures/ # Visualization outputs
│── logs/ # Pipeline logs
│── README.md


---

## Workflow Details

### FASTQ Processing
- Raw sequencing reads processed and subsampled for efficient computation  

### Alignment
- Reads aligned to GRCh38 reference genome using BWA  
- SAM converted to BAM, sorted, and indexed using SAMtools  

### Variant Calling
- SNPs and indels identified using bcftools  
- Compressed and indexed VCF files generated  

### Filtering
- Quality filtering applied (e.g., QUAL ≥ 20)  
- Retained high-confidence variants  

### Annotation
- Variants annotated using SnpEff (GRCh38 database)  
- Functional effects categorized (e.g., intronic, missense, synonymous)  

---

## Results and Biological Insights

### Variant Statistics

- ~2,551 raw variants identified  
- ~1,363 high-confidence filtered variants  
- ~1,330 SNPs and 33 indels  

These results are consistent with expected variant distributions in targeted genomic regions.

---

### Functional Impact Distribution

- Majority of variants fall under **MODIFIER impact**, indicating non-coding regions  
- Smaller proportions correspond to LOW, MODERATE, and HIGH impact variants  

This reflects expected biological patterns in human genomic variation.

---

### Variant Consequence Distribution

- Intronic and intergenic variants dominate the dataset  
- Regulatory variants (upstream/downstream) are common  
- Coding variants (missense, splice) represent a smaller but functionally significant subset  

---

### Gene-Level Variation

- Variants are distributed across multiple genes  
- Observed variation reflects gene length and genomic coverage  
- Supports downstream gene-level interpretation  

---

## Outputs

- Sorted and indexed BAM files  
- Filtered VCF files  
- Annotated VCF datasets  
- Variant statistics summaries  
- Functional impact and consequence summaries  

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
- Biological interpretation of sequencing data  
- Reproducible pipeline development  

---

## Impact

This project demonstrates workflows used in:

- Clinical genomics  
- Precision medicine  
- Variant interpretation  
- Biomarker discovery  

It highlights the ability to process raw sequencing data and extract biologically meaningful insights.

---

## Reproducibility

```bash
conda env create -f environment.yml
conda activate wes-variant-analysis

bash scripts/run_fastq_wes_pipeline.sh
```
---

## Author

Divya Reddy
MS Bioinformatics, Georgia Institute of Technology
