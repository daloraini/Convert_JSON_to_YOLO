#convert_JSON_to_YOLO

import json
import os


json_folder_path = 'path to JSON Folder'
yolo_folder_path = 'path to YOLO Folder'


def convert_to_yolo_format(data):
    yolo_labels = []
    img_width, img_height = data['width'],data['height']

    for item in data['step_1']['result']:
        x, y, width, height = item['x'], item['y'], item['width'], item['height']
        
        # Convert coordinates to YOLO format
        x_center = x + width / 2
        y_center = y + height / 2
        x_yolo = x_center / img_width
        y_yolo = y_center / img_height
        width_yolo = width / img_width
        height_yolo = height / img_height

        yolo_labels.append(f"0 {x_yolo:.6f} {y_yolo:.6f} {width_yolo:.6f} {height_yolo:.6f}")

    return yolo_labels

for filename in os.listdir(json_folder_path):
    if filename.endswith(".json"):
        input_path = os.path.join(json_folder_path, filename)
        output_path = os.path.join(yolo_folder_path, filename.replace(".json", ".txt"))
        
        with open(input_path, 'r') as json_file:
            data = json.load(json_file)

        yolo_labels = convert_to_yolo_format(data)

        with open(output_path, 'w') as yolo_file:
            yolo_file.write('\n'.join(yolo_labels))

        print(f"Conversion complete for {filename}. YOLO labels saved to {output_path}")
        





