import unittest
from selenium import webdriver

from utils import find_image_template


WAIT_IMPL = 10
WINDOW_SIZE = 1280, 1024
BROWSER = 'firefox'
WORK_FOLDER = ''  # Put path to folder with templates


class TestBrowserVisual(unittest.TestCase):
    """
    This test suite for visual testing.
    """

    def setUp(self):
        """
        Initiate driver for each test
        """
        if BROWSER == 'chrome':
            self.driver = webdriver.Chrome()
        if BROWSER == 'firefox':
            self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(WAIT_IMPL)
        self.driver.set_window_size(WINDOW_SIZE[0], WINDOW_SIZE[1])

    def _check_templates(self, url, name, templates, positive=True):
        """
        Common method for checking templates on a page.
        :param url: target url
        :param name: name of page
        :param templates: list of templates
        :param positive: what kind of verification (mostly using for negative test)
        """
        template_errors = []

        self.driver.get(url)
        self.driver.get_screenshot_as_file('{0}/{1}'.format(WORK_FOLDER, name))

        template_path = WORK_FOLDER
        where_to_save_result_path = WORK_FOLDER

        for template in templates:
            if not find_image_template(
                    template_path,
                    template,
                    name,
                    where_to_save_result_path):
                template_errors.append('Unable to find {} image on {} page'.format(template[:-4], name[:-9]))

        template_error_messages = '\n'.join(template_errors)

        if positive:
            self.assertFalse(template_error_messages, template_error_messages)
        else:
            self.assertTrue(template_error_messages, template_error_messages)

    def test_google_page(self):
        """
        Checking google home page
        """
        self._check_templates(
            url='https://www.google.com',
            name='home_page.png',
            templates=[
                'google_template.png',
                'search_template.png',
                'buttons_template.png'
            ]
        )

    def test_google_page_negative(self):
        """
        Checking google home page negative
        """
        self._check_templates(
            url='https://www.google.com',
            name='home_page.png',
            templates=['bad_template.png'],
            positive=False
        )

    def tearDown(self):
        """
        Closing driver after each test
        """
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
