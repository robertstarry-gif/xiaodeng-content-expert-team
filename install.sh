#!/usr/bin/env sh
set -eu

SKILL_NAME="creator-content-expert-team"
REPO="${REPO:-robertstarry-gif/xiaodeng-content-expert-team}"
BRANCH="${BRANCH:-main}"
TARGET="all"

usage() {
  cat <<EOF
Usage: install.sh [--target all|codex|gpt-codex|hermes|openclaw|claude-code] [--repo owner/repo] [--branch branch]

Environment:
  DEST_DIR   Install to one explicit directory.
  REPO       GitHub owner/repo when running from a fork.
  BRANCH     Git branch to download. Defaults to main.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    --repo)
      REPO="${2:-}"
      shift 2
      ;;
    --branch)
      BRANCH="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 1
  }
}

copy_skill() {
  src="$1"
  dest="$2"

  mkdir -p "$(dirname "$dest")"
  rm -rf "$dest"
  mkdir -p "$dest"

  (
    cd "$src"
    for item in ./* ./.??*; do
      [ -e "$item" ] || continue
      case "$(basename "$item")" in
        .|..|.git|.DS_Store|creator-content-expert-team.zip)
          continue
          ;;
      esac
      cp -R "$item" "$dest/"
    done
  )

  echo "Installed $SKILL_NAME -> $dest"
}

script_dir=""
case "${0:-}" in
  */*)
    script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || true)
    ;;
esac

source_dir=""
if [ -n "$script_dir" ] && [ -f "$script_dir/SKILL.md" ]; then
  source_dir="$script_dir"
elif [ -n "$script_dir" ] && [ -f "$script_dir/../SKILL.md" ]; then
  source_dir=$(CDPATH= cd -- "$script_dir/.." && pwd)
fi

tmp_dir=""
if [ -z "$source_dir" ]; then
  if [ "$REPO" = "__GITHUB_REPO__" ]; then
    echo "Installer repo placeholder is not set. Use --repo owner/repo or set REPO=owner/repo." >&2
    exit 1
  fi

  need_cmd curl
  need_cmd unzip

  tmp_dir=$(mktemp -d)
  archive="$tmp_dir/source.zip"
  curl -fsSL "https://github.com/$REPO/archive/refs/heads/$BRANCH.zip" -o "$archive"
  unzip -q "$archive" -d "$tmp_dir"
  source_dir=$(find "$tmp_dir" -mindepth 1 -maxdepth 3 -type f -name SKILL.md -exec dirname {} \; | head -n 1)
fi

if [ -z "$source_dir" ] || [ ! -f "$source_dir/SKILL.md" ]; then
  echo "Could not locate SKILL.md in downloaded source." >&2
  exit 1
fi

if [ -n "${DEST_DIR:-}" ]; then
  copy_skill "$source_dir" "$DEST_DIR"
  [ -z "$tmp_dir" ] || rm -rf "$tmp_dir"
  exit 0
fi

install_codex() {
  copy_skill "$source_dir" "${CODEX_HOME:-$HOME/.codex}/skills/$SKILL_NAME"
}

install_hermes() {
  copy_skill "$source_dir" "${HERMES_HOME:-$HOME/.hermes}/skills/$SKILL_NAME"
}

install_openclaw() {
  if [ -d "${OPENCLAW_HOME:-$HOME/.openclaw}/workspace" ]; then
    copy_skill "$source_dir" "${OPENCLAW_HOME:-$HOME/.openclaw}/workspace/skills/$SKILL_NAME"
  else
    copy_skill "$source_dir" "${OPENCLAW_HOME:-$HOME/.openclaw}/skills/$SKILL_NAME"
  fi
}

install_claude_code() {
  copy_skill "$source_dir" "${CLAUDE_HOME:-$HOME/.claude}/skills/$SKILL_NAME"
}

case "$TARGET" in
  all)
    install_codex
    install_hermes
    install_openclaw
    install_claude_code
    ;;
  codex|gpt-codex)
    install_codex
    ;;
  hermes)
    install_hermes
    ;;
  openclaw)
    install_openclaw
    ;;
  claude-code|claude)
    install_claude_code
    ;;
  *)
    echo "Unknown target: $TARGET" >&2
    usage >&2
    exit 2
    ;;
esac

[ -z "$tmp_dir" ] || rm -rf "$tmp_dir"
