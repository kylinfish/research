import preprocess as pp
import dataset as dataset

#extract feature and store to txt
pp.Make_feature_set()

flower = dataset.read_data("data/feature.txt")
