import json

class ImageInfo:
    def __init__(self, name, x_pos, y_pos, count, template_name):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.count = count
        self.template_name = template_name

    def __str__(self):
        return "name: " + self.name + "\nwidth: " + str(self.x_pos) + "\nheight: " + str(self.y_pos) + "\nchannels: " + str(self.count) + "\ntemplate_name: " + self.template_name

    def __repr__(self):
        return "name: " + self.name + "\nwidth: " + str(self.x_pos) + "\nheight: " + str(self.y_pos) + "\nchannels: " + str(self.count) + "\ntemplate_name: " + self.template_name

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def export_data(img, cont, template_name):
    image_info = ImageInfo(img,25,30,cont, template_name)
    json_str = image_info.to_json()
    json_file_name = "image_info.json"
    with open(json_file_name, "w") as json_file:
        json_file.write(json_str)
