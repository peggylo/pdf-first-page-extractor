import os
import re
from PyPDF2 import PdfReader, PdfWriter
import logging

# 設置日誌
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 定義源資料夾和目標資料夾路徑
source_folder = r'在這裡寫你的檔案資料夾路徑'
target_folder = os.path.join(source_folder, 'Extracted_First_Pages')

# 確保目標資料夾存在
os.makedirs(target_folder, exist_ok=True)

# 檢查源資料夾是否存在
if not os.path.exists(source_folder):
    logging.error(f"源資料夾不存在: {source_folder}")
    exit(1)

# 獲取所有 PDF 文件
pdf_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.pdf')]
logging.info(f"在源資料夾中找到 {len(pdf_files)} 個 PDF 文件")

# 如果沒有找到任何 PDF 文件，退出程式
if not pdf_files:
    logging.error("沒有找到任何 PDF 文件")
    exit(1)

# 提取並保存每個PDF的第一頁
extracted_files = []
for file in sorted(pdf_files):
    file_path = os.path.join(source_folder, file)
    logging.info(f"正在處理文件: {file}")
   
    try:
        # 讀取 PDF 文件
        reader = PdfReader(file_path)
       
        # 如果 PDF 至少有一頁，則提取第一頁
        if len(reader.pages) > 0:
            writer = PdfWriter()
            writer.add_page(reader.pages[0])
           
            # 保存提取的第一頁
            output_filename = f"extracted_{file}"
            output_path = os.path.join(target_folder, output_filename)
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            extracted_files.append(output_filename)
            logging.info(f"已提取並保存: {output_filename}")
        else:
            logging.warning(f"文件 {file} 沒有頁面")
    except Exception as e:
        logging.error(f"處理文件 {file} 時發生錯誤: {str(e)}")

# 如果沒有成功提取任何頁面，退出程式
if not extracted_files:
    logging.error("沒有成功提取任何頁面")
    exit(1)

# 合併所有提取的第一頁
merged_pdf = PdfWriter()

for file in extracted_files:
    file_path = os.path.join(target_folder, file)
    try:
        reader = PdfReader(file_path)
        merged_pdf.add_page(reader.pages[0])
        logging.info(f"已添加 {file} 到合併文件")
    except Exception as e:
        logging.error(f"合併文件 {file} 時發生錯誤: {str(e)}")

# 保存合併後的 PDF
output_path = os.path.join(target_folder, 'Merged_First_Pages.pdf')
try:
    with open(output_path, 'wb') as output_file:
        merged_pdf.write(output_file)
    logging.info(f"合併完成。新文件保存在: {output_path}")
except Exception as e:
    logging.error(f"保存合併文件時發生錯誤: {str(e)}")