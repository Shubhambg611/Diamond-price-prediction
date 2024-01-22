from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData,PredictPipeline 
from flask import Flask,request,render_template,jsonify

app=Flask(__name__)
@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/prediction',method=["GET","POST"])
def predict_datapoints():
    pass
    

app.run()