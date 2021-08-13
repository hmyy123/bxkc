import unittest
from appium import webdriver


class base(unittest.TestCase):
    def setUp(self):
        self.d = {}
        self.d["platformName"] = "Android"
        self.d["platformNameVersion"] = "9.0"
        # self.d["deviceName"] = "RMSNW18C28004552"
        self.d["deviceName"] = "127.0.0.1:7555"
        self.d["appPackage"] = "com.bxkc.android"
        self.d["appActivity"] = "com.bxkc.android.activity.WelcomeActivity"
        self.d["noReset"] = False
        # self.d["skipServerInstallation"] = True
        # self.d["skipDeviceInitialization"] = True
        self.driver = webdriver.Remote(r"http://127.0.0.1:4723/wd/hub", self.d)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
