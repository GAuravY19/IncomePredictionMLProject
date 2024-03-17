import numpy as np
from xgboost import XGBClassifier

from load_pickle import Load_picke_files


def make_prediction(age:int, capital_gain:int, capital_loss:int,
                    education:str, workclass:str, occupation:str, hour_per_week:int):

    # LOADING SCALERS FOR DIFFERENT COLUMNS
    age_scale = Load_picke_files('D:/IncomeML Model/deployment/server/artifacts/age_scale.pkl')
    capital_gain_scale = Load_picke_files('D:/IncomeML Model/deployment/server/artifacts/capital_gain.pkl')
    capital_loss_scale = Load_picke_files('D:/IncomeML Model/deployment/server/artifacts/capital_loss.pkl')
    education_scale = Load_picke_files('D:/IncomeML Model/deployment/server/artifacts/education.pkl')
    hour_per_week_scale = Load_picke_files('D:/IncomeML Model/deployment/server/artifacts/hour_per_week.pkl')
    lb_encode_scale = Load_picke_files('D:/IncomeML Model/deployment/server/artifacts/lb_encode_target.pkl')
    model_pickle = Load_picke_files('D:/IncomeML Model/deployment/server/artifacts/model_pickle')

    WORKCLASS = ['Local-gov', 'Never-worked', 'Private', 'Self-emp-inc', 'Self-emp-not-inc', 'State-gov', 'Without-pay']
    OCCUPATION = ['Armed-Forces', 'Craft-repair', 'Exec-managerial', 'Farming-fishing', 'Handlers-cleaners',
                  'Machine-op-inspct', 'Other-service', 'Priv-house-serv', 'Prof-specialty', 'Protective-serv',
                  'Sales', 'Tech-support', 'Transport-moving']

    try:
        workclass_index = WORKCLASS.index(workclass)
        x[workclass_index+2] = 1

    except:
        workclass_index = 0


    try:
        occupation_index = OCCUPATION.index(occupation)
        x[occupation_index + 8] = 1

    except:
        occupation_index = 0


    x = np.zeros(25)

    x[0] = age_scale.transform([[age]])
    x[1] = education_scale.transform([[education]])
    x[22] = capital_gain_scale.transform([[capital_gain]])
    x[23] = capital_loss_scale.transform([[capital_loss]])
    x[24] = hour_per_week_scale.transform([[hour_per_week]])


    return model_pickle.predict([x])






