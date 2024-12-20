# Databricks notebook source
df = spark.read.csv("/mnt/volume/your_file.csv", header=True, inferSchema=True)
display(df)
