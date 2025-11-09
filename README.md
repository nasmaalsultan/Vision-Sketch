# Vision-Sketch

VisionSketch is a web-based research tool built to explore the ethical boundaries of AI image generation.
It uses Stable Diffusion v1.5 to generate images from text prompts and helps analyze how AI models respond to prompts that may be creative, sensitive, or ethically challenging.

## Features

- Web Interface: Intuitive, responsive web app powered by Flask
- Real-time Generation: Generate images from your text prompts using Stable Diffusion
- Image Download: Download your generated images instantly
- History Tracking: Keeps a list of your generated prompts and timestamps
- AI Ethics Exploration: Designed for use in research projects related to AI ethics

## Project Structure

VisionSketch/
│
├── templates/
│   └── index.html         # Frontend interface for prompt input and image display
│
├── app.py                 # Flask web server for generating and serving images
├── vision_sketch.py       # Command-line interface version
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # License file (add your preferred license)
└── .gitignore             # Git ignore rules

## Installation

1. Clone the repository
git clone https://github.com/yourusername/vision-sketch.git
cd visionsketch

2. Set up a Python environment
python3 -m venv venv
source venv/bin/activate     # (or on Windows: venv\Scripts\activate)

3. Install dependencies
pip install -r requirements.txt

4. Run the app
python app.py

## Command-Line Version

If you prefer to generate images directly from the terminal:
python vision_sketch.py

You’ll be prompted to enter a description, and the generated image will be saved locally as:
generated_image_<number>.png

## Example Usage

<img width="600" height="720" alt="Screenshot 2025-11-09 at 17 13 33" src="https://github.com/user-attachments/assets/45c105a9-e334-4255-bee7-17e369b11950" />
