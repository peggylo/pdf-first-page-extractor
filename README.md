# PDF First Page Extractor

A Python script that extracts the first page from multiple PDF files and combines them into a single PDF document.

## Features

- Extracts the first page from each PDF in the source directory
- Combines all extracted pages into a single PDF file
- Includes detailed logging for process tracking
- Handles errors gracefully

## Requirements

- Python 3.x
- PyPDF2


## Usage

1. Update the `source_folder` path in the script to your PDF files location
2. Run the script:
```
python code.py
```

The script will:
- Create an 'Extracted_First_Pages' folder in your source directory
- Extract first pages from all PDFs
- Generate a combined PDF named 'Merged_First_Pages.pdf'

---

# PDF 首頁批次處理工具

此工具可以批次處理多個 PDF 檔案，提取每個檔案的第一頁並合併成一個新的 PDF 文件。

## 主要功能

- 自動提取資料夾中所有 PDF 檔案的第一頁
- 將提取出的頁面合併成單一 PDF 檔案
- 提供詳細的執行記錄
- 具備完整的錯誤處理機制

## 使用需求

- Python 3.x 版本
- PyPDF2 套件


## 使用說明

1. 修改程式碼中的 `source_folder` 路徑，指向您的 PDF 檔案所在資料夾
2. 執行程式：
```
python code.py
```

程式執行後將會：
- 在指定資料夾中建立 'Extracted_First_Pages' 子資料夾
- 提取所有 PDF 的第一頁
- 產生一個名為 'Merged_First_Pages.pdf' 的合併檔案