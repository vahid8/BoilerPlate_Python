import json
import os
import tqdm



if __name__ == '__main__':

    input_dir = "/media/vahid/Elements/Data/segmentation_training/seg_test"
    output_dir = "/media/vahid/Elements/Data/segmentation_training/seg_test2"

    # Add legal keywords to check typos
    legal_keywords = ["asphalt" , "unsealed", "pavement"]
    illegal_keyword = []
    # Get json files
    json_files = [item for item in os.listdir(input_dir) if item.endswith(".json")]
    # json_files = [json_files[0]]
    for item in tqdm.tqdm(json_files):
        with open(os.path.join(input_dir,item)) as json_file:
            data = json.load(json_file)
            # Check the labels for each shape and correct it
            for sh in data['shapes']:
                if sh['label'] == 'Asphalt' or sh['label'] == 'Street' or sh['label'] =='street':
                    sh['label'] = 'asphalt'
                if sh['label'] == 'Unsold':
                    sh['label'] = 'Unsealed'
                # Check for typos
                if sh['label'] not in legal_keywords:
                    illegal_keyword.append(sh['label'])

        # Save it to a new file
        with open(os.path.join(output_dir, item),"w") as outfile:
            json.dump(data, outfile)

        if len(illegal_keyword) > 0:
            print(f" there are some illegal keywords in your labels{illegal_keyword}")
