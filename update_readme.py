import re
from pathlib import Path

readme = Path("README.md")
content = readme.read_text(encoding="utf-8")

# -----------------------------
# Count LeetCode Problems
# -----------------------------
leetcode_match = re.search(
    r"## 📘 LeetCode Solutions(.*?)(?=\n#{1,6}\s|\Z)",
    content,
    re.S,
)

leetcode_count = 0
if leetcode_match:
    table = leetcode_match.group(1)
    leetcode_count = len(re.findall(r"^\|\s*\d+\s*\|", table, re.M))

# -----------------------------
# Count GFG Problems
# -----------------------------
gfg_match = re.search(
    r"## 📙 GeeksforGeeks Solutions(.*?)(?=\n#{1,6}\s|\Z)",
    content,
    re.S,
)

gfg_count = 0
if gfg_match:
    table = gfg_match.group(1)
    gfg_count = len(re.findall(r"^\|\s*\d+\s*\|", table, re.M))

total = leetcode_count + gfg_count

new_progress = f"""## 📈 Progress

- ✅ Total Problems Solved: **{total}**
- 🟠 LeetCode: **{leetcode_count}**
- 🟢 GeeksforGeeks: **{gfg_count}**
"""

# -----------------------------
# Replace Progress Section
# -----------------------------
content = re.sub(
    r"## 📈 Progress.*?(?=\n#{1,6}\s|\Z)",
    new_progress,
    content,
    flags=re.S,
)

readme.write_text(content, encoding="utf-8")

print(f"Updated: Total={total}, LC={leetcode_count}, GFG={gfg_count}")
