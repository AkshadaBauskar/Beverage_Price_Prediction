# Beverage Price Prediction

![Streamlit App](https://img.shields.io/badge/Streamlit-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.9-blue)

## 📖 Project Overview
**Beverage Price Prediction** is a machine learning project aimed at predicting optimal beverage price ranges based on customer demographics, preferences, and behaviors. The project leverages a clean survey dataset and advanced ML models to offer data-driven insights for pricing strategies in the beverage industry.

## 🎯 Objective
To build a predictive model that categorizes beverage prices into defined ranges, optimizing pricing strategies while enhancing customer satisfaction and business growth.

## 🚀 Key Features
- **Interactive Streamlit App**: Allows real-time prediction of beverage prices based on user input.
- **Advanced Machine Learning Models**: Utilizes XGBoost as the best-performing model with 92.54% accuracy.
- **Feature Engineering**: Introduces meaningful new features like Zone Affluence Score and Brand Switching Indicator for better predictions.
- **End-to-End Pipeline**: From data preprocessing to deployment, the project follows a streamlined ML pipeline.

## 🗂️ Dataset Overview
- **Records**: 30,010 rows
- **Features**: 17 (including target variable `price_range`)
- **Categories**:
  - Demographics: `Age`, `Gender`, `Zone`, `Occupation`
  - Behavioral: `Consumption Frequency`, `Brand Awareness`, `Purchase Channel`
  - Preferences: `Flavor Preference`, `Packaging Type`, `Health Concerns`

## 🛠️ Tools and Technologies
- **Programming Languages**: Python
- **Libraries**: pandas, numpy, scikit-learn, XGBoost, joblib
- **Deployment**: Streamlit
- **Version Control**: GitHub
- **Collaboration and Tracking**: DagsHub

## 🔍 Methodology
1. **Data Cleaning**:
   - Imputed missing values and corrected inconsistencies.
   - Removed duplicates and treated outliers using the IQR method.

2. **Feature Engineering**:
   - Created features like `Zone Affluence Score` and `Brand Switching Indicator`.
   - Applied OneHotEncoding and LabelEncoding for categorical features.

3. **Model Training**:
   - Tested various models including Logistic Regression, Random Forest, and XGBoost.
   - Achieved the highest accuracy of 92.54% using XGBoost.

4. **Deployment**:
   - Developed a user-friendly Streamlit application for real-time predictions.

## 🎮 Streamlit App Demo
**Try the live app here**: [Beverage Price Prediction App](https://beveragepriceprediction-fkw9mnjya2zrtk96vrctva.streamlit.app/)

### Features:
- Input customer data (age, gender, zone, etc.) to predict the price range.
- Real-time predictions powered by the XGBoost model.

## 📊 Model Performance
| Model                  | Accuracy |
|------------------------|----------|
| Gaussian Naive Bayes   | 56.66%   |
| Logistic Regression    | 79.28%   |
| Support Vector Machine | 83.58%   |
| Random Forest          | 89.28%   |
| **XGBoost**            | **92.54%** |
| LightGBM               | 90.76%   |

## 📈 Business Impact
- **Optimized Pricing**: Leverages insights to maximize profitability.
- **Market Segmentation**: Enables targeted marketing and promotions.
- **Customer Retention**: Aligns pricing with customer expectations.


## 💻 How to Run Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/AkshadaBauskar/Beverage_Price_Prediction.git
   cd Beverage_Price_Prediction

2. Install dependencies
   ```bash
    pip install -r requirements.txt

3. Run the Streamlit app:
   ```bash
   streamlit run src/app.py

## 📫 Contact
**Akshada Bauskar**  
- 📧 Email: [akshada.bauskar171222@gmail.com](mailto:akshada.bauskar171222@gmail.com)  
- 💼 [LinkedIn Profile](https://www.linkedin.com/in/akshada-bauskar/) *(Presentation available on LinkedIn)*  
- 🌐 [DagsHub Project](https://dagshub.com/AkshadaBauskar/Beverage_Price_Prediction)
