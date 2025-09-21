# 代码生成时间: 2025-09-21 21:50:03
import pandas as pd

"""
Document Converter

This program converts documents between different formats using the pandas library.
It is designed to be easy to understand and maintain.
"""

class DocumentConverter:
    def __init__(self, input_file, output_file):
        """
        Initialize the DocumentConverter with input and output file paths.

        :param input_file: Path to the input file
        :param output_file: Path to the output file
        """
        self.input_file = input_file
        self.output_file = output_file

    def convert_to_csv(self):
        """
        Convert the input file to a CSV format.

        :return: A pandas DataFrame containing the data
        """
        try:
            # Read the input file into a pandas DataFrame
            df = pd.read_excel(self.input_file)
            # Write the DataFrame to a CSV file
            df.to_csv(self.output_file, index=False)
            print(f'Successfully converted {self.input_file} to {self.output_file}')
        except Exception as e:
            print(f'Error converting file: {e}')

    def convert_to_excel(self):
        """
        Convert the input file to an Excel format.

        :return: A pandas DataFrame containing the data
        """
        try:
            # Read the input file into a pandas DataFrame
            df = pd.read_csv(self.input_file)
            # Write the DataFrame to an Excel file
            df.to_excel(self.output_file, index=False)
            print(f'Successfully converted {self.input_file} to {self.output_file}')
        except Exception as e:
            print(f'Error converting file: {e}')

# Example usage
if __name__ == '__main__':
    input_file = 'input.xlsx'
    output_file = 'output.csv'
    converter = DocumentConverter(input_file, output_file)
    converter.convert_to_csv()

    input_file = 'input.csv'
    output_file = 'output.xlsx'
    converter = DocumentConverter(input_file, output_file)
    converter.convert_to_excel()