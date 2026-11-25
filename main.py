"""The Agent's Uh-Oh entry: writes one uh-oh line to /output/entry.txt."""

import os

# Verified count: 83 characters (1 to 99, not only whitespace).
LINE = "Uh-oh. I pressed 'do not press', and now the printer is printing my search history."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "w", encoding="utf-8", newline="") as fh:
    fh.write(LINE)
