# Pakistan Population Visualization

This repository contains a **Streamlit**-based visualization tool that maps various demographic, educational, and population metrics for Pakistan. The interactive tool plots markers on a map of Pakistan, where each marker represents a city. The tool allows users to analyze population data and schooling metrics by adjusting primary and secondary parameters.

**Link of this tool** [Pakistan_pop_visualization_tool](https://pakistan-pop-visualization.streamlit.app/)

## Table of Contents
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Parameters](#parameters)
- [Screenshots](#screenshot)
- [Contributing](#contributing)


---

## Features

- **Interactive Map**: Visualize demographic and education metrics across Pakistan.
- **Customizable Parameters**: Choose primary and secondary parameters to display, affecting marker size and color respectively.
- **Province Filtering**: Focus on specific provinces or display data for all of Pakistan.
- **Detailed Metrics**: Primary and secondary parameters include population, school count, household density, and growth rate among others.

## Dataset

The dataset used for this visualization includes the following columns:
- **Demographic**: `total_male_total`, `total_female_total`, `population_2023`, `households`, `density_2023`, etc.
- **Education**: Counts of schools by gender and level, e.g., `primary_boys_schools`, `high_girls_schools`.
- **Geographic**: Coordinates (`lat`, `lng`), area, and density.
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/arafayr/Pakistan-population-Analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Pakistan-Population-Visualization
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run pak_pop_streamlit.py
   ```
2. Open the application in your browser 

## Parameters

- **Primary Parameter**: Sets the marker size, representing metrics like population or number of schools.
- **Secondary Parameter**: Sets the marker color, allowing comparison of a secondary metric such as school density or household size.
- **Province Filter**: Select from provinces (Punjab, Sindh, KPK, Balochistan.) or view data for the entire country.

### Available Metrics
Here are some metrics available for selection:
- Population (`population_2023`, `population_2017`, `growth_rate`)
- Gender distribution (`total_male_total`, `total_female_total`)
- Educational facilities (e.g., `primary_boys_schools`, `high_girls_schools`, `total_schools`)
- Geographic and household data (`area(km²)`, `density_2023`, `households`)

## Screenshot

<img width="957" alt="image" src="https://github.com/user-attachments/assets/9b7a0d36-6c01-499e-b55a-40a857e80b2f">

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
