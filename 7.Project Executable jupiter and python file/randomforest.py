import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
# Load your model (example)
model = pickle.load(open('ranf.pkl', 'rb'))
# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
 

@app.route('/services', methods=['POST'])  
def predict_startup_future():
    
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    prediction = model.predict(final_features)
    
    output = prediction[0]
    if output ==1:
        predictionText = 'Failed'
    elif output == 3:
        predictionText = 'Successfull'
    elif output == 4:
        predictionText = 'Canceled'
    elif output == 2:
        predictionText = 'Live'
    elif output == 5:
        predictionText = 'Suspended'
          
    return render_template('services.html', prediction_text='Kickstart will {}'.format(predictionText))


if __name__ == '__main__':
    app.run(debug=False)
