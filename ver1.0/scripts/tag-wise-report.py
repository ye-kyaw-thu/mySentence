# Print classification report for tags
# How to run : python tag-wise-report.py <reference-file> <hypothesis-file>
# Written by Thura Aung
# e.g : python tag-wise-report.py test.para_only.tg pySBD.para_only.tg
# Output :
#              precision    recall  f1-score   support
#
#           B       0.86      0.37      0.52      2092
#           E       0.91      0.38      0.54      2149
#           N       0.87      0.41      0.55      5749
#           O       0.79      0.98      0.88     23057

#    accuracy                           0.81     33047
#   macro avg       0.86      0.54      0.62     33047
#weighted avg       0.82      0.81      0.78     33047


import sys
from sklearn import metrics
from sklearn.metrics import confusion_matrix

refFile = open(sys.argv[1], 'r')
hypFile = open(sys.argv[2], 'r')
	
ref_lst = []
hyp_lst = []

def flatten(l):
    return [item for sublist in l for item in sublist]

for r, h in zip(refFile, hypFile):
	rlst = r.split()
	hlst = h.split()
	ref_lst.append(rlst)
	hyp_lst.append(hlst)


ref = flatten(ref_lst)
hyp = flatten(hyp_lst)

print(hypFile)
print(metrics.classification_report(ref, hyp))
print("Confusion matrix is \n", confusion_matrix(ref, hyp, labels=["B","O","N","E"]))

refFile.close()
hypFile.close()	
