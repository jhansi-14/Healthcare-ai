import cv2

def analyze_medical_image(path):

    img = cv2.imread(path)

    if img is None:
        return "Image not readable"

    height, width = img.shape[:2]

    return f"Image analyzed: {width}x{height}"