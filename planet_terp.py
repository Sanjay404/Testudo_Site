import requests
import json
import io
import csv
import pandas as pd

def num_credits(course_code):
    payload = requests.get('https://api.planetterp.com/v1/course', params={'name':course_code}).json()
    return payload['credits']

def get_professor(course_code):
    payload = requests.get('https://api.planetterp.com/v1/course', params={'name':course_code}).json()
    return payload['professors']

def avg_gpa(course_code):
    headers = { 'Accept': 'application/json'}
    payload = requests.get( 'https://api.planetterp.com/v1/grades', params={"course": course_code}, headers = headers).json()
    distribution = {'A+':4,'A':4,'A-':3.7,'B+':3.3,'B':3,'B-':2.7,'C+':2.3,'C':2,'C-':1.7,'D+':1.3,'D':1,'D-':0.7,'F':0}
    avg_gpa = 0
    for semester in payload: # iterates through all dictionaries
        temp_gpa = student_count = 0
        for grade in semester.keys(): #goes thru all the keys
            if grade in distribution:
                temp_gpa+= distribution[grade]*semester[grade]
                student_count+=semester[grade]
        avg_gpa+= temp_gpa/student_count
    
    return round(avg_gpa/len(payload),2)


def pandas_osmthing(olympic, country):
    df = pd.read_csv(io.StringIO(requests.get("http://winterolympicsmedals.com/medals.csv").text), delimiter = ',')
    print(df.head(),'\n', olympic, country)
    temp = df.loc[(df.City == olympic) & (df.Medal == "Gold") & (df.NOC == country)]
    return len(temp)
    

if __name__ == '__main__':
   pass