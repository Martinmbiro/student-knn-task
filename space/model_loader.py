import joblib, os
from huggingface_hub import hf_hub_download

# get model path
model_path = hf_hub_download(
    repo_id='martinmbiro/student_knn',
    filename='knn_model.joblib',
    token=os.environ.get('HF_TOKEN')
  )

# load model from joblib file
model = joblib.load(filename=model_path)
