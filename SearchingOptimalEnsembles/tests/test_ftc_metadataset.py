from pathlib import Path
import os

from SearchingOptimalEnsembles.metadatasets.ftc.metadataset import FTCMetaDataset

if __name__ == "__main__":
    data_dir = Path(os.path.dirname(os.path.abspath(__file__))) /  "data" 
    data_version = "extended"
    metadataset = FTCMetaDataset( metric_name="error",
                                 data_version=data_version)
    metadataset.set_state(dataset_name=metadataset.get_dataset_names()[1]
                          )
    #metadataset.evaluate_ensembles([[1,2],[3,4]])
    hp_candidates, indices = metadataset._get_hp_candidates_and_indices()
    metrics = metadataset.evaluate_ensembles([indices.tolist()])[2].T
    print("Done")