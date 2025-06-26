from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

df = pd.read_csv("Dataset .csv").dropna(subset=['Country Code', 'City', 'Cuisines'])

le_city = LabelEncoder()
le_cuisine = LabelEncoder()

df['City_enc'] = le_city.fit_transform(df['City'])
df['Cuisine_enc'] = le_cuisine.fit_transform(df['Cuisines'])

X = df[['City_enc', 'Cuisine_enc']]
y = df['Country Code']
model = RandomForestClassifier()
model.fit(X, y)
 
country_city_map = df.groupby('Country Code')['City'].unique().apply(list).to_dict()
city_cuisine_map = df.groupby('City')['Cuisines'].unique().apply(
    lambda x: list(set(', '.join(x).split(', ')))).to_dict()

@app.route('/')
def index():
    countries = sorted(df['Country Code'].unique())
    return render_template("index.html", countries=countries)

@app.route('/get_cities', methods=['POST'])
def get_cities():
    country = int(request.form['country'])
    cities = sorted(country_city_map.get(country, []))
    return {'cities': cities}

@app.route('/get_cuisines', methods=['POST'])
def get_cuisines():
    city = request.form['city']
    cuisines = sorted(city_cuisine_map.get(city, []))
    return {'cuisines': cuisines}

@app.route('/results', methods=['POST'])
def results():
    city = request.form['city']
    cuisine = request.form['cuisine']
 
    if city not in le_city.classes_ or cuisine not in le_cuisine.classes_:
        return render_template("results.html",
                               restaurants=[],
                               cuisine=cuisine)
 
    city_enc = le_city.transform([city])[0]
    cuisine_enc = le_cuisine.transform([cuisine])[0]
    predicted_country = model.predict([[city_enc, cuisine_enc]])[0]
 
    results = df[
        (df['Country Code'] == predicted_country) &
        (df['City'] == city) &
        (df['Cuisines'].str.contains(cuisine, case=False))
    ][['Restaurant Name', 'Locality', 'Cuisines', 'Average Cost for two', 'Aggregate rating']]

    return render_template("results.html",
                           restaurants=results.to_dict(orient='records'),
                           cuisine=cuisine)


if __name__ == '__main__':
    app.run(debug=True)
