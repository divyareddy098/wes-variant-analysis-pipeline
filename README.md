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

## Results 

### Variant Counts

| Metric | Value |
|------|------|
| Raw variants | ~2,551 |
| Filtered variants | ~1,363 |
| SNPs | ~1,330 |
| Indels | ~33 |

---

### Functional Impact

| Impact | Count |
|--------|------|
| MODIFIER | 6,834 |
| LOW | 75 |
| MODERATE | 49 |
| HIGH | 15 |

---

### Top Variant Consequences

- Intronic variants dominate (~3,885)
- Regulatory variants (upstream/downstream) are common
- Missense variants (~49) represent functional coding changes
- Splice-related variants (~14) may affect gene expression

---

### Key Takeaway

The observed variant distribution aligns with expected biological patterns:
- Non-coding variation dominates
- Functional mutations are rare but important
- Coding variants provide the most biologically actionable insights

---

## Biological Insights

The pipeline was used to characterize genomic variation from sequencing data and extract biologically meaningful patterns.

### Key Findings

- Identified ~1,363 high-confidence variants after filtering
- Majority of variants are located in **non-coding regions**, consistent with genome-wide distributions
- Detected **49 missense variants and 14 splice-related variants**, representing potentially functional mutations
- High-impact variants are rare (15 total), reflecting evolutionary constraints on deleterious mutations

### Gene-Level Observations

- Variants were distributed across multiple genes, including MRTFA, DEPDC5, and ADA2
- Gene-level variation reflects a combination of gene size, genomic location, and sequencing coverage
- Highlights the importance of normalization in interpreting variant burden
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
