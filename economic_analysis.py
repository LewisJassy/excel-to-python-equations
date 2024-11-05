import pandas as pd
from scipy.optimize import newton

def extract_economic_data(file_path):
    """
    Extract economic data from an Excel file.
    
    :param file_path: Path to the Excel file.
    :return: DataFrame containing the economic data.
    """
    data = pd.ExcelFile(file_path)
    
    # Check if the required sheet is present in the Excel file
    if "Economic Analysis" not in data.sheet_names:
        raise ValueError("Economic data sheet not found.")
    
    # Read the data from the specified sheet
    economic_data = pd.read_excel(file_path, sheet_name="Economic Analysis")

    return economic_data

def calculate_npv(cash_flows, discount_rate):
    """
    Calculate the net present value (NPV) of a project.
    
    :param cash_flows: List of cash flows.
    :param discount_rate: Discount rate.
    :return: Net present value (NPV).
    """
    npv = sum(cf / (1 + discount_rate) ** i for i, cf in enumerate(cash_flows))
    return npv

def calculate_irr(cash_flows):
    """
    Calculate the internal rate of return (IRR) of a project.
    
    :param cash_flows: List of cash flows.
    :return: Internal rate of return (IRR).
    """
    irr =  newton(lambda r: calculate_npv(cash_flows, r), 0.1)
    return irr

def calculate_years_to_breakeven(cash_flows):
    """
    Calculate the number of years to breakeven for a project.
    
    :param cash_flows: List of cash flows.
    :return: Number of years to breakeven.
    """
    cumulative_cash_flow = 0
    for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        if cumulative_cash_flow >= 0:
            return i
    return None

def calculate_profitability_index(cash_flows, discount_rate):
    """
    Calculate the profitability index of a project.
    
    :param cash_flows: List of cash flows.
    :param discount_rate: Discount rate.
    :return: Profitability index.
    """
    npv = calculate_npv(cash_flows[1:], discount_rate)
    initial_investment = cash_flows[0]
    pi = npv / initial_investment
    return pi

def economic_analysis(file_path, project_life_years, discount_rate):
    economic_data = extract_economic_data(file_path)
    
    # Extract relevant columns
    revenue = economic_data.loc[economic_data['Variables'] == 'Revenue'].iloc[:, 4:4+project_life_years].values.flatten()
    capex = economic_data.loc[economic_data['Variables'] == 'Capex'].iloc[:, 4:4+project_life_years].values.flatten()
    opex = economic_data.loc[economic_data['Variables'] == 'Opex'].iloc[:, 4:4+project_life_years].values.flatten()
    
    cash_flows = []
    
    for year in range(project_life_years):
        if year == 0:
            cash_flow = -capex[year]
        else:
            cash_flow = revenue[year] - opex[year]
        cash_flows.append(cash_flow)
    
    npv = calculate_npv(cash_flows, discount_rate)
    irr = calculate_irr(cash_flows)
    years_to_breakeven = calculate_years_to_breakeven(cash_flows)
    pi = calculate_profitability_index(cash_flows, discount_rate)

    print("Economic Analysis Results:")
    print(f"NPV: {npv}")
    print(f"IRR: {irr}")
    print(f"Years to Breakeven: {years_to_breakeven}")
    print(f"Profitability Index: {pi}")
    
    # return {
    #     'NPV': npv,
    #     'IRR': irr,
    #     'Years to Breakeven': years_to_breakeven,
    #     'Profitability Index': pi
    # }
if __name__ == "__main__":
    file_path = r"C:\Users\user\Desktop\excel-to-python-equations\Excel\Calculations_for_python.xlsx"
    project_life_years = 10  # Update this with the actual project life years
    discount_rate = 0.1  # Update this with the actual discount rate

    economic_analysis(file_path, project_life_years, discount_rate)