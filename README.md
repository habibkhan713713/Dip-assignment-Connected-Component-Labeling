# Dip-assignment-Connected-Component-Labeling
Connected Component Labeling with Color Mapping

This Python code performs connected component labeling on a binary image and then generates a colored image with unique colors for each connected component.
Overview

Connected component labeling is a technique used in image processing to identify and label connected regions in a binary image. This code takes an input binary image, labels each connected component, and then creates a new image where each connected component is assigned a unique color. This is a common technique used in various image analysis tasks.
Prerequisites

Before running the code, make sure you have the following libraries installed:

    OpenCV (cv2)
    NumPy (numpy)

You can install these libraries using pip:

bash

pip install opencv-python-headless
pip install numpy

Usage

    Save your binary image as 'img.bmp' in the same directory as the code.

    Run the code using a Python interpreter.

    The code will perform connected component labeling and generate two images:
        "Labeled Image" shows the connected components labeled with unique integers.
        "Colored Result" shows the connected components in unique colors.

    Close the image windows to exit the application.

Code Explanation

    The code starts by thresholding the input image to create a binary image.

    It performs connected component labeling using a two-pass algorithm, labeling each component with a unique label.

    After labeling, it creates a dictionary that maps labels to random RGB colors.

    Finally, it generates a colored image where each component is colored according to the label-color mapping.

Author

    Habibullah Khan


