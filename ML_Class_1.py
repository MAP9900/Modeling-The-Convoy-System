#Imports
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_curve, auc, matthews_corrcoef, balanced_accuracy_score, confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.base import BaseEstimator
import xgboost as xgb
from xgboost import XGBRegressor

#Machine Learning Class Number 1:

class Model_Tester:

    def __init__(self, model = None, scaler = None, parameter_grid = None, cv_folds = 5):
        """
        Class Initializer

        Parameter model: Model used for machine learning (defaults to random classifier)
        Parameter scaler: Scaler used for K-Fold cross-validation
        Parameter parameter_grid: Dictionary of hyperparamters for use in Grid Search Cross-Validation
        Parameter cv_folds: The number of folds used in cross-validation (defaults to 5)
        """
        if model is not None and not hasattr(model, "fit"):
            raise ValueError(f"Error: model must be a scikit-learn classifier, but got {type(model)}")
        self.model = model
        print("DEBUG: Model initialized:", self.model)  # Debugging step

        self.scaler = scaler
        self.parameter_grid = parameter_grid
        self.cv_folds = cv_folds
        self.best_model = None
        self.feature_importance = None
        self.k_fold_results = {"train_scores": [], "test_scores": []}

    def train_test_split(self, X, y, train_size = 0.8, random_state = 1945):
        """
        Perfomr Train Test Split
        """
        self.X_train, self. X_test, self.y_train, self.y_test = train_test_split(
            X, y, train_size=train_size, random_state=random_state, stratify=y)
        
    def k_folds(self, K = None, random_state= 1945):
        """
        Perform K-Fold Cross-Validation
        """
        K = K if K else self.cv_folds

        X_train_array = np.array(self.X_train)
        y_train_array = np.array(self.y_train)
        kf = KFold(n_splits=K, random_state=random_state, shuffle=True)
        train_scores, test_scores = [], []
        

        for idxTrain, idxTest in kf.split(X_train_array):
            X_train_fold, X_test_fold = X_train_array[idxTrain], X_train_array[idxTest]
            y_train_fold, y_test_fold = y_train_array[idxTrain], y_train_array[idxTest]

            if self.scaler is not None: #Scale
                X_train_fold = self.scaler.fit_transform(X_train_fold)
                X_test_fold = self.scaler.transform(X_test_fold)

        self.model.fit(X_train_fold, y_train_fold)
        train_scores.append(self.model.score(X_train_fold, y_train_fold))
        test_scores.append(self.model.score(X_test_fold, y_test_fold))

        self.k_fold_results = {'Train Scores': train_scores, 'Test Scores': test_scores}
        print(f"Average Train Score: {np.mean(train_scores):.4f} ± {np.std(train_scores):.4f}")
        print(f"Average Test Score: {np.mean(test_scores):.4f} ± {np.std(test_scores):.4f}")

        return train_scores, test_scores
    
    def optimize(self):
        """
        Optimization of model/classifier through Grid Search Cross-Validation
        """

        if self.model is None:
            raise ValueError("No model provided for optimization.")

        if self.parameter_grid:
            grid_search = GridSearchCV(self.model, self.parameter_grid, cv=self.cv_folds, scoring='accuracy', n_jobs=-1)
            #n_jobs = -1 uses all available CPUs (Parallel Execution). Switch to -2 to avoid freezing (ex: running server side)
            grid_search.fit(self.X_train, self.y_train)
            self.best_model = grid_search.best_estimator_
            print(f"\nBest Hyperparameters Found:\n{grid_search.best_params_}")
            print(f"Best Cross-Validation Accuracy: {grid_search.best_score_:.4f}")
        else:
            self.best_model = self.model
            if not hasattr(self.best_model, "estimators_"):  # Ensure RandomForestClassifier is properly initialized
                self.best_model.fit(self.X_train, self.y_train)

    def evaluate(self):
        """
        Evaluates the model/classifier using the test data. 
        
        Returns a classification report. Also returns.... (to add)
        """

        if not hasattr(self.best_model, "estimators_") and isinstance(self.best_model, RandomForestClassifier):
            raise RuntimeError("RandomForestClassifier is not fitted before evaluation.")

        model_name = type(self.best_model).__name__
        y_predict = self.best_model.predict(self.X_test)
        y_predict_probability = self.best_model.predict_proba(self.X_test)[:, 1] #Probabilities for ROC & Log Loss

        #Print Model Name
        print(f"\n{model_name} Evaluation:")

        #Classification Report
        print('\nClassification Report:')
        print(classification_report(self.y_test, y_predict))

        #ROC Curve and AUC Score (Receiver Operating Characteristic - Area Under the Curve)
            #Measures ability to distinguish high vs. low risk
            #The ROC Curve plots True Positive Rate (tpr) vs. False Positive Rate (fpr) at various threshold values
        fpr, tpr, _ = roc_curve(self.y_test, y_predict_probability)
        ROC_AUC = auc(fpr, tpr)
        print(f"\nROC AUC Score: {ROC_AUC:.4f}") #If AUC is >0.8, the model is performing well; closer to 0.5 means random guessing.
        self.plot_roc_curve(fpr, tpr, ROC_AUC)

        #Matthews Correlation Coefficient
            #Used due to imablance within the data (more low risk than high risk)
            #A single score that accounts for true/false positives & negatives
        mcc = matthews_corrcoef(self.y_test, y_predict)
        print(f"Matthews Correlation Coefficient (MCC): {mcc:.4f}") #Closer to 1 means better classification

        #Balanced Accuracy Score
            #Used due to imablance within the data (more low risk than high risk)
            #Adjusted accuracy for class imbalance
        balanced_acc = balanced_accuracy_score(self.y_test, y_predict)
        print(f"Balanced Accuracy: {balanced_acc:.4f}")

        #Confusion Matrix
        cm = confusion_matrix(self.y_test, y_predict)
        self.plot_confusion_matrix(cm)

        #Feature Importance
        if hasattr(self.best_model, "feature_importances_"):
            self.plot_feature_importance()

    def plot_roc_curve(self, fpr, tpr, ROC_AUC):
        """
        ROC Curve Plot
        """
        plt.figure(figsize=(6,4), facecolor='lightgrey')
        plt.plot(fpr, tpr, color='#06768d', label=f'ROC Curve (AUC = {ROC_AUC:.2f})')
        plt.plot([0, 1], [0, 1], color='grey', linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve')
        plt.legend(loc='lower right')
        plt.show()

    def plot_confusion_matrix(self, cm):
        """
        Plot Confusion Matrix
        """
        plt.figure(figsize=(6,4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Low Risk', 'High Risk'], \
                    yticklabels=['Low Risk', 'High Risk'])
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.title('Confusion Matrix')
        plt.show()

    def plot_feature_importance(self):
        """
        Feature Importance Plot
        """
        feature_importance_df = pd.DataFrame({
        'Feature': self.feature_names,  
        'Importance': self.best_model.feature_importances_
    }).sort_values(by='Importance', ascending=False)
        plt.figure(figsize=(8,4))
        sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette="coolwarm")  
        plt.title('Feature Importance')
        plt.show()





