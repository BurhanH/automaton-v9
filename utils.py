import cv2
import numpy as np


def find_image_template(template_path,
                        target_template,
                        actual_image,
                        where_to_save,
                        threshold=0.8):

    """
    This function helps to find template image in image. Based on opencv library.
    Detailed info about how it works:
        https://docs.opencv.org/2.4/modules/imgproc/doc/object_detection.html
    :param template_path: Path to templates
    :param target_template: Target template name for search
    :param actual_image: Actual image where needs search
    :param where_to_save: Path to save results
    :param threshold: Some kind of sensitivity of search
    """

    path_to_actual_result = '{}/{}'.format(where_to_save, actual_image)
    path_to_template = '{}/{}'.format(template_path, target_template)

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
        cv2.imwrite('{}/{}'.format(where_to_save, '{}_result.png'.format(target_template[:-4])), img_rgb)
        passed = True

    return passed
