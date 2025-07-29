import pandas as pd
dict={
	'names':['alice', 'bob', 'charlie'],
	'age':[25, 30, 35],
	'score':[88, 76, 91]
	}
mydata=pd.DataFrame(dict)
print(mydata.head(2))
