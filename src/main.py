import cv2
import numpy as np

def count_mosquito_eggs(image_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Use binary thresholding to segment the image
    _, threshed_image = cv2.threshold(blurred_image, 100, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours,_ = cv2.findContours(threshed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original image (for visualization)
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    # Count the number of mosquito eggs
    egg_count = len(contours)

    # Display the result
    print(f"Number of mosquito eggs: {egg_count}")

    # Show the original image with contours
    #cv2.imshow("Image with Contours", image_with_contours)
    
    cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('custom window', image_with_contours)
    cv2.resizeWindow('custom window', 200, 200)

    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "img/20200214_143902.jpg"  # Replace with the path to your JPG image
    count_mosquito_eggs(image_path)
