from google.cloud import storage
from imagebind import data
import torch
from imagebind.models import imagebind_model
from imagebind.models.imagebind_model import ModalityType
import os

def download_files_from_gcs(bucket_name, prefix, local_path):
    """Download files from a GCS bucket."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)

    for blob in blobs:
        file_path = os.path.join(local_path, blob.name.split("/")[-1])
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        blob.download_to_filename(file_path)
        print(f"Downloaded {blob.name} to {file_path}")

# Set up GCS bucket and paths
BUCKET_NAME = "multimodal_recomm"
VIDEO_PREFIX = "multimodal/videos/"
POSTER_PREFIX = "multimodal/posters/"
DESCRIPTION_PREFIX = "multimodal/descriptions/"
LYRICS_PREFIX = "multimodal/lyrics/"
LOCAL_DOWNLOAD_PATH = "./gcp_downloads"

# Download data
download_files_from_gcs(BUCKET_NAME, VIDEO_PREFIX, LOCAL_DOWNLOAD_PATH + "/videos")
download_files_from_gcs(BUCKET_NAME, POSTER_PREFIX, LOCAL_DOWNLOAD_PATH + "/posters")
download_files_from_gcs(BUCKET_NAME, DESCRIPTION_PREFIX, LOCAL_DOWNLOAD_PATH + "/descriptions")
download_files_from_gcs(BUCKET_NAME, LYRICS_PREFIX, LOCAL_DOWNLOAD_PATH + "/lyrics")

# Prepare inputs for ImageBind
text_list = []
image_paths = []
audio_paths = []

# Read text data
for file_name in os.listdir(LOCAL_DOWNLOAD_PATH + "/descriptions"):
    with open(os.path.join(LOCAL_DOWNLOAD_PATH + "/descriptions", file_name), "r") as f:
        text_list.append(f.read())

for file_name in os.listdir(LOCAL_DOWNLOAD_PATH + "/lyrics"):
    with open(os.path.join(LOCAL_DOWNLOAD_PATH + "/lyrics", file_name), "r") as f:
        text_list.append(f.read())

# Gather paths for visual and audio data
image_paths = [os.path.join(LOCAL_DOWNLOAD_PATH + "/posters", file) for file in os.listdir(LOCAL_DOWNLOAD_PATH + "/posters")]
audio_paths = [os.path.join(LOCAL_DOWNLOAD_PATH + "/videos", file) for file in os.listdir(LOCAL_DOWNLOAD_PATH + "/videos")]

device = "cuda:0" if torch.cuda.is_available() else "cpu"

# Instantiate model
model = imagebind_model.imagebind_huge(pretrained=True)
model.eval().to(device)

inputs = {
    ModalityType.TEXT: data.load_and_transform_text(text_list, device),
    ModalityType.VISION: data.load_and_transform_vision_data(image_paths, device),
    ModalityType.AUDIO: data.load_and_transform_audio_data(audio_paths, device),
}

# Run embeddings
with torch.no_grad():
    embeddings = model(inputs)

# Print similarities
print("Vision x Text:", torch.softmax(embeddings[ModalityType.VISION] @ embeddings[ModalityType.TEXT].T, dim=-1))
print("Audio x Text:", torch.softmax(embeddings[ModalityType.AUDIO] @ embeddings[ModalityType.TEXT].T, dim=-1))
print("Vision x Audio:", torch.softmax(embeddings[ModalityType.VISION] @ embeddings[ModalityType.AUDIO].T, dim=-1))
