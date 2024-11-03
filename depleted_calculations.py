import pandas as pd

def extract_depleted_data(file_path):
    """
    Extract depleted data from an Excel file.
    
    :param file_path: Path to the Excel file.
    :return: DataFrame containing the depleted data.
    """
    data = pd.ExcelFile(file_path)
    
    # Check if the required sheet is present in the Excel file
    if "Depleted Field Storage" not in data.sheet_names:
        raise ValueError("Depleted data sheet not found.")
    
    # Read the data from the specified sheet
    depleted_data = pd.read_excel(file_path, sheet_name="Depleted Field Storage")

    return depleted_data

def calculate_gas_produced_rb(gas_produced, Bg):
    """
    Calculate the gas produced in reservoir barrels (Rb).
    
    :param gas_produced: Gas produced in MMscf.
    :param Bg: Gas formation volume factor.
    :return: Gas produced in Rb.
    """
    return gas_produced * Bg * 1000  # Rb

def calculate_solution_gas_produced_rb(original_gas_in_place, gas_produced, Bg):
    """
    Calculate the solution gas produced in reservoir barrels (Rb).
    
    :param original_gas_in_place: Original gas in place in MMscf.
    :param gas_produced: Gas produced in MMscf.
    :param Bg: Gas formation volume factor.
    :return: Solution gas produced in Rb.
    """
    return (original_gas_in_place - gas_produced) * Bg * 1000  # Rb

def calculate_reservoir_bbl_produced_rb(oil_produced, formation_oil_factor):
    """
    Calculate the reservoir barrels (Rb) produced from oil.
    
    :param oil_produced: Oil produced in barrels.
    :param formation_oil_factor: Formation oil volume factor.
    :return: Reservoir barrels produced in Rb.
    """
    return oil_produced * formation_oil_factor  # Rb

def calculate_total_fluid_rb(gas_produced_rb, water_produced, reservoir_bbl_produced_rb):
    """
    Calculate the total fluid produced in reservoir barrels (Rb).
    
    :param gas_produced_rb: Gas produced in Rb.
    :param water_produced: Water produced in barrels.
    :param reservoir_bbl_produced_rb: Reservoir barrels produced from oil in Rb.
    :return: Total fluid produced in Rb.
    """
    return gas_produced_rb + water_produced + reservoir_bbl_produced_rb  # Rb

def calculate_total_fluid_kg(total_fluid_rb, CO2_density):
    """
    Calculate the total fluid produced in kilograms (kg).
    
    :param total_fluid_rb: Total fluid produced in Rb.
    :param CO2_density: Density of CO2 in kg/m³.
    :return: Total fluid produced in kg.
    """
    return total_fluid_rb * CO2_density  # kg

def calculate_storage_capacity(original_oil_in_place, original_gas_in_place, CO2_density):
    """
    Calculate the storage capacity of the depleted field.
    
    :param original_oil_in_place: Original oil in place in barrels.
    :param original_gas_in_place: Original gas in place in MMscf.
    :param CO2_density: Density of CO2 in kg/m³.
    :return: Storage capacity in metric tons.
    """
    # Convert original gas in place from MMscf to barrels
    original_gas_in_place_bbl = original_gas_in_place * 1000 / 5.615
    total_fluid_bbl = original_oil_in_place + original_gas_in_place_bbl
    
    # Convert total fluid to kg
    total_fluid_kg = total_fluid_bbl * 0.159 * 1000  # 1 barrel = 0.159 cubic meters
    
    # Calculate storage capacity
    storage_capacity = total_fluid_kg / CO2_density
    return storage_capacity

def is_numeric(value):
    """
    Check if a value is numeric.
    
    :param value: The value to check.
    :return: True if the value is numeric, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False

def main():
    file_path = r"C:\Users\user\Desktop\excel-to-python-equations\Excel\Calculations_for_python.xlsx"
    depleted_data = extract_depleted_data(file_path)
    
    # Check if the required data is present
    required_fields = [
        'Original Oil in Place', 'Original Gas in Place', 'Gas Produced', 
        'Oil produced', 'Water Produced', 'Bg', 'Formation Oil Factor', 'CO2 Density'
    ]
    
    for field in required_fields:
        if depleted_data.loc[depleted_data['Unnamed: 2'] == field].empty:
            raise ValueError(f"Required field '{field}' not found in the data.")
    
    def get_numeric_value(field):
        value = depleted_data.loc[depleted_data['Unnamed: 2'] == field, 'Unnamed: 4'].values[0]
        if not is_numeric(value):
            raise ValueError(f"Value for '{field}' is not numeric: {value}")
        return float(value)
    
    original_oil_in_place = get_numeric_value('Original Oil in Place')
    # print(original_oil_in_place)
    original_gas_in_place = get_numeric_value('Original Gas in Place')
    gas_produced = get_numeric_value('Gas Produced')
    oil_produced = get_numeric_value('Oil produced')
    water_produced = get_numeric_value('Water Produced')
    # print(water_produced)
    Bg = get_numeric_value('Bg')
    formation_oil_factor = get_numeric_value('Formation Oil Factor')
    CO2_density = get_numeric_value('CO2 Density')
    
    gas_produced_rb = calculate_gas_produced_rb(gas_produced, Bg)
    solution_gas_produced_rb = calculate_solution_gas_produced_rb(original_gas_in_place, gas_produced, Bg)
    reservoir_bbl_produced_rb = calculate_reservoir_bbl_produced_rb(oil_produced, formation_oil_factor)
    total_fluid_rb = calculate_total_fluid_rb(gas_produced_rb, water_produced, reservoir_bbl_produced_rb)
    total_fluid_kg = calculate_total_fluid_kg(total_fluid_rb, CO2_density)
    storage_capacity = calculate_storage_capacity(original_oil_in_place, original_gas_in_place, CO2_density)

    # return storage_capacity
    
    print(f"Gas Produced (Rb): {gas_produced_rb}")
    print(f"Solution Gas Produced (Rb): {solution_gas_produced_rb}")
    print(f"Reservoir BBL Produced (Rb): {reservoir_bbl_produced_rb}")
    print(f"Total Fluid (Rb): {total_fluid_rb}")
    print(f"Total Fluid (kg): {total_fluid_kg}")
    print(f"Storage Capacity: {storage_capacity} metric tons")

if __name__ == "__main__":
    main()