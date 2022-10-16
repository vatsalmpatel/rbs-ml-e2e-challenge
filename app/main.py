"""
File Containing all the code for the FastAPI project. This file will create a FastAPI instance and then takes in a 
query and returns a JSON response if there is a signature in the predicted image or not and if present then it will
return the location of the signature in the image as well the confidence with which it thinks that it is an actual 
image.
"""

from fastapi import FastAPI
from typing import Optional
import uvicorn
import requests
import os
import numpy as np
import shutil
from PIL import Image
from detect import run

port = os.environ["PORT"]

app =  FastAPI()

@app.get("/")
async def home_view():
    """
        Returns a home view on the '/' address which displays a basic json response.

        Parameters
        ----------

        Returns
        -------
        Returns a JSON response stating just a basic message to show that the web-page is working
    """
    return {"hello-change": "Staging"}

@app.get("/img")
async def img_echo_view(q: Optional[str]= None):
    """
        Return a JSON response containing the location of the signature in the image with the confidence with which it
        predicts the signature and if there is not signature, it will return nothing. This function will make a call
        to another helper function "call_detect" which will help in actual signature detection.

        Parameters
        ----------
        q: a link of the image which will be used for prediction

        Returns
        -------
        result: a json response that will inform if there is a signature in the image or not
    """
    if q == None:
        return {"query": "use /?q=(url) to submit the url."}
    else:
        if q.endswith('.jpeg') or q.endswith('.jpg') or q.endswith('.png') or 1:
            response = requests.get(q, stream=True)
            response.raw.decode_content = True
            result= call_detect(q)
            if result:
                return result
            else:
                return {"result" : "False"}

def call_detect(q):
    """
        Return the location of signature in the image with the confidence with which it thinks it is an actual signature.
        This function will use the trianed YOLOv5 model weights and the 'run' method provided by the YOLO model to detect
        signature in the image.

        Parameters
        ----------
        q: a query(link) of the image that we will use to detect signatures

        Returns
        -------
        json_file: will contain a json response that describes the location of signature in the image and the confidence level of the model
    """
    json_file= {'prediction': {}}
    key=0
    name_ext=q.split("/")[-1]
    name= name_ext.split(".")[0]
    try:
        os.mkdir("/detect")
    except:
        pass
    path= "detect/"+name

    name=q.split("/")[-1].split(".")[0]
    run(weights= "yolo_signature.pt", source= q, save_txt= True, save_conf= True, name= name, project= "detect", data= "", conf_thres= 0.5)

    path_labels= path+"/labels"

    for file_name in os.listdir(path_labels):
        data= np.loadtxt(path_labels+"/"+file_name)
        try:
            for row in data:
                element= {}
                element['left']= row[1]
                element['top']= row[2]
                element['width']= row[3]
                element['height']= row[4]
                element['conf']= row[5]

                json_file['prediction'][key]= element
                key+= 1
        except:
            element= {}
            element['left']= data[1]
            element['top']= data[2]
            element['width']= data[3]
            element['height']= data[4]
            element['conf']= data[5]

            json_file['prediction'][key]= element
            key+= 1
    shutil.rmtree(path)
    os.remove(name_ext)
    return json_file

if __name__ == "__main__":
    uvicorn.run("main:app", host = "0.0.0.0",port = int(port),reload=True)