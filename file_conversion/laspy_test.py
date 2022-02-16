import laspy
import numpy as np

las = laspy.read('NZ19_Wellington.las')

print(np.unique(las.classification))