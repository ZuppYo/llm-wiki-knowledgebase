#!/usr/bin/env sh
# Resolve a working Python for wiki_tool (Git/Cursor hooks often lack python3 on PATH).
set -e

if [ -n "$PYTHON" ] && command -v "$PYTHON" >/dev/null 2>&1; then
  exec "$PYTHON" "$@"
fi

if command -v python3 >/dev/null 2>&1 && python3 -c "pass" 2>/dev/null; then
  exec python3 "$@"
fi

if command -v py >/dev/null 2>&1 && py -3 -c "pass" 2>/dev/null; then
  exec py -3 "$@"
fi

for candidate in \
  "/c/Python314/python.exe" \
  "/c/Python313/python.exe" \
  "/c/Python312/python.exe" \
  "/c/Python311/python.exe"; do
  if [ -x "$candidate" ]; then
    exec "$candidate" "$@"
  fi
fi

if command -v python >/dev/null 2>&1; then
  py_path=$(command -v python)
  case "$py_path" in
    *[Ww]indows[Aa]pps*|*[Mm]icrosoft*)
      ;;
    *)
      exec python "$@"
      ;;
  esac
fi

echo "wiki_python: no working Python found." >&2
echo "Install Python 3.9+ or set PYTHON to your python.exe path." >&2
exit 1
