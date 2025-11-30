import pandas as pd 
import numpy as np 

seed = 42
np.random.seed(seed)

# The formula in Supplementary Information 
def calculate_class_weights(df, label_column, gamma):
    class_counts = df[label_column].value_counts().to_dict()
    total_samples = len(df)
    class_weights = {cls: total_samples / (gamma * count + (1-gamma)*total_samples) for cls, count in class_counts.items()}
    return class_weights 

if __name__ == "__main__":

    # image annotation types (example paths)
    csv_paths =[f'./fold_easy/types.csv', 
        f'./fold_hard.csv']

    # output of combined set annotations (image paths, and label paths)
    output_csv = f'fold_easy_hard_weighted.csv'
    
    # Concatenate all DataFrames (from different class types) into a single DataFrame
    dataframes = []
    for path in csv_paths:
        df = pd.read_csv(path)
        dataframes.append(df)
    df = pd.concat(dataframes, ignore_index=True)
    df['labels'] = df['images'].str.replace('/images/', '/labels/').str.replace('.png', '.npy')

    # weights 
    class_weights = calculate_class_weights(df, 'class', gamma=0.85)
    df['weight'] = df['class'].map(class_weights)
    df['weight'] = df['weight'] / df['weight'].sum()


    sampled_indices = np.random.choice(df.index, size=len(df), replace=True, p=df['weight'].values)
    reordered_df = df.loc[sampled_indices].reset_index(drop=True)

    reordered_df.to_csv(output_csv, index=False)

    # can be directly used for customized Pytorch-like dataset, with "images" and "labels" columns 
