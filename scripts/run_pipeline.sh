#!/bin/bash
set -e

echo "Starting WES pipeline..."

bash scripts/alignment.sh
bash scripts/variant_calling.sh
bash scripts/filtering.sh
bash scripts/annotation.sh

echo "Pipeline completed successfully!"
