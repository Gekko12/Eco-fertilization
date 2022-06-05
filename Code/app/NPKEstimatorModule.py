import warnings
import numpy as np 
import pandas as pd 
from sklearn import metrics
import category_encoders as ce
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

warnings.filterwarnings('ignore')


class NPKEstimator:
    def __init__(self, data = 'Nutrient_recommendation.csv', ):
        self.df = pd.read_csv(data, header=None)
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    
    def renameCol(self):
        self.df.columns = ['Crop', 'Temperature', 'Humidity', 'Rainfall', 'Label_N', 'Label_P', 'Label_K']
        self.df.drop(self.df.index[:1], inplace=True)
    
    
    def cropMapper(self):
        # create mapping of crop(string) to int type
        mapping = dict()

        with open("mapped_crops.csv", "w") as fh:
            fh.write("Crops,Key\n")
            for i, crop in enumerate(np.unique(self.df[['Crop']]), 1):
                mapping[crop] =  i
                fh.write("%s,%d\n" % (crop, i))
            mapping['NA'] = np.nan
            fh.write("NA,nan")
        # print(mapping)
        
        ordinal_cols_mapping = [{"col": "Crop", "mapping": mapping}, ]
        encoder = ce.OrdinalEncoder(cols = 'Crop', mapping = ordinal_cols_mapping, return_df = True)
        return mapping, encoder
    
    
    def estimator(self, crop, temp, humidity, rainfall, y_label):
        X = self.df.drop(['Label_N', 'Label_P', 'Label_K'], axis=1)
        y = self.df[y_label]
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)
        
        mapping, encoder = self.cropMapper()
        self.X_train = encoder.fit_transform(self.X_train)
        self.X_test = encoder.transform(self.X_test)
        
        regressor = RandomForestRegressor(n_estimators = 50, random_state = 0)
        regressor.fit(self.X_train, self.y_train)
        
        # y_pred = regressor.predict(self.X_test)
        query = [mapping[crop.strip().lower()], temp, humidity, rainfall]
        y_pred = regressor.predict([query])
        return y_pred[0]
    
    
    def accuracyCalculator(self):
        model = RandomForestRegressor(n_jobs=-1)
        estimators = np.arange(10, 200, 10)
        scores = []
        for n in estimators:
            model.set_params(n_estimators=n)
            model.fit(self.X_train, self.y_train)
            scores.append(model.score(self.X_test, self.y_test))
        
        scores_arr = [round(sc, 3) for sc in scores]
        unique, counts = np.unique(scores_arr, return_counts = True)

        max_count = max(counts)
        accuracy = -1
        for uni, count in zip(unique, counts):
            # print(uni, count)
            if count == max_count:
                accuracy = uni

        # print("Model accuracy: %.2f" % (accuracy))
        return accuracy