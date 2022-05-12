# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 14:00:20 2022

@author: bsaiv
"""

from flask import Flask,render_template, request,jsonify
application = Flask(__name__)
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA
import  math 
from sklearn.manifold import MDS
from sklearn import metrics

application.config['JSON_SORT_KEYS'] = False

@application.route('/')
def index():
    return render_template("Dashboard.html")

@application.route('/Map_chart', methods=['GET', 'POST'])
def Map_chart():
    data  = pd.read_csv('static/data/Processed_file.csv')
    data = data.query('Latitude.notnull() & Longitude.notnull()', engine='python')
    output=data[["Latitude","Longitude"]]
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        return 'Sucesss', 200

@application.route('/Map_Chart_pie', methods=['GET', 'POST'])
def Map_Chart_pie():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data = data.query('Latitude.notnull() & Longitude.notnull()', engine='python')
    data_1 = data.query('Police_District ==@d')
    output=data_1[["Latitude","Longitude"]]
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})
    
@application.route('/Map_Chart_lollipop', methods=['GET', 'POST'])
def Map_Chart_lollipop():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data = data.query('Latitude.notnull() & Longitude.notnull()', engine='python')
    data_1 = data.query('Incident_Category ==@d')
    output=data_1[["Latitude","Longitude"]]
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})
    
@application.route('/Map_Chart_line', methods=['GET', 'POST'])
def Map_Chart_line():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data = data.query('Latitude.notnull() & Longitude.notnull()', engine='python')
    data_1 = data.query('Incident_Year ==@d')
    output=data_1[["Latitude","Longitude"]]
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})

@application.route('/Pie_chart', methods=['GET', 'POST'])
def Pie_chart():
    dataset  = pd.read_csv('static/data/Processed_file.csv')
    count=dataset.groupby(['Police_District']).size().reset_index(name='counts')
    output  = pd.DataFrame([], columns =['year', 'counts'])
    output['year'] = list(count.Police_District)
    output['counts'] = list(count.counts)
    if request.method == 'GET':
        return jsonify({'values' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        return 'Sucesss', 200

@application.route('/Pie_chart_lillipop', methods=['GET', 'POST'])
def Pie_chart_lillipop():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Incident_Category ==@d')
    count=data_1.groupby(['Police_District']).size().reset_index(name='counts')
    output  = pd.DataFrame([], columns =['year', 'counts'])
    output['year'] = list(count.Police_District)
    output['counts'] = list(count.counts)
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})
    
@application.route('/Pie_chart_line_chart', methods=['GET', 'POST'])
def Pie_chart_line_chart():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Incident_Year ==@d')
    count=data_1.groupby(['Police_District']).size().reset_index(name='counts')
    output  = pd.DataFrame([], columns =['year', 'counts'])
    output['year'] = list(count.Police_District)
    output['counts'] = list(count.counts)
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})
    
@application.route('/line_chart', methods=['GET', 'POST'])
def Line_chart():
    data  = pd.read_csv('static/data/Processed_file.csv')
    output=data.groupby(['Incident_Year']).size().reset_index(name="counts")
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        return 'Sucesss', 200

@application.route('/line_chart_pie', methods=['GET', 'POST'])
def Line_chart_pie():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Police_District ==@d')
    output=data_1.groupby(['Incident_Year']).size().reset_index(name="counts")
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})
    
@application.route('/line_chart_lillipop', methods=['GET', 'POST'])
def Line_chart_lillipop():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Incident_Category ==@d')
    output=data_1.groupby(['Incident_Year']).size().reset_index(name="counts")
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})

@application.route('/lollipop_chart', methods=['GET', 'POST'])
def lollipop_chart():
    data  = pd.read_csv('static/data/Processed_file.csv')
    output=data.groupby(['Incident_Category']).size().reset_index(name="counts")
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        return 'Sucesss', 200

@application.route('/lollipop_chart_pie', methods=['GET', 'POST'])
def Lollipop_chart_pie():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Police_District ==@d')
    output=data_1.groupby(['Incident_Category']).size().reset_index(name="counts")
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})
    
@application.route('/lollipop_chart_line_chart', methods=['GET', 'POST'])
def Lollipop_chart_line_chart():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Incident_Year ==@d')
    output=data_1.groupby(['Incident_Category']).size().reset_index(name="counts")
    if request.method == 'GET':
        return jsonify({'data' : output.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output.to_dict('records')})

@application.route('/stats', methods=['GET', 'POST'])
def stats():
    data  = pd.read_csv('static/data/Processed_file.csv')
    output=data.groupby(['Resolution']).size().reset_index(name="counts")
    output_2=data.groupby(['Filed_Online']).size().reset_index(name="counts")
    output_2=output_2[["counts"]]
    output_3=output[output.Resolution == 'Open or Active']
    output_3=output_3[["counts"]]
    output_4=output.query("Resolution =='Cite or Arrest Adult'")
    output_4=output_4[["counts"]]
    output_5=output.query("Resolution =='Exceptional Adult'")
    output_5=output_5[["counts"]]
    output_6=output.query("Resolution =='Unfounded'")
    output_6=output_6[["counts"]]
    if request.method == 'GET':
        return jsonify({'data' : output_6.to_dict('records'), 'data2' : output_2.to_dict('records'), 'data3' : output_3.to_dict('records'), 'data4' : output_4.to_dict('records'), 'data5' : output_5.to_dict('records')})
    if request.method == 'POST':
        return 'Sucesss', 200
    
@application.route('/stats_line_chart', methods=['GET', 'POST'])
def stats_line_chart():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Incident_Year ==@d')
    output=data_1.groupby(['Resolution']).size().reset_index(name="counts")
    output_2=data_1.groupby(['Filed_Online']).size().reset_index(name="counts")
    if(output_2.empty):
        output_2 = pd.DataFrame({"counts": range(1)})
    output_2=output_2[["counts"]]
    output_3=output.query("Resolution =='Open or Active'")
    if(output_3.empty):
        output_3 = pd.DataFrame({"counts": range(1)})
    output_3=output_3[["counts"]]
    output_4=output.query("Resolution =='Cite or Arrest Adult'")
    if(output_4.empty):
        output_4 = pd.DataFrame({"counts": range(1)})
    output_4=output_4[["counts"]]
    output_5=output.query("Resolution =='Exceptional Adult'")
    if(output_5.empty):
        output_5 = pd.DataFrame({"counts": range(1)})
    output_5=output_5[["counts"]]
    output_6=output.query("Resolution =='Unfounded'")
    if(output_6.empty):
        output_6 = pd.DataFrame({"counts": range(1)})
    output_6=output_6[["counts"]]
    if request.method == 'GET':
        return jsonify({'data' : output_6.to_dict('records'), 'data2' : output_2.to_dict('records'), 'data3' : output_3.to_dict('records'), 'data4' : output_4.to_dict('records'), 'data5' : output_5.to_dict('records')})
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output_6.to_dict('records'), 'data2' : output_2.to_dict('records'), 'data3' : output_3.to_dict('records'), 'data4' : output_4.to_dict('records'), 'data5' : output_5.to_dict('records')})

@application.route('/stats_lollipop_chart', methods=['GET', 'POST'])
def stats_lollipop_chart():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Incident_Category ==@d')
    output=data_1.groupby(['Resolution']).size().reset_index(name="counts")
    output_2=data_1.groupby(['Filed_Online']).size().reset_index(name="counts")
    if(output_2.empty):
        output_2 = pd.DataFrame({"counts": range(1)})
    output_2=output_2[["counts"]]
    output_3=output.query("Resolution =='Open or Active'")
    if(output_3.empty):
        output_3 = pd.DataFrame({"counts": range(1)})
    output_3=output_3[["counts"]]
    output_4=output.query("Resolution =='Cite or Arrest Adult'")
    if(output_4.empty):
        output_4 = pd.DataFrame({"counts": range(1)})
    output_4=output_4[["counts"]]
    output_5=output.query("Resolution =='Exceptional Adult'")
    if(output_5.empty):
        output_5 = pd.DataFrame({"counts": range(1)})
    output_5=output_5[["counts"]]
    output_6=output.query("Resolution =='Unfounded'")
    if(output_6.empty):
        output_6 = pd.DataFrame({"counts": range(1)})
    output_6=output_6[["counts"]]
    if request.method == 'GET':
        return jsonify({'data' : output_6.to_dict('records'), 'data2' : output_2.to_dict('records'), 'data3' : output_3.to_dict('records'), 'data4' : output_4.to_dict('records'), 'data5' : output_5.to_dict('records')})
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output_6.to_dict('records'), 'data2' : output_2.to_dict('records'), 'data3' : output_3.to_dict('records'), 'data4' : output_4.to_dict('records'), 'data5' : output_5.to_dict('records')})

@application.route('/stats_pie_chart', methods=['GET', 'POST'])
def stats_pie_chart():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Police_District ==@d')
    output=data_1.groupby(['Resolution']).size().reset_index(name="counts")
    output_2=data_1.groupby(['Filed_Online']).size().reset_index(name="counts")
    if(output_2.empty):
        output_2 = pd.DataFrame({"counts": range(1)})
    output_2=output_2[["counts"]]
    output_3=output.query("Resolution =='Open or Active'")
    if(output_3.empty):
        output_3 = pd.DataFrame({"counts": range(1)})
    output_3=output_3[["counts"]]
    output_4=output.query("Resolution =='Cite or Arrest Adult'")
    if(output_4.empty):
        output_4 = pd.DataFrame({"counts": range(1)})
    output_4=output_4[["counts"]]
    output_5=output.query("Resolution =='Exceptional Adult'")
    if(output_5.empty):
        output_5 = pd.DataFrame({"counts": range(1)})
    output_5=output_5[["counts"]]
    output_6=output.query("Resolution =='Unfounded'")
    if(output_6.empty):
        output_6 = pd.DataFrame({"counts": range(1)})
    output_6=output_6[["counts"]]
    if request.method == 'GET':
        return jsonify({'data' : output_6.to_dict('records'), 'data2' : output_2.to_dict('records'), 'data3' : output_3.to_dict('records'), 'data4' : output_4.to_dict('records'), 'data5' : output_5.to_dict('records')})
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : output_6.to_dict('records'), 'data2' : output_2.to_dict('records'), 'data3' : output_3.to_dict('records'), 'data4' : output_4.to_dict('records'), 'data5' : output_5.to_dict('records')})

@application.route('/area_chart', methods=['GET', 'POST'])
def area_chart():
    data  = pd.read_csv('static/data/Processed_file.csv')
    output=data.groupby(['Incident_Datetime']).size().reset_index(name="counts")
    output.rename(columns = {'Incident_Datetime':'time'}, inplace = True)
    output['time'] =pd.to_datetime(output['time'])
    #output_data=output[['time','counts']]
    output['time'] = output.time.apply(lambda x: x.hour)
    dataset=output[['time']]
    if request.method == 'GET':
        return jsonify({'data' : dataset.to_dict('records')})
    if request.method == 'POST':
        return 'Sucesss', 200
    
@application.route('/area_chart_line_chart', methods=['GET', 'POST'])
def area_chart_line_chart():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Incident_Year ==@d')
    output=data_1.groupby(['Incident_Datetime']).size().reset_index(name="counts")
    output.rename(columns = {'Incident_Datetime':'time'}, inplace = True)
    output['time'] =pd.to_datetime(output['time'])
    #output_data=output[['time','counts']]
    output['time'] = output.time.apply(lambda x: x.hour)
    dataset=output[['time']]
    if request.method == 'GET':
        return jsonify({'data' : dataset.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : dataset.to_dict('records')})
    
@application.route('/area_chart_lollipop_chart', methods=['GET', 'POST'])
def area_chart_lollipop_chart():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Incident_Category ==@d')
    output=data_1.groupby(['Incident_Datetime']).size().reset_index(name="counts")
    output.rename(columns = {'Incident_Datetime':'time'}, inplace = True)
    output['time'] =pd.to_datetime(output['time'])
    #output_data=output[['time','counts']]
    output['time'] = output.time.apply(lambda x: x.hour)
    dataset=output[['time']]
    if request.method == 'GET':
        return jsonify({'data' : dataset.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : dataset.to_dict('records')})
    
@application.route('/area_chart_pie_chart', methods=['GET', 'POST'])
def area_chart_pie_chart():
    d = request.get_json()["post"]
    data  = pd.read_csv('static/data/Processed_file.csv')
    data_1 = data.query('Police_District ==@d')
    output=data_1.groupby(['Incident_Datetime']).size().reset_index(name="counts")
    output.rename(columns = {'Incident_Datetime':'time'}, inplace = True)
    output['time'] =pd.to_datetime(output['time'])
    #output_data=output[['time','counts']]
    output['time'] = output.time.apply(lambda x: x.hour)
    dataset=output[['time']]
    if request.method == 'GET':
        return jsonify({'data' : dataset.to_dict('records')})  # serialize and use JSON headers
    if request.method == 'POST':
        d=request.get_json()
        return jsonify({'data' : dataset.to_dict('records')})
    


if __name__ == "__main__":
   
    application.debug = True
    application.run()
    application.run(debug = True)