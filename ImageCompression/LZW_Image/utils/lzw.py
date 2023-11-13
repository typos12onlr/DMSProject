import numpy as np

def lzw_encoder(
    img: np.ndarray[np.uint8], block_size: int, max_dict_size: int
) -> tuple[list[list[int]], int]:
    """
    Encodes a grayscale image using LZW compression

    Parameters:
        img (grayscale image): np.ndarray[np.uint8]
        block_size (size of the blocks): int
        max_dict_size (maximum dictionary size): int

    Returns:
        encoded_img (list of LZW encoded blocks): list[list[int]]
        max_dict_filled (maximum dictionary code used): int
    """
    height, width = img.shape

    if block_size < 1 or block_size > min(height, width):
        block_size = min(height, width)

    # Perform zero padding to make the image dimensions divisible by the block size
    padded_height = height + (block_size - height % block_size) % block_size
    padded_width = width + (block_size - width % block_size) % block_size
    padded_img = np.zeros((padded_height, padded_width), dtype=np.uint8)
    padded_img[:height, :width] = img

    # Split the image into blocks
    blocks = [
        padded_img[i : i + block_size, j : j + block_size]
        for i in range(0, padded_height, block_size)
        for j in range(0, padded_width, block_size)
    ]

    # Initialize variables for the output
    encoded_img = []
    max_dict_filled = 255

    # Iterate over all blocks and apply LZW compression
    for block in blocks:
        # Initialize variables for the current block
        # Code dictionary to store the codes for the recognized patterns in the current block
        code_dict = dict((chr(i), i) for i in range(256))

        # List to store the encoded output for the current block
        encoded_block = []

        # String to store the currently recognized pattern
        currently_recognized = ""

        # Variable to store the encoded output for the currently recognized pattern
        encoded_output = None

        # Iterate over all pixels in the block
        for pixel in block.flatten():
            # Add the pixel to the currently recognized pattern
            currently_recognized += chr(pixel)

            if currently_recognized in code_dict:
                # If the currently recognized pattern is in the code dictionary, store the encoded output for the currently recognized pattern
                encoded_output = code_dict[currently_recognized]
            else:
                # If the currently recognized pattern is not in the code dictionary, store the encoded output for the previously recognized pattern
                encoded_block.append(encoded_output)
                if len(code_dict) < max_dict_size:
                    # Add the currently recognized pattern to the code dictionary
                    code_dict[currently_recognized] = len(code_dict)
                    max_dict_filled = max(max_dict_filled, len(code_dict) - 1)

                # Reset the currently recognized pattern
                currently_recognized = chr(pixel)
                encoded_output = code_dict[currently_recognized]

        # Store the encoded output for the last recognized pattern
        if currently_recognized in code_dict:
            encoded_output = code_dict[currently_recognized]

        encoded_block.append(encoded_output)

        # Add the encoded block to the encoded image
        encoded_img.append(encoded_block)

    return encoded_img, max_dict_filled

def lzw_decoder(
    encoded_img: list[list[int]],
    height: int,
    width: int,
    block_size: int,
    max_dict_size: int,
) -> np.ndarray[np.uint8]:
    """
    Decodes a grayscale image using LZW compression

    Parameters:
        encoded_img (list of LZW encoded blocks): list[np.ndarray[np.int32]]
        height (height of the image): int
        width (width of the image): int
        block_size (size of the blocks): int
        max_dict_size (maximum dictionary size): int

    Returns:
        decoded_img (decoded image): np.ndarray[np.uint8]
    """
    if block_size < 1 or block_size > min(height, width):
        block_size = min(height, width)

    # Calculate the padded height and width of the image
    padded_height = height + (block_size - height % block_size) % block_size
    padded_width = width + (block_size - width % block_size) % block_size

    # Create a numpy array to store the decoded image
    decoded_img = np.zeros((padded_height, padded_width), dtype=np.uint8)

    # Initialize a counter to keep track of the current block being processed
    counter = 0

    # Iterate over all blocks in the encoded image
    for i in range(0, padded_height, block_size):
        for j in range(0, padded_width, block_size):
            # Initialize variables for the current block
            # List to store the decoded output for the current block
            decoded_block = []

            # List to store the decoded output for the previous code
            decoded = []

            # Dictionary to store the code dictionary for the current block
            code_dict = dict((i, [i]) for i in range(256))

            # Iterate over all codes in the current block
            for code in encoded_img[counter]:
                # If the code is not in the code dictionary, add it
                if code not in code_dict:
                    code_dict[code] = decoded + [decoded[0]]

                # Add the decoded output for the current code to the decoded block
                decoded_block += code_dict[code]

                # If the dictionary is not full and the decoded output for the previous code + the first output for the current code is not in the code dictionary, add it
                if (
                    0 < len(code_dict) < max_dict_size
                    and decoded + [code_dict[code][0]] not in code_dict.values()
                ):
                    code_dict[len(code_dict)] = decoded + [code_dict[code][0]]

                # Update the decoded output for the previous code
                decoded = code_dict[code]

            # Reshape the decoded block and store it in the decoded image
            decoded_img[i : i + block_size, j : j + block_size] = np.array(
                decoded_block, dtype=np.uint8
            ).reshape(block_size, block_size)

            # Increment the counter to move on to the next block
            counter += 1

    # Return the decoded image with the correct height and width
    return decoded_img[:height, :width]

