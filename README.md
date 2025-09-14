![IMG_0178 600x600 px](https://github.com/user-attachments/assets/a4db83a8-9b05-432e-b24a-33a2e0bedefc)# ImgToLego
🧱 Image to Lego Mosaic Generator
A tool that converts your images into Lego mosaic designs.

✨ Features
Smart Color Quantization: Automatically reduces your image's color palette to the most common colors available in Lego bricks.

Multiple Brick Support: (Optional: if applicable) Can be configured to use standard 1x1 bricks, or a variety of larger brick sizes for different effects.

Customizable Resolution: Adjust the number of "studs" (pixels) to control the final size and level of detail in your mosaic.

🚀 How It Works


Processing: The algorithm:

The first step of the algorithm is resize image to create a blocky effect.

Resize back to original size to simulate Lego blocks (upsampling)

Convert the image into a NumPy array.

Create a palette of limited colors (Since Lego bricks have limited colors).

Initialize an zero matrix using NumPy (lego_img_array) with the correct shape and data type.

Go through each pixel block (i,j)  of the image, find the closest one from the predefined palette, Assign the closest color (RGB tuple) to the corresponding position in lego_img_array.

Convert the resulting array back to an image.

Save the output image.

Input: You provide an image file (e.g., JPG, PNG).
Output: a Lego-like image.

Example:
Input image: ![IMG_0178 600x600 px](https://github.com/user-attachments/assets/14a2380a-2741-4260-9344-b842fbfc4744)

Output image: ![lego_mosaic_output_Walid](https://github.com/user-attachments/assets/7bd53da4-e512-4592-add2-d299b511aa44)

