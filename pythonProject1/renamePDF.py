import os
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_from_pdf(file_path):
    resource_manager = PDFResourceManager()
    file_handle = open(file_path, 'rb')
    converter = TextConverter(resource_manager, file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    full_text = ''
    for page in PDFPage.get_pages(file_handle, check_extractable=True):
        page_interpreter.process_page(page)
        full_text += converter.get_text()

    file_handle.close()
    converter.close()

    return full_text.strip()


def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)

            try:
                title = extract_text_from_pdf(file_path)
            except Exception as e:
                print(f'无法读取文件 {filename} 的内容: {str(e)}')
                continue

            if title:
                new_filename = title[:30] + '.pdf'
                new_filepath = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_filepath)
                print(f'将文件 {filename} 重命名为 {new_filename}')
            else:
                print(f'未找到标题，跳过文件 {filename}')

if __name__ == '__main__':
    folder_path = '/Users/coapeng/Desktop/person/三方打通资料'  # 替换为真实的文件夹路径
    rename_files(folder_path)