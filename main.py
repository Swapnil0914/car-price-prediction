
from flask import Flask, render_template, request

import pickle



app = Flask(__name__,template_folder='Templates')
model = pickle.load(open('md.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('p1.html')


@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Year = int(request.form['Year'])
        MPG=float(request.form['MPG'])
        EG=float(request.form['EG'])
        Tax=int(request.form['Tax'])
        T=request.form['Transmission']
        F=request.form['FuelT']
        Mileage=int(request.form['Mileage'])
        
        
        T1,T2,T3=0,0,0
        F1,F2,F3,F4=0,0,0,0
        
        
        if(T=='Manual'):
            T1=1
        elif (T=='Semi-Auto'):
            T3=1
        elif (T=='Automatic'):
            T1,T2,T3=0,0,0
        else:
            T2=1
            
        if(F=='Electric'):
            F1=1
        elif (F=='Hybrid'):
            F2=1
        elif (F=='Diesel'):
            F1,F2,F3,F4=0,0,0,0
        elif (F=='Petrol'):
            F4=1
        else :
            F3=1
            
        

            
            
            
        prediction=model.predict([[Year,Mileage,Tax,MPG,EG,T1,T2,T3,F1,F2,F3,F4]])
        output=round(prediction[0],2)
        
        return render_template('p1.html',prediction_text="Car Price is {}".format(output))


if __name__=="__main__":
    app.run()
