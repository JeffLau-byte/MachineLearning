import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv('C:/Users/jeffl/Downloads/House_Price_Dataset.csv')

#features and target
x = df.drop(columns = ['price', 'region'])
y = df['price']

features = ["location", "type", "size_sqft", "rooms", "bathrooms"]
target = 'price'

#drop missing value for column target (price)
df = df.dropna(subset = [target])

#preprocessing
num_features = ['size_sqft', 'rooms',]
cat_features = ['size_sqft', 'rooms', 'bathrooms']
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), num_features),
    ('cat', OneHotEncoder(handle_unknown = 'ignore'), cat_features)
])

#split data
X = df[features]
Y = df[target]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 123)

#pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators = 100, random_state = 123))
])

pipeline.fit(X_train, Y_train)