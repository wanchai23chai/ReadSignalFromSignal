import pyedflib
import numpy as np
f = pyedflib.EdfReader("shhs2-200078.edf")
n = f.signals_in_file
print("signal:",n)
signal_labels = f.getSignalLabels()
print signal_labels 
s = f.getNSamples()  
print(s)

	
