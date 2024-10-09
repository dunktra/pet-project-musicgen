# pet-project-musicgen
A pet project that turns text to music using Meta's Audiocraft and MusicGen modal. Credits of creation go to AI Anytime.

### Installation Instructions

Follow these steps to clone the repository, install the necessary dependencies, and run the app locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dunktra/pet-project-musicgen.git
   cd pet-project-musicgen
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate   # For Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   Install all required Python packages from the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install additional libraries**:
   Install `Streamlit`, `Torch`, `Torchaudio`, and `Audiocraft` (if not already included):
   ```bash
   pip install streamlit torch torchaudio audiocraft
   ```

5. **Run the app**:
   ```bash
   streamlit run app.py
   ```

6. **Access the app**:
   Open your browser and go to the following URL:
   ```
   http://localhost:8501
   ```

### Important Notes:
- **No need to clone Meta's Audiocraft repository**: The app will automatically download the required MusicGen model (e.g., `facebook/musicgen-small`) from Meta’s servers when the app is first run.
- Ensure that you have a stable internet connection to allow Audiocraft to fetch the model during runtime. 

This will set up and run the app, allowing you to generate music based on natural language input!


Resources:
- Tutorial: https://www.youtube.com/watch?v=UqsW9IK8pCI
- Audiocraft library: https://github.com/facebookresearch/audiocraft
