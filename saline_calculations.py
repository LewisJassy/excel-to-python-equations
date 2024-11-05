import pandas as pd
import math

# global variable
ETA = 1.0 # Replace this with the actual value
GAMMA = 1.0 # Replace this with the actual value

def extract_saline_data(file_path):
    """
    Extract saline data from a CSV file.
    
    :param file_path: Path to the CSV file.
    :return: DataFrame containing the saline data.
    """
    saline_data = pd.read_csv(file_path, skiprows=1)
    return saline_data

def calculate_storage_efficiency_no_dip(injection_rate, reservoir_thickness, injection_time, reservoir_depth, pressure_gradient, 
                                        reservoir_angle, permeability, water_salinity, CO2_relative_permeability, water_relative_permeability, temperature, porosity):
    """
    Calculate the storage efficiency of a saline aquifer without a dip angle.
    
    :param injection_rate: Injection rate in million tons per annum.
    :param reservoir_thickness: Thickness of the reservoir in meters.
    :param injection_time: Injection time in years.
    :param reservoir_depth: Depth of the reservoir in meters.
    :param pressure_gradient: Pressure gradient in psi/ft.
    :param reservoir_angle: Angle of the reservoir in degrees.
    :param permeability: Permeability of the reservoir in mD.
    :param water_salinity: Salinity of the water in ppm.
    :param CO2_relative_permeability: Relative permeability of CO2.
    :param water_relative_permeability: Relative permeability of water.
    :param temperature: Temperature in Fahrenheit.
    :param porosity: Porosity of the reservoir in percent.
    :return: Storage efficiency of the saline aquifer.
    """
    
    # Define constants(Assume Area as 1 for unit storage efficiency)
    area = 1  # area can be calculate or assumed as 1 for efficiency purposes

    # Storage efficiency without dip
    storage_efficiency = (permeability * injection_time *  reservoir_thickness * porosity * CO2_relative_permeability) / area
    return storage_efficiency * 100 # Convert to percent

def calculate_storage_efficiency_with_dip(injection_rate, reservoir_thickness, injection_time, reservoir_depth, pressure_gradient, 
                                        reservoir_angle, permeability, water_salinity, CO2_relative_permeability, water_relative_permeability, temperature, porosity):
    """
    Calculate storage efficiency with dip.
    
    :param injection_rate: Injection rate in million tons per annum.
    :param reservoir_thickness: Reservoir thickness in meters.
    :param injection_time: Injection time in years.
    :param porosity: Porosity in percent.
    :param reservoir_depth: Reservoir depth in meters.
    :param pressure_gradient: Pressure gradient in psi/ft.
    :param reservoir_angle: Reservoir angle in degrees.
    :param permeability: Permeability in mD.
    :param water_salinity: Water salinity in parts per million.
    :param CO2_relative_permeability: CO2 relative permeability.
    :param water_relative_permeability: Water relative permeability.
    :param temperature: Temperature in Fahrenheit.
    :return: Storage efficiency with dip in percent.
    """

    # Define constants
    area = 1  # area can be calculate or assumed as 1 for efficiency purposes
    dip_angle_radians = math.radians(reservoir_angle) # Convert angle to radians

    # Storage efficiency with dip
    storage_efficiency = (permeability * injection_time * reservoir_thickness * porosity * CO2_relative_permeability * math.sin(dip_angle_radians)) / area
    return storage_efficiency * 100  # Convert to percent

def calculate_radius_dong_duan(injection_rate, permeability, porosity):
    """
    Calculate the radius of the CO2 plume using the Dong and Duan method.
    
    :param injection_rate: Injection rate in million tons per annum.
    :param permeability: Permeability of the reservoir in mD.
    :param porosity: Porosity of the reservoir in percent.
    :return: Radius of the CO2 plume in meters.
    """
    # Convert injection rate to cubic meters per second
    Q = injection_rate * 1e6 / (365.25 * 24 * 3600)
    radius_dong_duan = ETA * (GAMMA * permeability / porosity) ** 0.25 * math.sqrt(Q)
    return radius_dong_duan


def calculate_area(radius):
    """
    Calculate the area of the aquifer.
    
    :param radius: Radius of the aquifer in meters.
    :return: Area of the aquifer in square meters.
    """
    area = (math.pi * radius **2) / 2.59e6 # Convert to square miles
    return area

def calculate_reservoir_pressure(reservoir_depth, pressure_gradient):
    """
    Calculate the reservoir pressure.
    
    :param reservoir_depth: Depth of the reservoir in meters.
    :param pressure_gradient: Pressure gradient in psi/ft.
    :return: Reservoir pressure in psi.
    """
    reservoir_depth_ft = reservoir_depth * 2.28084
    reservoir_pressure = pressure_gradient * reservoir_depth_ft
    return reservoir_pressure

def calculate_density(CO2_density, water_density):
    """
    Calculate the density of the saline solution.
    
    :param CO2_density: Density of CO2 in kg/m^2.
    :param water_density: Density of water in kg/m^2.
    :return: Density of the saline solution in kg/m^2.
    """
    delta_density = water_density - CO2_density
    return delta_density

def calculate_radius_dong(injection_rate, reservoir_thickness, injection_time, porosity, permeability):
    """
    Calculate the radius of the aquifer using the Dong et al. (2017) method.
    
    :param injection_rate: Injection rate in million tons per annum.
    :param reservoir_thickness: Thickness of the reservoir in meters.
    :param injection_time: Injection time in years.
    :param porosity: Porosity of the reservoir in percent.
    :param reservoir_depth: Depth of the reservoir in meters.
    :param pressure_gradient: Pressure gradient in psi/ft.
    :return: Radius of the aquifer in meters.
    """
    C = 1.0 # Empirical constantfor unit adjustments
    radius_dong = C * math.sqrt(injection_rate * injection_time / (porosity * reservoir_thickness * permeability))
    return radius_dong

def calculate_area_dong(radius):
    """
    Calculate the area of the aquifer using the Dong et al. (2017) method.
    
    :param radius: Radius of the aquifer in meters.
    :return: Area of the aquifer in square meters.
    """
    area_dong = (radius ** 2) * math.pi / 2.59e6 # Convert to square miles
    return area_dong

def calculate_radius_nordbotten(injection_rate, permeability, porosity):
    """
    Calculate the radius of the CO2 plume using the Nordbotten method.
    
    :param injection_rate: Injection rate in million tons per annum.
    :param permeability: Permeability of the reservoir in mD.
    :param porosity: Porosity of the reservoir in percent.
    :return: Radius of the CO2 plume in meters.
    """
    # Convert injection rate to cubic meters per second
    Q = injection_rate * 1e6 / (365.25 * 24 * 3600)
    radius_nordbotten = ETA * (GAMMA * permeability / porosity) ** 0.25 * math.sqrt(Q)
    return radius_nordbotten

def calculate_area_nordbotten(radius):
    """
    Calculate the area of the aquifer using the Nordbotten et al. (2018) method.
    
    :param radius: Radius of the aquifer in meters.
    :return: Area of the aquifer in square meters.
    """
    area_nordbotten = (radius ** 2) * math.pi / 2.59e6 # Convert to square miles
    return area_nordbotten

def main():
    file_path = "Calculations for python - Saline Storage.csv"
    saline_data =  extract_saline_data(file_path)

    injection_rate = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Injection Rate', 'Unnamed: 5'].values[0])
    reservoir_thickness = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Reservoir Thickness', 'Unnamed: 5'].values[0])
    injection_time = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Injection Time', 'Unnamed: 5'].values[0])
    porosity = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Porosity', 'Unnamed: 5'].values[0])
    reservoir_depth = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Reservoir Depth', 'Unnamed: 5'].values[0])
    pressure_gradient = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Pressure Gradient', 'Unnamed: 5'].values[0])
    reservoir_angle = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Reservoir Angle', 'Unnamed: 5'].values[0])
    permeability = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Permeability', 'Unnamed: 5'].values[0])
    water_salinity = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Water Salinity', 'Unnamed: 5'].values[0])
    CO2_relative_permeability = float(saline_data.loc[saline_data['Unnamed: 2'] == 'CO2 Relative Permeability', 'Unnamed: 5'].values[0])
    water_relative_permeability = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Water Relative Permeability', 'Unnamed: 5'].values[0])
    temperature = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Temperature', 'Unnamed: 5'].values[0])
    CO2_density = float(saline_data.loc[saline_data['Unnamed: 2'] == 'CO2 Density', 'Unnamed: 5'].values[0])
    water_density = float(saline_data.loc[saline_data['Unnamed: 2'] == 'Water Density', 'Unnamed: 5'].values[0])


    # Perfom calculations
    storage_efficiency_no_dip = calculate_storage_efficiency_no_dip(injection_rate, reservoir_thickness, injection_time, porosity, reservoir_depth, pressure_gradient, reservoir_angle, permeability, water_salinity, CO2_relative_permeability, water_relative_permeability, temperature)
    storage_efficiency_dip = calculate_storage_efficiency_with_dip(injection_rate, reservoir_thickness, injection_time, porosity, reservoir_depth, pressure_gradient, reservoir_angle, permeability, water_salinity, CO2_relative_permeability, water_relative_permeability, temperature)
    radius = calculate_radius_dong_duan(injection_rate, permeability, porosity)
    area = calculate_area(radius)
    reservoir_pressure = calculate_reservoir_pressure(reservoir_depth, pressure_gradient)
    delta_density = calculate_density(CO2_density, water_density)
    radius_dong = calculate_radius_dong(injection_rate, reservoir_thickness, injection_time, porosity, permeability)
    area_dong = calculate_area_dong(radius_dong)
    radius_nordbotten = calculate_radius_nordbotten(injection_rate, reservoir_thickness, injection_time, porosity, permeability, reservoir_depth)
    area_nordbotten = calculate_area_nordbotten(radius_nordbotten)

    # return storage_efficiency_no_dip, storage_efficiency_dip, radius, area, reservoir_pressure, delta_density

    # print results
    print(f"Storage Efficiency without Dip: {storage_efficiency_no_dip}%")
    print(f"Storage Efficiency with Dip: {storage_efficiency_dip}%")
    print(f"Radius: {radius} meters")
    print(f"Area: {area} square miles")
    print(f"Reservoir Pressure: {reservoir_pressure} psi")
    print(f"Density of Saline Solution: {delta_density} kg/m^2")
    print(f"Radius (Dong and Duan method): {radius_dong} meters")
    print(f"Area (Dong and Duan method): {area_dong} square miles")
    print(f"Radius (Nordbotten method): {radius_nordbotten} meters")
    print(f"Area (Nordbotten method): {area_nordbotten} square miles")

if __name__ == "__main__":
    main()
