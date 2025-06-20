import cv2
import numpy as np
import json
import os
import argparse
from itertools import batched


def main():
    parser = argparse.ArgumentParser(description='Produce different depictions of a double pendulum')
    parser.add_argument('template_filename', help='name of the template file to use')
    parser.add_argument('output_filename', help='name of the output file to use')
    # parser.add_argument('template_filename', help='name of config file')
    parser.add_argument('-i', '--input-list', nargs='+', default=[], help='list of images to be added to display')
    args = parser.parse_args()

    # print(args.template_filename)
    # print(args.input_list)

    # read in all corner positions for where the image will overlay on the template
    with open('template_positions.json') as f:
        pos_data = json.load(f)

    # template_file = 'templates/square_floor.jpg'
    # read in the input arguments
    template_file = args.template_filename
    template = cv2.imread(template_file)
    # image_filename = args.input_list[0]
    # image = cv2.imread(image_filename)
    positions = []

    # get the correct positions based on the input template file
    for template_data in pos_data:
        if template_data['filename'] == template_file:
            positions = template_data['positions']
            break

    # determine the number of inlay locations and create temp filenames
    # for that same number so they can be read and updated without over writing
    n_photos = len(positions)//2
    temp_file_names = [f'temp_{i}.png' for i in range(n_photos)]

    # loop over the positions in batchs of two since the data is stored with the
    # even indices (starting with 0) being the corners and odd indices matching 
    # with the previous index being the inverted corner
    for p1, p2 in batched(range(len(positions)), n=2):
        pos1 = positions[p1]
        pos2 = positions[p2]

        file_idx = p1//2
        output_file = temp_file_names[file_idx]
        image_filename = args.input_list[file_idx]
        image = cv2.imread(image_filename)

        if p2 > 1:
            input_file = temp_file_names[file_idx-1]
            template = cv2.imread(input_file)

        height, width = template.shape[:2]
        h1,w1 = image.shape[:2]

        pts1=np.float32([[0,0],[w1,0],[0,h1],[w1,h1]])
        pts2=np.float32(pos1)

        h, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC,5.0)

        height, width, channels = template.shape
        im1Reg = cv2.warpPerspective(image, h, (width, height))

        mask2 = np.zeros(template.shape, dtype=np.uint8)
        roi_corners2 = np.int32(pos2)
        channel_count2 = template.shape[2]  
        ignore_mask_color2 = (255,)*channel_count2

        cv2.fillConvexPoly(mask2, roi_corners2, ignore_mask_color2)

        mask2 = cv2.bitwise_not(mask2)
        masked_image2 = cv2.bitwise_and(template, mask2)

        # Using Bitwise or to merge the two images
        final = cv2.bitwise_or(im1Reg, masked_image2)
        cv2.imwrite(output_file,final)


    input_file = temp_file_names[-1]
    template = cv2.imread(input_file)
    cv2.imwrite(args.output_filename,final)

    for temp_file in temp_file_names:
        os.remove(temp_file)


if __name__ == '__main__':
    main()