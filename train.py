import pandas as pd
import numpy as np
import kagglehub
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def train_model():
    # 1. Download and Load Data
    print("Downloading dataset...")
    path = kagglehub.dataset_download("adityakadiwal/water-potability")
    df = pd.read_csv(f"{path}/water_potability.csv")
    
    X = df.drop("Potability", axis=1)
    y = df["Potability"]

    # 2. Define Feature Groups
    # These 3 have missing values and need imputation
    impute_cols = ['ph', 'Sulfate', 'Trihalomethanes']
    # All columns will eventually be used for the Random Forest
    all_cols = X.columns.tolist()

    # 3. Build the Preprocessing Pipeline
    # Step A: Impute missing values
    # Step B: Scale the features (Optional for RF, but good practice in pipelines)
    preprocessor = ColumnTransformer([
        ('imputer', SimpleImputer(strategy='mean'), impute_cols)
    ], remainder='passthrough')

    # 4. Define the Champion Model with your tuned hyperparameters
    # Replace these values with the exact ones from your grid search output
    best_params = {
        'n_estimators': 200,
        'max_depth': None,
        'min_samples_split': 2,
        'max_features': 'sqrt',
        'random_state': 42
    }

    champion_rf = RandomForestClassifier(**best_params)

    # 5. Create the Full Pipeline
    # This bundles preprocessing and the model into one object
    clf_pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', champion_rf)
    ])

    # 6. Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # 7. Train the Model
    print("Training the Tuned Random Forest model...")
    clf_pipeline.fit(X_train, y_train)

    # 8. Evaluate
    y_pred = clf_pipeline.predict(X_test)
    print("\n--- Model Performance ---")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # 9. Save the Model
    model_filename = "model.pkl"
    joblib.dump(clf_pipeline, model_filename)
    print(f"\nModel saved successfully as {model_filename}")

if __name__ == "__main__":
    train_model()