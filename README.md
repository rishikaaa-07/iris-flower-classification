# 🌸 Iris Flower Classification

<h3 align="center">🌿 Predicting Iris Flower Species Using Machine Learning 🌿</h3>

<p align="center">
  A Machine Learning project that classifies Iris flowers into three different species using Python, Scikit-learn, and Streamlit.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>

---

## 🌺 Project Overview

The **Iris Flower Classification** project is a supervised Machine Learning application designed to identify and classify Iris flowers into three species:

- 🌼 Iris-setosa
- 🌷 Iris-versicolor
- 🌸 Iris-virginica

The model predicts the flower species based on four important physical measurements: sepal length, sepal width, petal length, and petal width.

This project demonstrates the complete Machine Learning workflow, from data preprocessing and exploratory data analysis to model training, evaluation, and real-time prediction through an interactive web application.

## 🎯 Project Objectives

- Understand and analyze the Iris flower dataset.
- Perform data cleaning and preprocessing.
- Explore patterns and relationships using data visualization.
- Implement multiple Machine Learning classification algorithms.
- Compare model performance and accuracy.
- Build an interactive flower prediction application using Streamlit.

## 📊 Dataset Information

The project uses the Iris Flower Classification dataset.

| Attribute | Description |
|---|---|
| Dataset size | 150 records originally |
| Total features | 4 |
| Target variable | Species |
| Classification type | Multi-class |
| Missing values | 0 |

### 🌱 Input Features

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal (cm) |
| Sepal Width | Width of the sepal (cm) |
| Petal Length | Length of the petal (cm) |
| Petal Width | Width of the petal (cm) |

### 🌸 Target Classes

1. Iris-setosa
2. Iris-versicolor
3. Iris-virginica

## 🛠️ Technologies & Libraries Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning |
| Jupyter Notebook | Development environment |
| Streamlit | Interactive web application |
| Pickle | Saving trained ML models |

## 🤖 Machine Learning Algorithms

Four classification algorithms are implemented and compared:

**1. Logistic Regression**
- A supervised classification algorithm.
- Predicts the probability of different flower species.

**2. K-Nearest Neighbors (KNN)**
- Classifies flowers based on their nearest data points.
- Uses distance-based classification.

**3. Decision Tree**
- Uses decision rules to classify flower species.
- Provides an easy-to-understand classification structure.

**4. Random Forest**
- Combines multiple decision trees.
- Improves prediction performance through ensemble learning.

## 🔍 Project Workflow

1. Import required Python libraries.
2. Load the Iris dataset.
3. Explore the dataset and statistical information.
4. Perform data cleaning and preprocessing.
5. Conduct Exploratory Data Analysis (EDA).
6. Visualize data using different graphs.
7. Split the dataset into training and testing sets.
8. Apply feature scaling where required.
9. Train four Machine Learning algorithms.
10. Compare model accuracy.
11. Evaluate performance using classification reports and confusion matrices.
12. Predict the species of new Iris flowers.

## 📈 Data Visualization

The project includes several visualizations to understand the dataset:

- Species Distribution Count Plot
- Sepal Length Distribution
- Petal Length Distribution
- Petal Length vs Petal Width Scatter Plot
- Feature Box Plots
- Correlation Heatmap
- Model Accuracy Comparison
- Confusion Matrix

## 🌐 Interactive Web Application

An interactive web application is developed using **Streamlit**.

Users can enter the following flower measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

By clicking the **Predict Flower Species** button, the application uses the trained Machine Learning model to predict the flower species.

### ✨ Application Features

- Simple and user-friendly interface.
- Interactive measurement input fields.
- Real-time flower species prediction.
- Machine Learning model integration.
- Prediction results displayed instantly.

## 📁 Project Structure

```text
irisflowerclassification/
│
├── 01_iris_flower_classification.csv
├── irisflowerclassification.ipynb
├── app.py
├── iris_model.pkl
├── iris_scaler.pkl
├── model_scaled.pkl
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

**Step 1: Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/iris-flower-classification.git
```

**Step 2: Navigate to the project directory**

```bash
cd iris-flower-classification
```

**Step 3: Install the required dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Streamlit application**

```bash
streamlit run app.py
```

**Step 5: Open the application**

Visit:

```text
http://localhost:8501
```

Enjoy predicting Iris flower species! 🌸

## 📊 Model Evaluation

The performance of the four Machine Learning algorithms is compared using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

The best-performing model is selected based on its test accuracy.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and data analysis.
- Data preprocessing and exploratory data analysis.
- Data visualization techniques.
- Supervised Machine Learning.
- Classification algorithms.
- Model evaluation and comparison.
- Building interactive applications using Streamlit.
- Saving and loading trained Machine Learning models.

## 🚀 Future Enhancements

- Deploy the application online using Streamlit Community Cloud.
- Add interactive flower images based on predictions.
- Improve the user interface and design.
- Experiment with additional classification algorithms.
- Add prediction confidence visualization.

## 👩‍💻 Author

**Developed as a Machine Learning Project**

🌸 Iris Flower Classification using Python and Machine Learning.

---

<p align="center">
  ⭐ If you find this project interesting, consider giving it a star!
</p>

<p align="center">
  <b>Made with ❤️ using Python and Machine Learning</b>
</p>
