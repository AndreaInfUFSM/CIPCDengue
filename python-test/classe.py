import json

class ImageInfo:
    def __init__(self, name, coordinates_pair, count, template_name):
        self.name = name
        self.coordinates_pair = coordinates_pair
        self.count = count
        self.template_name = template_name

    def __str__(self):
        return "name: " + self.name + "\nwidth: " + str(self.coordinates_pair) + "\nchannels: " + str(self.count) + "\ntemplate_name: " + self.template_name

    def __repr__(self):
        return "name: " + self.name + "\nwidth: " + str(self.coordinates_pair) + "\nchannels: " + str(self.count) + "\ntemplate_name: " + self.template_name

    def to_json(self):
        if isinstance(self, ImageInfo):
            return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        else:
            return None

def export_data(img, cont, template_name, img_rgb, coordinates):
    image_info = ImageInfo(img, coordinates, cont, template_name)
    json_str = image_info.to_json()
    if json_str is not None:
        json_file_name = "./results/data/"+img_rgb.split('.')[0]+f"-{cont}.json"
        with open(json_file_name, "w") as json_file:
            json_file.write(json_str)
