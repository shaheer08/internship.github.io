import pandas as pd
import numpy as np
att_status={ 
            'Staff': pd.Series([5, 6, 7, 9, 10, 4, 5, 6, 4, 8], index=['1','2','3','4','5','6','7','8','9','10']),
            'Students': pd.Series([25, 30, 26, 14, 12, 24, 28, 27, 21, 22], index=['1','2','3','4','5','6','7','8','9','10'])
           }
df=pd.DataFrame(att_status)
#see the frame
print(df)
#Plot
import matplotlib.pyplot as plt
plt.plot(df)
plt.ylabel('Attendance')
plt.xlabel('Day')
plt.show()
