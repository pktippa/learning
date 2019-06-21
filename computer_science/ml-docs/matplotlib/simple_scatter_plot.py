import csv
import matplotlib.pyplot as plt
input_csv=open("trainingdata.csv","r")
input_csv_text=csv.reader(input_csv)
# Extracting features and labels
X_features,y_labels = zip(*input_csv_text)
# Converting string to float for features
X_features = list(map(float, X_features))
# Converting string to float for labels
y_labels = list(map(float, y_labels))
plt.scatter(X_features,y_labels)
plt.show()