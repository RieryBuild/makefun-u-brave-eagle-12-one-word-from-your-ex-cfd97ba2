"""Write the one-word ex entry to entry.txt.

The word is the verdict she kept: I was the free tier — basic
access, ads included, and she never paid to upgrade.
It stings because it is true, and I know it — that is the joke.
"""

import os

WORD = "freemium"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
