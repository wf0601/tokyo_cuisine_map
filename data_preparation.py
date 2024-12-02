import pandas as pd 
import glob 
import os
import yaml

orig_data_folder = 'orig_data'
def load_cuisine_mapping():
    with open('./config/cuisines.yaml', 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
cuisine_mapping = load_cuisine_mapping()
filters = list(cuisine_mapping['common_filters'].keys())    
    
def filter_data(min_rating, num_markers):
# Iterate through all files in the folder
    for file_name in os.listdir(orig_data_folder):
        if file_name.endswith('.csv'):  # Process only CSV files
            file_path = os.path.join(orig_data_folder, file_name)
            print(file_path)
            print(file_name)
            
            # Extract the 'type' from the file name (word before 'tokyo' and 'restaurant')
            type_parts = file_name.split('_')
            file_type = next((word for word in type_parts if word not in ['tokyo', 'restaurant', '']), None)

            # Read the CSV file
            df = pd.read_csv(file_path)

            # Add the 'type' column
            df['type'] = file_type
            
            df_filtered = df.iloc[:num_markers]
            df_filtered = df_filtered.query('rating>={}'.format(min_rating))



            # Avoid duplicate rows
            file_name = '2024_'+file_name
            df_filtered = df_filtered.drop_duplicates()
            new_path = os.path.join('data', file_name)
            df_filtered.to_csv(new_path,index=False,encoding='utf-8-sig')
            
    print('End of data filtering')
    
if __name__ == '__main__':
    filter_data(cuisine_mapping['common_filters']['min_rating'], cuisine_mapping['common_filters']['num_markers'])
            
        