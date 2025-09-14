from PIL import Image
import numpy as np

def lego_mosaic(input_image_path, output_image_path, block_size=10):
    # Open the input image
    img = Image.open(input_image_path)

    # Resize image to create a blocky effect (downsampling)
    img = img.resize((img.size[0] // block_size, img.size[1] // block_size), Image.NEAREST)

    # Resize back to original size to simulate Lego blocks (upsampling)
    img = img.resize((img.size[0] * block_size, img.size[1] * block_size), Image.NEAREST)

    # Convert to numpy array (this is now an array with RGB values)
    img_array = np.array(img)

    # Create a palette of limited colors (you can customize this)
    palette = np.array([
        [255, 0, 0],    # Red
        [0, 255, 0],    # Green
        [0, 0, 255],    # Blue
        [255, 255, 0],  # Yellow
        [0, 255, 255],  # Cyan
        [255, 0, 255],  # Magenta

        [128, 128, 128],# Gray
        [0, 0, 0],      # Black
        [255, 255, 255], # White
        [176, 160, 111],  # Brick Yellow
        [30, 90, 168] , # Bright Blue
        [6, 157, 159],  # Bright Bluish Green
        [88, 171, 65], # Bright Green
        [214, 121, 35],  # Bright orange
        [211, 53, 157],  # Bright purple
        [55, 33, 0],  # Dark Brown
        [131, 67, 40], # skin color
        [68, 40, 29], # moustache
        [255, 213, 157],  # couleur sable
        [31, 26, 67],  # Dark blue
        [123, 149, 202],  # Blue sky
        [89, 70, 63],  # Maron
        [168, 94, 69],
        [42, 33, 29]


    ])

    # Ensure lego_img_array is initialized with the correct shape and data type (RGB image)
    lego_img_array = np.zeros((img_array.shape[0], img_array.shape[1], 3), dtype=np.uint8)

    # Loop through every pixel and assign the closest color from the palette
    for y in range(img_array.shape[0]):
        for x in range(img_array.shape[1]):
            # Get the current pixel's RGB values
            pixel = img_array[y, x]

            # Calculate Euclidean distance between this pixel and every color in the palette
            distances = np.linalg.norm(palette - pixel, axis=1)

            # Find the index of the closest color
            closest_color_idx = np.argmin(distances)

            # Assign the closest color (RGB tuple) to the corresponding position in lego_img_array
            lego_img_array[y, x] = palette[closest_color_idx]

    # Convert the resulting array back to an image
    lego_image = Image.fromarray(lego_img_array)

    # Save the output image
    lego_image.save(output_image_path)


# Example usage
input_path = 'IMG_0178 600x600 px.jpg'  # Path to your input image
output_path = 'lego_mosaic_output_Walid_2.jpg'  # Path for the output image
lego_mosaic(input_path, output_path, block_size=4)
