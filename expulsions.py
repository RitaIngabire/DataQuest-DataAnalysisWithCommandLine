import pandas as pd 

if __name__ == "__main__":                                  
    data = pd.read_csv('data/CRDC2013_14.csv',encoding = 'Latin-1')
   
    data['total_expulsion'] = data['TOT_DISCWODIS_EXPWOE_M'] + data['TOT_DISCWODIS_EXPWOE_F']
    all_expulsion = data['total_expulsion'].sum()
    print(all_expulsion)  
     