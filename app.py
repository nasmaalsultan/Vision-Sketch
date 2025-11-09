import os
import torch
from flask import Flask, request, jsonify, send_file, render_template
from diffusers import StableDiffusionPipeline
import io
from datetime import datetime
import base64

app = Flask(__name__)

# Initialize the pipeline
print("Loading Stable Diffusion model...")
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Using device: {device}")
pipe = pipe.to(device)
print("Model loaded successfully!")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        data = request.json
        prompt = data.get('prompt', '')

        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        print(f"Generating image for prompt: {prompt}")

        # Generate image
        with torch.autocast("cpu" if device == "cpu" else "mps"):
            image = pipe(prompt).images[0]

        # Convert image to base64 for web display
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)

        # Also save to file for download
        base_name = "generated_image_"
        extension = ".png"
        i = 1
        while os.path.exists(f"{base_name}{i}{extension}"):
            i += 1

        output_path = f"{base_name}{i}{extension}"
        image.save(output_path)
        print(f"Image saved as {output_path}")

        # Return both base64 for display and filename for download
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

        return jsonify({
            'success': True,
            'image': f"data:image/png;base64,{img_base64}",
            'download_filename': output_path,
            'prompt': prompt,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)