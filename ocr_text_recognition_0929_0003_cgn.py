# 代码生成时间: 2025-09-29 00:03:16
import pandas as pd
from PIL import Image
import pytesseract

# 配置pytesseract的路径
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

class OcrTextRecognition:
    def __init__(self, image_path):
        """
        初始化OCR对象
        :param image_path: 图像文件路径
        """
        self.image_path = image_path
        self.image = Image.open(image_path)

    def extract_text(self):
        """
        提取图像中的文本
        :return: 图像中的文本
        """
        try:
            # 使用pytesseract提取图像中的文本
            text = pytesseract.image_to_string(self.image)
            # 返回提取的文本
            return text
        except Exception as e:
            # 处理提取文本过程中可能出现的错误
            print(f"Error extracting text: {e}")
            return None

    def save_text_to_file(self, output_path):
        """
        将提取的文本保存到文件
        :param output_path: 输出文件路径
        """
        try:
            text = self.extract_text()
            if text is not None:
                # 保存文本到文件
                with open(output_path, 'w') as file:
                    file.write(text)
                print(f"Text saved to {output_path}")
            else:
                print("No text extracted")
        except Exception as e:
            # 处理保存文本过程中可能出现的错误
            print(f"Error saving text to file: {e}")

# 示例用法
if __name__ == '__main__':
    image_path = 'example_image.jpg'  # 图像文件路径
    output_path = 'output_text.txt'  # 输出文件路径
    
    try:
        ocr = OcrTextRecognition(image_path)
        ocr.save_text_to_file(output_path)
    except Exception as e:
        print(f"Error in OCR process: {e}")