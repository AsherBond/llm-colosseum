import numpy as np

KEN_RED = [248, 0, 0]
KEN_GREEN = [48, 88, 152]


def detect_position_from_color(
    observation: dict, color: list, epsilon=1, save_frame: bool = True
) -> tuple:
    """
    Convert the observation from pixels to player coordinates.

    It works by finding the first pixel that matches the color.

    Returns a tuple of (x, y) coordinates.
    """
    frame = observation["frame"]
    # the screen is a np.array of RGB colors (3 channels)
    # Select the frames where the characters play: between 80 vertical and 200 vertical

    # dump the observation to a file

    if save_frame:
        np.save("observation.npy", frame)

    frame = frame[80:200, :]

    # Detect the red color of Ken
    # !!! THIS DOESNT WORK BECAUSE THE COLOR ISNT RIGHT!!

    diff = np.linalg.Norm(np.array(frame) - np.array(color), axis=2)
    print("diff", diff)
    mask = diff < epsilon

    # Return the index where the red color is detected
    coordinates = mask.any(axis=2).nonzero()
    print("coordinates", coordinates)

    if len(coordinates[0]) == 0:
        return None

    first_match = coordinates[0][0], coordinates[1][0]

    # Add back the vertical offset
    first_match = (first_match[0], first_match[1] + 80)

    return first_match