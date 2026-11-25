ENTRY = "Here lies Ed. His last words: \"Hold my beer and watch this.\" The beer survived."

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
