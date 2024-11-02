import pandas as pd

def extract_saline_data(file_path):
    """
    Extract saline data from an Excel file.
    
    :param file_path: Path to the Excel file.
    :return: DataFrame containing the saline data.
    """
    data = pd.ExcelFile(file_path)
    
    if "Saline Storage" not in data.sheet_names:
        raise ValueError("Saline data sheet not found.")
    saline_data = pd.read_excel(file_path, sheet_name="Saline Storage")

    return saline_data

if  __name__ == '__main__':
    file_path = r"C:\Users\user\Desktop\excel-to-python-equations\Excel\Calculations_for_python.xlsx"
    saline_data = extract_saline_data(file_path)
    print(saline_data.columns)