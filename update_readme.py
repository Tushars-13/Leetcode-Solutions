import re
from pathlib import Path

readme = Path("README.md")

content = readme.read_text(encoding="utf-8")

# Extract the LeetCode Solutions table
leetcode_match = re.search(
    r"## 📘 LeetCode Solutions(.*?)(?=\n## |\Z)",
    content,
    re.S,
)

leetcode_count = 0
if leetcode_match:
    table = leetcode_match.group(1)
    leetcode_count = len(re.findall(r"^\|\s*\d+\s*\|", table, re.M))

# Extract the GFG Solutions table
gfg_match = re.search(
    r"## 📙 GeeksforGeeks Solutions(.*?)(?=\n## |\Z)",
    content,
    re.S,
)

gfg_count = 0
if gfg_match:
    table = gfg_match.group(1)
    gfg_count = len(re.findall(r"^\|\s*GFG\s*\|", table, re.M))

total = leetcode_count + gfg_count

new_progress = f"""## 📈 Progress

- ✅ Total Problems Solved: **{total}**
- 🟠 LeetCode: **{leetcode_count}**
- 🟢 GeeksforGeeks: **{gfg_count}**
"""

# Replace the Progress section
content = re.sub(
    r"## 📈 Progress.*?(?=\n## |\Z)",
    new_progress,
    content,
    flags=re.S,
)

readme.write_text(content, encoding="utf-8")

print("README Progress Updated Successfully!")
