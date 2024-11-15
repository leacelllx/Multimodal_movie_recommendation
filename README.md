# 🎥 ***Multimodal Movie Recommendation with LLaMA 3.2***

An advanced movie recommendation system leveraging **LLaMA 3.2** and multimodal data (text, images, audio, and video metadata) to generate personalized and emotion-aware suggestions. The project integrates Retrieval-Augmented Generation (RAG) for retrieving and recommending movies based on user preferences.

---

## 🚀 **Features**

1. **Multimodal Input**:  
   Supports **text** (metadata, synopsis), **images** (posters), **audio** (transcripts—due to legal issues, soundtracks were removed from the project), and **video** (trailers).

2. **Retrieval-Augmented Generation (RAG)**:  
   Combines multimodal embeddings for retrieving and recommending movies.

3. **Emotion-Aware Recommendations**:  
   Adapts suggestions based on recognized emotions from user input and movie content.

4. **Explainable AI**:  
   Provides explanations for each recommendation based on input features.

---

## 📁 **Repository Structure**

```plaintext
multimodal-movie-recommendation/
│
├── README.md                # Project overview and instructions
├── requirements.txt         # Python dependencies
├── data/                    # Sample datasets and preprocessed data
│   ├── raw/                 # Raw datasets (movie posters, metadata, etc.)
│   ├── processed/           # Preprocessed embeddings or extracted features
│
├── src/                     # Source code
│   ├── data_preprocessing/  # Scripts for data preparation
│   ├── models/              # Model loading and fine-tuning scripts
│   ├── multimodal_rag/      # RAG implementation scripts
│   ├── ui/                  # Streamlit or Gradio UI scripts
│   ├── utils/               # Utility scripts (e.g., logging, evaluation)
│
├── notebooks/               # Jupyter notebooks for experimentation
│   ├── data_exploration.ipynb
│   ├── model_finetuning.ipynb
│   ├── multimodal_testing.ipynb
│
├── tests/                   # Unit tests for the project
├── docker/                  # Docker-related files
└── deployment/              # Deployment scripts
```
## 📦 Installation

### Clone the Repository:
```bash
git clone https://github.com/your-username/multimodal-movie-recommendation.git
cd multimodal-movie-recommendation
```

### Set Up Environment:

Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Download Data:

Download the required datasets and place them in the data/raw/ directory.
#### Preprocess Data:

Run preprocessing scripts to generate embeddings:
```bash
python src/data_preprocessing/preprocess_data.py
```
## 🛠 Usage
### 1. Run Locally
Start the Streamlit/Gradio app:
```bash
streamlit run src/ui/app.py
```
Open the link provided in the terminal to interact with the app.
### 2.  Run Notebooks
Use Jupyter notebooks in the notebooks/ directory to explore and experiment with the dataset and models.
## 🧠 Model Details

### LLaMA 3.2 Fine-Tuning
- **Base Model**: LLaMA 3.2
- **Fine-Tuning Task**: Movie recommendation-related text generation.
- **Multimodal Embeddings**:
  - **Image**: Processed with ImageBind.
  - **Audio**: Processed with Whisper or CLAP.
  - **Text**: Processed with LLaMA tokenizer and embeddings.
  - **Video**: Extracted keyframes processed via CLIP and subtitles for text embeddings.

---

## 📊 Evaluation

### Metrics:
- **NDCG (Normalized Discounted Cumulative Gain)**
- **Precision@k**
- **Mean Reciprocal Rank (MRR)**

Evaluation scripts are available in `src/utils/evaluation.py`.

---

## 🌐 Deployment

### Deploy to Hugging Face Spaces:
1. Create a new Hugging Face Space.
2. Push the repository to the Space.
3. Ensure the app runs via `app.py`.

### Deploy Using Docker:
1. Build the Docker image:
   ```bash
   docker build -t multimodal-movie-recommendation .
   ```
2. Run the container:
```bash
docker run -p 8501:8501 multimodal-movie-recommendation
```
## 📚 Datasets
- IMDB dataset: Metadata for movies, including titles, genres, and ratings.
- Trailer 12K: Movie Posters and Trailers
- Soundtracks: eliminated.

## ✨ Acknowledgements
Hugging Face for the Transformers library.
FAISS for efficient retrieval indexing.
ImageBind for multimodal embeddings.
Open-source datasets like MovieLens and others.



# IN PROCESS:
## ✅ fine tune LLama 3.2 multimodal (overfitted will add evaluation)
## ✅  Got embeddings 
