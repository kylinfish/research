import numpy as np

class Bunch(dict):
    """Container object for datasets: dictionary-like object that
       exposes its keys as attributes."""

    def __init__(self, **kwargs):
        dict.__init__(self, kwargs)
        self.__dict__ = self
        
        
def read_data(filename):
    file_feature = open(filename, "r")
    define = file_feature.readline().split(", ")
    n_samples = int(define[0])
    n_features = int(define[1])
    target_names = np.array(define[2].split("\n")[0].split("|"))
    data = np.empty((n_samples, n_features))
    target = np.empty((n_samples,), dtype=np.int)
    
    for i, obj in enumerate(file_feature):
        tmp=[]
        for fea in obj.split(", ")[:-1]:
            tmp.append(fea)
        data[i] = np.asarray(fea, dtype=np.float)
        target[i] = np.asarray(obj.split(", ")[-1], dtype=np.int)
    return Bunch(data=data, target=target,
                 target_names=target_names,
                 feature_names=['R (mean)', 'G (mean)','B(mean)'])