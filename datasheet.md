📄 Dataset Datasheet: Rain Tomorrow Prediction
1. Motivation
This dataset is used to predict whether it will rain the next day based on weather observations collected today. The goal is to support decision-making in agriculture, transportation, and event planning by providing early warnings for rainfall.

2. Composition
Instances: ~145,000 weather observations

Features (21 total):

Categorical: Location, WindGustDir, WindDir9am, WindDir3pm, RainToday

Numerical: MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm, Temp9am, Temp3pm

Target: RainTomorrow (binary: Yes or No)

3. Collection Process
Source: Australian Government Bureau of Meteorology

Method: Weather stations across Australia record hourly/daily readings which are then aggregated.

Time span: Data spans multiple years across various locations.

4. Preprocessing
Missing Values: Imputed using mean for continuous variables and mode for categorical ones

Encoding: Label encoding and one-hot encoding applied to categorical variables

Scaling: Not required for tree-based models like LightGBM

5. Distribution
The target variable is slightly imbalanced (approximately 78% No Rain vs. 22% Rain).

Weather conditions vary significantly by location and season.

6. Uses
Binary classification: Will it rain tomorrow?

Can be used in:

Weather prediction research

Real-time alert systems

Machine learning tutorials

7. Ethical Considerations
Privacy: No personal or sensitive data included.

Bias: Bias may exist due to geographic and seasonal variations; locations with extreme climates may dominate the signal.

8. Licensing
Dataset is publicly available under the terms provided by the Australian Bureau of Meteorology.

