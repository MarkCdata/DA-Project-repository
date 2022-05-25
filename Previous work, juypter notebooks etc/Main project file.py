import pandas as pd
import numpy as np
filename = "Movies.csv"
Movies = pd.read_csv(r"C:\Users\markc\Desktop\Movies.csv")

Movies.info()
Movies.drop("poster_path", inplace=True, axis=1)
Movies.drop("backdrop_path", inplace=True, axis=1)
Movies.drop("recommendations", inplace=True, axis=1)
Movies.drop("production_companies", inplace=True, axis=1)



print(Movies)