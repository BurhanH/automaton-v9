import cv2
import numpy as np


def find_image_template(
        template_path: str,
        target_template: str,
        actual_image: str,
        where_to_save: str,
        threshold: float = 0.8) -> bool:

    """ This function helps to find template image in image. Based on opencv library.
        Detailed info about how it works:
        https://docs.opencv.org/2.4/modules/imgproc/doc/object_detection.html

    Args:
        template_path (str): Path to templates
        target_template (str): Target template name for search
        actual_image (str): Actual image where needs search
        where_to_save (str): Path to save results
        threshold (float): Some kind of sensitivity of search

    Returns:
        bool: True or False
    """

    path_to_actual_result = f'{where_to_save}/{actual_image}'
    path_to_template = f'{template_path}/{target_template}'

    # Finds all templates if it applicable
    # load the actual result and template images
    img_rgb = cv2.imread(path_to_actual_result)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(path_to_template, 0)
    w, h = template.shape[::-1]

    # find the template in the actual result
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    # print("Method 2:\n {}\n".format(res))  # <-- debugging line

    loc = np.where(res >= threshold)
    # print(zip(*loc[::-1]))  # <-- debugging line

    passed = False

    for pt in zip(*loc[::-1]):
        # Make a border for each found template
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
        # save result into file
        cv2.imwrite(f'{where_to_save}/{target_template[:-4]}_result.png', img_rgb)
        passed = True

    return passed
