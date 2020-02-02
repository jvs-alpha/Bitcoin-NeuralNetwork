import pandas as pd
import matplotlib.pyplot as plt
import sys

def viewGraph(filename,xval,yval):
    csv_data = pd.read_csv(filename)
    csv_data.plot(kind="line",x=xval,y=yval)
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage python3 viewGraph.py <filename> <x-title> <y-title>")
    else:
        viewGraph(sys.argv[1],sys.argv[2],sys.argv[3])
