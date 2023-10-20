import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))


res = (df.sum(axis=1)>100)

print(df[res])