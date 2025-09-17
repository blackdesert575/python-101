# import packages
from pypdf import PdfReader
import re

# open the pdf file
pdf_path = "./load/test.pdf"
reader = PdfReader(pdf_path)

# define key terms
keyword = "登記日期"
found = False

# extract text and search
for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    if not text:
        continue

    match = re.search(keyword, text)
    if match:
        found = True
        start = max(0, match.start() - 10)   # 關鍵字前10個字元
        end = min(len(text), match.end() + 10)  # 關鍵字後10個字元
        context = text[start:end].replace("\n", "")
        print(f"✅ 找到「{keyword}」在第 {i} 頁: ...{context}...")

if not found:
    print(f"❌ PDF 中沒有找到關鍵字「{keyword}」。")