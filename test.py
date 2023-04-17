import pandas as pd

data = pd.read_csv('childrecode.csv')

weight_age_sd = 'hw8'
height_age_sd = 'hw5'
weight_height_sd = 'hw11'

#new WHO values
weight_age_sd_new = 'hw71'
height_age_sd_new = 'hw70'
weight_height_sd_new = 'hw72'

# create stunting column
data['stunting'] = data[height_age_sd_new] < -200
#data['severe_stunting'] = data[height_age_sd_new] < -300

# create wasting column
data['wasting'] = data[weight_height_sd_new] < -200
#data['severe_wasting'] = data[weight_height_sd_new] < -300

# create underweight column
data['underweight'] = data[weight_age_sd_new] < -200
#data['severe_underweight'] = data[weight_age_sd_new] < -300

data = data[data['hw2'] <= 9997] # Removing missing
data = data[data['hw3'] <= 9997] # Removing missing

#Divide by 10 to remove implied decimal place
data['hw3'] = data['hw3'] / 10
data['hw2'] = data['hw2'] / 10

df_new = pd.DataFrame({
    'case_id': data['caseid'],
    'weight': data['hw2'],
    'age': data['b8'],
    'height': data['hw3'],
    'stunting': data['stunting'],
    'wasting': data['wasting'] ,
    'underweight': data['underweight']
})


print(df_new.head())
