# Excel to Python Equations

This project converts Excel-based calculations into Python functions for integration into a web application. The calculations are sourced from three Excel tabs: Saline, Depleted, and Economic Analysis, each containing different levels of complexity.

## Project Structure

- **Saline Module (`saline_calculations.py`)**: Basic calculations from the Saline tab.
- **Depleted Module (`depleted_calculations.py`)**: Similar basic calculations from the Depleted tab.
- **Economic Analysis Module (`economic_analysis.py`)**: Complex cash flow calculations, including logic for financial metrics.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/LewisJassy/excel-to-python-equations.git
    ```

2. **Navigate into the project directory:**
    ```bash
    cd excel-to-python-equations
    ```

3. **(Optional) Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

4. **Install any necessary dependencies:**
    Currently, there are no external dependencies. However, if libraries are added, you can install them using:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Each module is designed to run independently. Example usages for each module are provided below.

### Saline Module

This module performs straightforward calculations based on the data in the Saline tab.

### Depleted Module

This module performs calculations based on the Depleted tab.



### Economic Analysis Module

This module handles cash flow calculations and financial metrics based on data from the Economic Analysis tab.



## Configuration

- **CO2 Variables**: The variables CO2 density and CO2 viscosity use placeholder values, as they will be provided later by a different workstream.
- **Azure Compatibility**: Code is written to be modular for easy integration with the Azure backend.

## Project Requirements

The Python code is designed to be compatible with:

- Python 3.8 or higher

## Repository Details

- **GitHub Repository**: [excel-to-python-equations](https://github.com/LewisJassy/excel-to-python-equations)
- **Primary Contact**: [graemecarbonstorage](https://github.com/graemecarbonstorage)

## License

This project is licensed under the MIT License.
