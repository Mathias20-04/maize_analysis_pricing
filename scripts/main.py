#!/usr/bin/env python3
"""
Main Script - Runs Complete Analysis Pipeline
"""

import importlib.util
import pathlib
import os

# Helper to load scripts that start with digits (e.g. '01_data_validation.py')
# without renaming files. Returns the loaded module object.
def _load_script(name):
    base = pathlib.Path(__file__).parent
    path = base / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Load modules and bind the callable symbols used by the pipeline
_validate_mod = _load_script("01_data_validation")
_validate = _validate_mod.validate_data
_analysis_mod = _load_script("02_data_analysis")
_analyze = _analysis_mod.analyze_data
_viz_mod = _load_script("03_visualization")
_generate_visuals = _viz_mod.generate_visuals

def main():
    print("=== MAIZE PRICING ANALYSIS PIPELINE ===")
    
    # Ensure output directories exist
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('results/tables', exist_ok=True)
    os.makedirs('results/figures', exist_ok=True)

    print("\nSTEP 1: Data Validation")
    df = _validate()

    print("\nSTEP 2: Statistical Analysis")
    _analyze()

    print("\nSTEP 3: Visualization")
    _generate_visuals()

    print("\n=== ANALYSIS COMPLETE ===")
    print("Find outputs in the results/ folder")

if __name__ == "__main__":
    main()
