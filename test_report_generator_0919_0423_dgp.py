# 代码生成时间: 2025-09-19 04:23:48
import pandas as pd
import json
import os
from datetime import datetime

"""
Test Report Generator
This script is designed to generate a test report from a JSON file.
It reads a JSON file containing test results and outputs a test report in CSV format.
"""


class TestReportGenerator:
    def __init__(self, json_file_path):
        """
        Initialize the TestReportGenerator with a JSON file path.
        Args:
            json_file_path (str): The path to the JSON file containing test results.
        """
        self.json_file_path = json_file_path
        self.csv_file_path = self.json_file_path.replace('.json', '.csv')

    def read_json_file(self):
        """
        Read the JSON file and return the data as a dictionary.
        """
        try:
            with open(self.json_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The file {self.json_file_path} does not exist.")
            return None
        except json.JSONDecodeError:
            print(f"Error: The file {self.json_file_path} is not a valid JSON file.")
            return None

    def generate_csv_file(self, data):
        """
        Generate a CSV file from the test results data.
        Args:
            data (dict): The test results data.
        """
        if not data:
            print("Error: No test results data to generate a report.")
            return

        report_data = []
        for test_case, result in data.items():
            report_data.append([test_case, result['status'], result['message']])

        try:
            pd.DataFrame(report_data, columns=['Test Case', 'Status', 'Message']).to_csv(
                self.csv_file_path, index=False
            )
            print(f"Test report generated successfully: {self.csv_file_path}")
        except Exception as e:
            print(f"Error: Failed to generate test report. {str(e)}")

    def run(self):
        """
        Run the test report generator.
        """
        data = self.read_json_file()
        self.generate_csv_file(data)


if __name__ == '__main__':
    # Example usage
    json_file_path = 'test_results.json'
    if os.path.exists(json_file_path):
        generator = TestReportGenerator(json_file_path)
        generator.run()
    else:
        print(f"Error: The file {json_file_path} does not exist.")