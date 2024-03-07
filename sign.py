import cv2
from skimage.metrics import structural_similarity as ssim
import imghdr
from tkinter import Tk, filedialog


def load_and_preprocess_image(image_path, target_size=(300, 300)):
    # Load the image and resize it to the target size while maintaining the aspect ratio
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    
    # Convert the resized image to grayscale
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    
    return gray_image

def compare_images(image1, image2):
    # Compute the Structural Similarity Index (SSI) between the two images
    score, _ = ssim(image1, image2, full=True)
    return score

def browse_image():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    return file_path

def main():
    # Get the file paths for the reference and input signature images
    print("Select the reference signature image:")
    reference_signature_path = browse_image()

    print("Select the input signature image:")
    input_signature_path = browse_image()

    # Load and preprocess the images
    reference_signature = load_and_preprocess_image(reference_signature_path)
    input_signature = load_and_preprocess_image(input_signature_path)
    
    # Compare the images
    similarity_score = compare_images(reference_signature, input_signature)

    # Set a threshold for similarity (adjust as needed)
    similarity_threshold = 0.82

    # Check if the similarity score is above the threshold
    if similarity_score > similarity_threshold:
        print("Signatures match! Similarity Score:", similarity_score)
    else:
        print("Signatures do not match. Similarity Score:", similarity_score)

if __name__ == "__main__":
    main()

