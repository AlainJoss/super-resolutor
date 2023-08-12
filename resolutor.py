import cv2
from cv2 import dnn_superres
import os
import resources

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read the desired model
sr.readModel(resources.X4_MODEL)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 4)

# Read image
image = cv2.imread(resources.IMAGE_PATH)

# Upscale the image
result = sr.upsample(image)

# Save the image
os.makedirs('app/results', exist_ok=True)  # Creates 'results' directory inside 'app' directory
cv2.imwrite("app/results/upscaled.png", result)  # The image will be saved in 'app/results' directory