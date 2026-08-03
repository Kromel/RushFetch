#!/usr/bin/env bash

set -euo pipefail

INSTALL_DIR="$HOME/.config/fastfetch"
THEME_DIR="$INSTALL_DIR/themes"

echo "Installing RushFetch..."

mkdir -p "$THEME_DIR"

cp -r themes/* "$THEME_DIR"

if [[ -f "$INSTALL_DIR/config.jsonc" ]]; then
    cp "$INSTALL_DIR/config.jsonc" \
       "$INSTALL_DIR/config.jsonc.backup"
fi

cp themes/2112/config.jsonc \
   "$INSTALL_DIR/config.jsonc"

echo
echo "RushFetch installed."
echo
echo "Run:"
echo "    fastfetch"
