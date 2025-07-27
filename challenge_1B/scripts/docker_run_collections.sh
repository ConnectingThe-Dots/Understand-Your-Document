#!/usr/bin/env bash
set -euo pipefail

# Docker script to run collections processing
docker run --rm \
  --entrypoint="" \
  -v "$(pwd)/Challenge_1b:/app/challenge_1B/Challenge_1b" \
  -v "$(pwd)/config:/app/challenge_1B/config" \
  challenge_1b_image \
  python -m challenge_1B.src.multi_processor \
  --config challenge_1B/config/default.yaml \
  --collections-root challenge_1B/Challenge_1b
