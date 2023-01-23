import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist    
import pandas as pd
import numpy as np  
import csv
dataset='/home/vishnu/Documents/A_ZHandwritten Data.csv' 
# z=open(dataset)
def load_aphabets_dataset(datapath):
        # x=pd.read_csv(datapath)         
        # # print(x)
        # for row in x:
        #         row=row.split(",")
        #         #print(row)
        #         print(row[1:
        data=[]
        labels=[]
        for row in open(dataset):
                row=row.split(",")
                label=int(row[0])
                image=np.array([int(i) for i in row[1:]],dtype="uint8")
                # print(image.shape)
                if(image.shape==(784,)):
                        image=image.reshape((28,28))
                        # print(image)
                        data.append(image)
                else:
                        image=image.reshape((32,19))
                labels.append(label)
        # print(len(data))
        # print(data[0])
        data=np.array(data,dtype="float32")
        # if(lables[0]==lables[1]):
        #         print('true')
        labels=np.array(labels,dtype="int")
        return (data,labels)
load_aphabets_dataset(dataset)   
def load_numbers_dataset():
        ((trainData, trainLabels), (testData, testLabels)) = mnist.load_data()
        # print(trainData.shape)
        # print(trainLabels.shape)
        data = np.vstack([trainData, testData])#it combines rows of the data
        # print(data.shape)
        labels = np.hstack([trainLabels, testLabels])#it combines columns of the data
        # print(labels.shape) 
        return (data,labels)  
load_numbers_dataset()