'''Pandas is python libaries use for data analysis and manipulation for .csv or .json or excel files '''
import pandas as p
""" this function pandas is use for the reading the dataset(dataframe)"""
#data_set = p.read_json("Pandas.py/sample_Data.json")
#data_set = p.read_csv("Pandas.py/car details v4.csv")
data_set = p.read_excel("Pandas.py/archive.zip/SampleSuperstore.xlsx", engine="openpyxl")
print(data_set)

