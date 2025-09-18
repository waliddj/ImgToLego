# ImgToLego
<img width="172" height="294" alt="small_lego" src="https://github.com/user-attachments/assets/8b242f9e-8534-41fc-b926-deef26690448" /> Image to Lego Mosaic Generator is a tool that converts your images into Lego mosaic designs.

## Features
Smart Color Quantization: Automatically reduces your image's color palette to the most common colors available in Lego bricks.

Multiple Brick Support: (Optional: if applicable) Can be configured to use standard 1x1 bricks, or a variety of larger brick sizes for different effects.

Customizable Resolution: Adjust the number of "studs" (pixels) to control the final size and level of detail in your mosaic.

## How It Works?

The first step of the algorithm is resize image to create a blocky effect.

Resize back to original size to simulate Lego blocks (upsampling)

<img width="809" height="812" alt="Frame 2" src="https://github.com/user-attachments/assets/53683393-409f-49f7-8958-2dc716ac7cd4" /> (an image representation if the upsampling and downsampling)


Convert the image into a NumPy array.

Create a palette of limited colors (Since Lego bricks have limited colors).

Initialize a zero matrix using NumPy (lego_img_array) with the correct shape and data type.

<img width="600" height="600" alt="Group 3" src="https://github.com/user-attachments/assets/eaf9ce27-773b-4334-9a4f-8e7d8db843bb" />  (an image representation of the zero matrix)

Go through each pixel block (i,j)  of the image, find the closest one from the predefined palette, Assign the closest color (RGB tuple) to the corresponding position in lego_img_array.

<img width="600" height="600" alt="Group 3_1" src="https://github.com/user-attachments/assets/efc3900a-e575-4432-bcd7-6aade051f235" />

<img width="597" height="557" alt="Group 4" src="https://github.com/user-attachments/assets/27354bb0-9d33-4002-8861-3174d8ec93a3" />


Convert the resulting array back to an image.

Save the output image.

Example:

Input image: ![IMG_0178 600x600 px](https://github.com/user-attachments/assets/14a2380a-2741-4260-9344-b842fbfc4744)

Output image: ![lego_mosaic_output_Walid](https://github.com/user-attachments/assets/7bd53da4-e512-4592-add2-d299b511aa44)


NOTE:

You can control the image resolution by modifying the size of the blocks.

