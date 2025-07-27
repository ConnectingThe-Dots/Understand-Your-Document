#!/usr/bin/env bash
set -euo pipefail

# Navigate to Challenge_1b root before running
python3 -m src.multi_processor \
  --config config/default.yaml \
  --collections-root .
