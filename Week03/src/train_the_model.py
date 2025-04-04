import  numpy as np
import  pandas as pd
import  matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier, LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
from sklearn.preprocessing import StandardScaler
from pickle import dump

def model_training(data, X_train, y_train):
    lr = SGDClassifier(loss='log_loss', learning_rate='constant', eta0=0.002, max_iter=1, warm_start=True)

    losses = []
    accuracies = []

    for _ in range(250):  # 250 iterations
        lr.partial_fit(X_train, y_train, classes=np.unique(y_train))
        y_pred_prob = lr.predict_proba(X_train)[:, 1]
        loss = log_loss(y_train, y_pred_prob)
        losses.append(loss)
        
        y_pred = lr.predict(X_train)
        accuracy = accuracy_score(y_train, y_pred)
        accuracies.append(accuracy)

    return lr, losses, accuracies



def model_plots(model, losses, accuracies):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot Loss curve
    ax1.plot(losses, color='red')
    ax1.set_title('Loss Curve for Logistic Regression')
    ax1.set_xlabel('Iterations')
    ax1.set_ylabel('Log Loss')
    ax1.grid(True)

    # Plot Accuracy curve
    ax2.plot(accuracies, color='blue')
    ax2.set_title('Accuracy Curve for Logistic Regression')
    ax2.set_xlabel('Iterations')
    ax2.set_ylabel('Accuracy')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

def train():
    data = pd.read_csv('./data/Admission_Predict_df_cleaned.csv')
    scaler = StandardScaler()
    THRESHOLD = 0.70

    X = data.drop('Chance of Admit ', axis=1)
    y = data['Chance of Admit ']
    y = (y > THRESHOLD).astype(int)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)

    model, losses, accuracies = model_training(data, X_train_scaled, y_train)
    if input("plot the Loss curve and Accuracy curve? (yes/no): ") == 'yes':
        model_plots(model, losses, accuracies)
    dump(model, open('./model/Admission_Predict_SGDC_model.pkl', 'wb'))
    dump(scaler, open('./model/scaler.pkl', 'wb'))

