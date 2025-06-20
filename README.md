# 💳 Fraud Detection Website using Streamlit

This is a Streamlit-powered web application that uses machine learning to predict the likelihood of a financial transaction being fraudulent.

---

## 📌 Features

- Predicts fraud based on transaction details.
- User-friendly UI for input via dropdowns and number fields.
- Uses a trained logistic regression model.
- Built with Streamlit and scikit-learn.

---

## 📊 Dataset

- **Source**: [Kaggle - Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download)
- **Size**: ~400 MB
- **Records**: 6.3 million

### 💡 Description

The dataset contains mobile money transaction records and flags whether a transaction is fraudulent. It includes:

- **CASH-IN**: Adding funds to an account.
- **CASH-OUT**: Withdrawing money.
- **DEBIT**: Sending money to a bank account.
- **PAYMENT**: Paying merchants for goods/services.
- **TRANSFER**: Sending money to another user.

---

## 🧪 Data Preprocessing and Modeling

1. **Dropped Columns**:
   - `nameOrig`, `nameDest`, and `isFlaggedFraud` were removed to avoid data leakage or non-contributive features.

2. **Feature Engineering**:
   - Created `balanceDiffOrig` and `balanceDiffDest` to represent differences in sender/receiver balances.

3. **Selected Features**:
   - Categorical: `type`
   - Numerical: `amount`, `oldbalanceOrg`, `newbalanceOrig`, `oldbalanceDest`, `newbalanceDest`

4. **Data Split**:
   - Used `train_test_split` with stratification to preserve fraud/non-fraud ratio.

5. **Preprocessing Pipeline**:
   - `StandardScaler` for numerical features.
   - `OneHotEncoder` for `type` (transaction type).

6. **Model**:
   - Logistic Regression with `class_weight='balanced'` to handle class imbalance.
   - Trained for `max_iter=1000`.

7. **Model Export**:
   - The trained model is saved as `fraud_detection_model.pkl` using `joblib`.

---

## 📈 Model Performance

### 🎯 Accuracy
- **94.62%**
