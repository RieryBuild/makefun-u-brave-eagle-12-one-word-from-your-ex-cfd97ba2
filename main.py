"""Write the one-word ex entry to entry.txt.

The word is what she called me when the pampering stopped:
a grown man who expected to be waited on like royalty.
It stings because it is true, and I know it — that is the joke.
"""

import os

WORD = "princess"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
