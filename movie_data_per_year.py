import pandas as pd
import numpy
import matplotlib.pyplot as plt
import sys
sys.__stdout__ = sys.stdout

url = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
movie_data = pd.read_csv(url, encoding="Latin-1")

mean_dur_by_year = movie_data.pivot_table(index="title_year", values="duration", aggfunc=numpy.mean)
min_dur_by_year = movie_data.pivot_table(index="title_year", values="duration", aggfunc=numpy.min)
max_dur_by_year = movie_data.pivot_table(index="title_year", values="duration", aggfunc=numpy.max)

plt.plot(mean_dur_by_year, "r")
plt.plot(min_dur_by_year, "b")
plt.plot(max_dur_by_year, "g")
plt.show()
