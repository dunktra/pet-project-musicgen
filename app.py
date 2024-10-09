from audiocraft.models import MusicGen
import streamlit as st
import os
import torch
import torchaudio
import base64

# Cache the model to avoid reloading and reinitializing for every request
@st.cache_resource
def load_model():
    model = MusicGen.get_pretrained("facebook/musicgen-small")
    return model

# Function to generate music based on the description and duration
def generate_music(description: str, duration: int):
    model = load_model()
    # Set the duration and other generation parameters
    model.set_generation_params(duration=duration)
    # Generate music based on text description
    output = model.generate([description])
    return output[0]

# Function to save the generated audio to a file
def save_audio_to_file(samples: torch.Tensor, save_dir="audio_output/"):
    sample_rate = 32000
    os.makedirs(save_dir, exist_ok=True)

    samples = samples.detach().cpu()
    if samples.dim() == 2:
        samples = samples[None, ...]

    audio_path = os.path.join(save_dir, f"audio_0.wav")
    torchaudio.save(audio_path, samples[0], sample_rate)  # Save only the first generated sample
    return audio_path

# Helper function to create a download link for audio files
def create_download_link(bin_file, label='Download File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    encoded_data = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{encoded_data}" download="{os.path.basename(bin_file)}">{label}</a>'
    return href

# Set Streamlit page configuration
st.set_page_config(
    page_title="Music Generator",
    page_icon=":notes:",
)

# Main function to run the app
def main():
    st.title("Word-to-Melody Machine")
    st.write("Turn words into music with Meta's Audiocraft and MusicGen—where your ideas become soundtracks :notes:")

    description = st.text_area("Write your music recipe:")
    duration = st.slider("Select duration (seconds)", min_value=2, max_value=10, value=5)

    if description:
        if st.button("Generate Music"):
            with st.spinner('Sprinkling magic...'):
                music_samples = generate_music(description, duration)
                audio_path = save_audio_to_file(music_samples)

                audio_file = open(audio_path, 'rb')
                audio_bytes = audio_file.read()

                st.audio(audio_bytes, format='audio/wav')
                st.markdown(create_download_link(audio_path, 'Download Audio'), unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
