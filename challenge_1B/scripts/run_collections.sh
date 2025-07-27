#!/usr/bin/env bash
set -euo pipefail

# Navigate to the parent directory where challenge_1B package can be found
cd "$(dirname "$0")/../.."
python3 -m challenge_1B.src.multi_processor \
  --config challenge_1B/config/default.yaml \
  --collections-root challenge_1B/Challenge_1b
