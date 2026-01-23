# Employee Performance Prediction using Machine Learning

## 📌 Project Overview
This project predicts employee performance based on key workplace and personal factors using machine learning techniques.
The aim is to assist organizations in making data-driven HR decisions.

The **Decision Tree model achieved the highest accuracy of 93.55%**, and hence was selected as the final model.

---

## 🖥️ Application Interface

Below is a screenshot of the deployed Streamlit web application:

![Employee Performance Prediction App](Screenshot%202026-01-23%20152854.png)

The application allows users to input employee details such as experience, salary, overtime, promotions, and satisfaction score, and instantly predicts the employee performance score.

---

## 📊 Dataset
**File:** `Extended_Employee_Performance_and_Productivity_Data.csv`

### Features Used
- Years_At_Company  
- Monthly_Salary  
- Overtime  
- Promotions  
- Employee_Satisfaction_Score  

### Target Variable
- Performance_Rating

---

## 🧠 Machine Learning Models Implemented
- Logistic Regression  
- Decision Tree ✅ *(Best Model)*  
- Random Forest  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)

---

## 🏆 Model Performance
| Model | Accuracy |
|------|----------|
| Decision Tree | **93.55%** |
| Random Forest | ~90% |

---

## ⚙️ Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  

---

## 🔄 Project Workflow
1. Data loading and preprocessing  
2. Encoding categorical variables  
3. Train-test split  
4. Feature scaling using StandardScaler  
5. Model training and evaluation  
6. Model comparison using multiple metrics  
7. Saving model and scaler using joblib  
8. Deployment using Streamlit  

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run Streamlit App
```bash
streamlit run app.py
```

---

## 💾 Saved Files
- `decision_tree_model.pkl` — trained Decision Tree model  
- `scaler.pkl` — feature scaler  

---

## 📈 Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  
- Confusion Matrix  

---

## 🎯 Conclusion
The Decision Tree classifier provided high accuracy and interpretability, making it suitable for real-world employee performance prediction tasks.

---

## 👨‍💻 Author
**Nayan Suhane**

---

## 📌 Future Enhancements
- Hyperparameter tuning  
- Cross-validation  
- Feature importance visualization  
- Cloud deployment using Streamlit Cloud  
