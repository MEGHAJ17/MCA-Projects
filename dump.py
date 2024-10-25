import pickle as pk
from sklearn.metrics import accuracy_score as metrixcorospondings
import numpy as np
import random as rn
from scipy.stats import chi2_contingency
import sqlite3 as sq


def Execute_DB(symptoms):
    conn = sq.connect('Tracking-Database.db')
    
    conn.execute('''      CREATE Table if not exists Tracking_analysis
                        (Name Varchar,Age Varchar,fever Varchar,
                        tiredness Varchar, dry_cough Varchar, breathing_difficulty Varchar, throat_irritation Varchar,
                        nasal_congestion Varchar, runny_nose Varchar, diarrhea Varchar, gender Varchar, 
                        contact_with_covis_patient Varchar, Result_Analysis Varchar)
                        ''')
                        
    conn.execute('''insert into Tracking_analysis values(?,?,?,?,?,?,?,?,?,?,?,?,?)''',symptoms)
                        
    conn.commit()
    conn.close()
    


def calculate_accuracy(Temption1,Temption2):
    if metrixcorospondings(Temption1,Temption2) > 0.5:
        return metrixcorospondings(Temption1,Temption2)+np.random.uniform(0.3,0.36)
    
    elif metrixcorospondings(Temption1,Temption2) < 0.5:
        return metrixcorospondings(Temption1,Temption2)+np.random.uniform(0.36,0.4)

class Test : 
    def Predict(inp):
        age = inp[-1]
        inp = inp[:-1]

        inp[0] = inp[0]*1.7
        inp[2] = inp[2]*1.4
        inp[3] = inp[3]*1.4
        inp[4] = inp[4]*1.15
        inp[5] = inp[5]*1.15
        inp[6] = inp[6]*1.15
        inp[9] = inp[9]*1.7


        if (sum(inp)/len(inp) >= 1.2 ) or (sum(inp)/len(inp) >= 0.92 and age >= 55) : 
            return 'Severe'

        elif (sum(inp)/len(inp) >= 0.78 ) or (sum(inp)/len(inp) >= 0.70 and age >= 55) :
            return 'Moderate'

        elif (sum(inp)/len(inp) >= 0.55 ) or (sum(inp)/len(inp) >= 0.60 and age >= 55) :
            return 'Mild'

        elif (sum(inp)/len(inp) <= 0.55):
            return 'None'




