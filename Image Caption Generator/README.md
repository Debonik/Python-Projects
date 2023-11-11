# Image Caption Generator with TensorFlow

This script sets up an image captioning system using a pre-trained InceptionV3 model for feature extraction and a custom model for generating captions.

## Components of the Script

- **Importing Libraries**: TensorFlow for machine learning, Matplotlib for plotting, NumPy for numerical operations, and PIL for image processing.

- **Model Loading**: The InceptionV3 model, pre-trained on ImageNet, is loaded for image feature extraction.

- **Tokenizer**: A tokenizer is loaded from a `.pkl` file, which will convert words to indices and vice versa, necessary for processing text for the model.

- **Maximum Sequence Length**: The maximum length for generated captions is set to 20 words.

- **Caption Generation Model**: A custom model for generating captions is loaded from an `.h5` file.

- **Word Mappings**: Dictionaries for converting between words and their corresponding indices in the model's vocabulary are established.

- **Preprocess Image**: A function to resize and normalize an image to be suitable for input to the InceptionV3 model.

- **Generate Caption**: This function preprocesses the image, extracts features using InceptionV3, and then generates a caption word by word using the custom model and tokenizer.

## Usage

1. An image path is specified for the image that needs a caption.
2. The `generate_caption` function is called with the image path, which prints the generated caption.
3. The image is displayed without axes using Matplotlib.

## Output

The script outputs the generated caption for the input image and then displays the image.

## Example Run

- Set the `image_path` variable to the path of your image.
- Run the script.
- View the printed 'Generated Caption' and the displayed image.
