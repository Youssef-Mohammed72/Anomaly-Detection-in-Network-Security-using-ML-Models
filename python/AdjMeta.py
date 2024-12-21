import os
import pandas as pd
import glob
from sklearn.model_selection import train_test_split

def process_csv_files(input_dir):
    csv_files = glob.glob(os.path.join(input_dir, '*.csv'))
    
    all_datasets = []
    
    for filename in csv_files:
        print(f"Processing {filename}")
        
        df = pd.read_csv(filename)
        
        # Remove leading spaces from column names
        df.columns = [col.lstrip() for col in df.columns]
        
        # Move 'Label' column to the end if it exists
        cols = list(df.columns)
        print(cols)
        cols.append(cols.pop(cols.index('Label')))
        df = df[cols]
        
        all_datasets.append(df)
    
    return all_datasets

def concatenate_data(all_datasets, output_path):
    combined_df = pd.concat(all_datasets, ignore_index=True)
    combined_df.to_csv(output_path, index=False)
    print(f"Concatenated data saved to {os.path.dirname(output_path)}")

def split_train_test(combined_df):
    X = combined_df.drop(['Label'], axis=1)
    y = combined_df['Label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    train_df = pd.concat([X_train, y_train], axis=1)
    test_df = pd.concat([X_test, y_test], axis=1)
    
    return train_df, test_df

def save_dataframes(train_df, test_df, train_output_path, test_output_path):
    # Create directories for train and test data
    train_folder = os.path.dirname(train_output_path)
    test_folder = os.path.dirname(test_output_path)
    
    try:
        os.makedirs(train_folder, exist_ok=True)
        os.makedirs(test_folder, exist_ok=True)
    except OSError as e:
        print(f"Error creating directories: {e}")
    
    # Save train.csv to train folder
    train_df.to_csv(train_output_path, index=False)
    print(f"Train data saved to {train_folder}/train.csv")
    
    # Save test.csv to test folder
    test_df.to_csv(test_output_path, index=False)
    print(f"Test data saved to {test_folder}/test.csv")