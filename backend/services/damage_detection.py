import cv2
import numpy as np
from PIL import Image

def analyze_damage(image_path: str):
    """
    Real image-based damage detection using OpenCV
    """

    # Load image
    image = cv2.imread(image_path)

    if image is None:
        return {
            "damage_type": "Unknown",
            "severity": "Unknown"
        }

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours (possible damage regions)
    contours, _ = cv2.findContours(
        edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # Calculate damage area
    damage_area = 0
    for contour in contours:
        damage_area += cv2.contourArea(contour)

    image_area = image.shape[0] * image.shape[1]
    damage_ratio = damage_area / image_area

    # Decide severity
    if damage_ratio > 0.15:
        severity = "Severe"
        damage_type = "Major Structural Damage"
    elif damage_ratio > 0.05:
        severity = "Moderate"
        damage_type = "Visible Vehicle Damage"
    elif damage_ratio > 0.01:
        severity = "Minor"
        damage_type = "Surface Damage"
    else:
        severity = "Unknown"
        damage_type = "No Clear Damage Detected"

    return {
        "damage_type": damage_type,
        "severity": severity,
        "damage_ratio": round(damage_ratio, 4)
    }
