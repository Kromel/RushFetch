#!/usr/bin/env bash

set -e

INSTALL_DIR="$HOME/.config/fastfetch"

rm -rf "$INSTALL_DIR/themes"

if [[ -f "$INSTALL_DIR/config.jsonc.backup" ]]; then
    mv \
      "$INSTALL_DIR/config.jsonc.backup" \
      "$INSTALL_DIR/config.jsonc"
fi

echo "RushFetch removed."
