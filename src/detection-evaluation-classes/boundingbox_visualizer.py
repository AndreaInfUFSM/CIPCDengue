import cv2
import numpy as np
from numpy.typing import NDArray
#from PIL import Image
from IPython.display import display
from IPython import get_ipython


class BoundingBoxVisualizer():

    def __init__(self, unique_labels):
        self.map_color_fn = self.__map_ids_to_colors(unique_labels)

    def show_bboxes(self, image: NDArray, yx_boxes_list, labels_list):
        plot = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        for i, box in enumerate(yx_boxes_list):
            x1, y1, x2, y2 = box
            # y1, x1, y2, x2 = box
            color = self.map_color_fn(labels_list[i])
            cv2.rectangle(plot, (x1, y1), (x2, y2), color, 2)


        if 'ipykernel' in str(type(get_ipython())):
            # Running in a Jupyter notebook
            from IPython.display import display
            from PIL import Image as PILImage
            display(PILImage.fromarray(plot))
        else:
            # Running as a .py script
            from PIL import Image as PILImage
            image = PILImage.fromarray(plot)
            image.show()

        #display(Image.fromarray(plot))


    def __generate_contrasting_colors(self, n):
        colors = [(0, 255, 0)]  # First color is always green

        # if n == 1:
        #     return colors  # If only one color is needed, return just green

        # Predefined vibrant colors for small numbers of colors
        vibrant_colors = [        
            (0, 0, 255),   # Blue
            (255, 255, 0), # Yellow
            (255, 0, 255), # Magenta
            (0, 255, 255), # Cyan
        ]

        # For small n, return predefined vibrant colors along with green
        if n == 2:
            return colors + [vibrant_colors[0]]
        elif n <= len(vibrant_colors) + 1:
            return colors + vibrant_colors[:n-1]

        # Calculate the step size based on the number of remaining colors
        step = 255 // ((n - 1) // 3 + 1)

        # Generate the rest of the colors
        for i in range(1, n):
            r = (i * step) % 256
            g = (i * step * 2) % 256
            b = (i * step * 3) % 256
            colors.append((r, g, b))
        
        return colors


    def __map_ids_to_colors(self, ids):

        colors = self.__generate_contrasting_colors(len(ids))

        # Create a dictionary to map each ID to a color
        id_to_color_map = {id: colors[i % len(colors)] for i, id in enumerate(ids)}

        # Return a function that looks up the color by ID
        def get_color_by_id(id):
            return id_to_color_map.get(id, (0, 0, 0))  # Return a default color if ID not found

        return get_color_by_id