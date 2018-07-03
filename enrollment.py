import pandas as pd 

if __name__ == "__main__":
    data = pd.read_csv('data/CRDC2013_14.csv',encoding = 'Latin-1')
        
    #calculating percentage race enrollment 
    data['total_enrollment'] = data['TOT_ENR_M'] + data['TOT_ENR_F']
    all_enrollment = data['total_enrollment'].sum()

    tot_hisp = (data['SCH_ENR_HI_M']+data['SCH_ENR_HI_F']).sum()
    percent_hisp = tot_hisp/all_enrollment * 100
       
    print(percent_hisp)   

    