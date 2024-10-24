Titanic Survival Analysis
# Titanic Survival Analysis Project

This project focuses on analyzing the dataset of Titanic passengers, exploring key insights, and predicting survival chances using various data preprocessing, exploratory data analysis (EDA), and machine learning techniques.

This project has also been deployed as an interactive web app using Streamlit. You can check it out [here](https://titanicliagcaviedes.streamlit.app/).

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Data Preprocessing](#data-preprocessing)
- [Machine Learning Model](#machine-learning-model)
- [Streamlit App](#streamlit-app)
- [How to Run Locally](#how-to-run-locally)

## Project Overview
The Titanic Survival Analysis project aims to extract valuable insights from the historical Titanic dataset and predict the survival rate of passengers based on various factors such as gender, class, age, family group, and more.

Through data cleaning, visualizations, and machine learning models, we explore patterns that correlate with survival outcomes and deploy an automated machine learning model for prediction.

## Features
### 1. Data Preprocessing

### 2. Exploratory Data Analysis (EDA)

### 3. Visualizations

### 4. Machine Learning Model

### 5. Streamlit Web Application
- Streamlit app deployment for user-friendly interaction with the dataset and visualizations.
- Predict survival chances based on input variables via the web app interface.
- Dynamic charts and plots integrated for live interaction and exploration.
- Check the web app here: [Titanic Survival Streamlit App](https://titanicliagcaviedes.streamlit.app/).

## Technologies Used
- **Python**: Core programming language for data processing and analysis.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.
- **Matplotlib & Seaborn**: Data visualization libraries.
- **Plotly**: Interactive visualizations.
- **Scikit-learn**: Machine learning library for model building and preprocessing.
- **Streamlit**: Web application framework for interactive data apps.

## Exploratory Data Analysis (EDA)
We explore survival rates across different variables using visualizations and statistical methods. Key insights include:
- **Survival by Age**: Higher survival rates among children.
- **Survival by Gender**: Females had a significantly higher survival rate.
- **Survival by Class**: Passengers in first-class had better chances of survival.
- **Family Groups**: Passengers with family had varying survival chances depending on the size of their family group.

- ### Visualizations 
- Comparison of the survival rates across various variables such as:
    - Age groups
    - Passenger class (Pclass)
    - Gender (Sex)
    - Embarked locations
    - Family groups
- Combination charts and histograms to deeply analyze survival patterns.
- Built-in visualizations using libraries like Matplotlib, Seaborn, and Plotly.
- Dynamic combo charts for comparing survival rates against variables.
- Interactive gender-class and age-group survival comparison graphs.


## Data Preprocessing
Data cleaning and preprocessing included:

### Handling Missing Values:
- Imputed missing ages using KNN Imputer based on nearest neighbors.
- Replaced missing values in Embarked with the most frequent category.
- Dropped columns with too many missing values, such as Cabin.

### Feature Engineering:
- **FamilyGroup**: Combined SibSp (siblings/spouses) and Parch (parents/children) into a single feature to represent family size.
- **AgeGroup**: Created buckets for ages to categorize passengers into distinct age groups.
- **Title**: Extracted passenger titles from the Name column to explore the social status effect.
- **Type of Ticket**: Distinguished between numeric and alphanumeric ticket types to observe patterns.

### Data Transformation:
- Encoded categorical variables using LabelEncoder for machine learning models.
- Scaled numerical features using StandardScaler before applying the KNN imputation method.

## Machine Learning Model
- A machine learning pipeline is implemented to predict survival rates using key features from the dataset.
- Automated model selection and performance evaluation using metrics like accuracy.     
The model pipeline includes:
        - **Data Preprocessing**: Handled missing values, feature scaling, and encoding.
        - **Model Training**: Built an automatic machine learning pipeline to predict survival chances.
        - **Evaluation**: Assessed model accuracy and performance using training and validation datasets.



## Streamlit App

The Titanic Survival Prediction app allows users to interact with the dataset through:
- **Dynamic visualizations**: Visualize survival rates across various dimensions like gender, class, and age.
- **Predictive model**: Input key variables (e.g., age, class, gender, family size) and get survival predictions.

The app is hosted on Streamlit, and you can try it out by visiting: [Titanic Survival Streamlit App](#).



## How to Run Locally
To run this project locally, follow these steps:

### Prerequisites
- Python 3.8+

### Install required dependencies:
```bash
pip install -r requirements.txt
```

### Running the Jupyter Notebook
1. Clone the repository:
        ```bash
        git clone https://github.com/your-repo/titanic-survival-analysis.git
        ```
2. Navigate to the project directory:
        ```bash
        cd titanic-survival-analysis
        ```
3. Open the Jupyter Notebook to explore the code and run the analysis:
        ```bash
        jupyter notebook
        ```

### Running the Streamlit App
Run the Streamlit app locally:
```bash
streamlit run app.py
```
Open the browser at [http://localhost:8501](http://localhost:8501) to interact with the app.


### License

This project is licensed under the MIT License. See the LICENSE file for details.


### Author

- **Name**: Rosalía González Caviedes
- **Email**: rosaliagonzalezc@gmail.com
- [LinkedIn profile](https://www.linkedin.com/in/rosaliagonzalezcaviedes/)

### Contributing
We welcome contributions to this project! Please submit a pull request or open an issue if you have suggestions or improvements.
