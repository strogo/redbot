#!/usr/bin/env python
# coding=UTF-8

import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import unittest


class BasicWebUiTest(unittest.TestCase):
    test_uri = "http://www.mnot.net/"
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(redbot_uri)
        self.uri = self.browser.find_element_by_id("uri")
        self.uri.send_keys(self.test_uri + Keys.RETURN)
        time.sleep(1.0)
        self.check_complete()
        
    def test_multi(self):
        check = self.browser.find_element_by_xpath("//a[@accesskey='a']")
        check.click()
        time.sleep(0.5)
    
    def check_complete(self):
        try:
            self.browser.find_element_by_xpath("//div[@class='footer']")
        except NoSuchElementException:
            raise Exception, "Page not complete."
    
    def tearDown(self):
        self.check_complete()
        self.browser.close()

class CnnWebUiTest(BasicWebUiTest):
    test_uri = 'http://edition.cnn.com/'


if __name__ == "__main__":
    redbot_uri = os.environ.get("REDBOT_URI", None)
    if redbot_uri:
      unittest.main()
    else:
      test_host = "localhost"
      test_port = 8080
      redbot_uri = "http://%s:%s/" % (test_host, test_port)
      import sys
      sys.path.insert(0, "deploy")
      def redbot_run():
        import webui
        webui.standalone_main(test_host, test_port, "deploy/static")
      from multiprocessing import Process
      p = Process(target=redbot_run)
      p.start()
      unittest.main(exit=False, verbosity=2)
      print "done test..."
      p.terminate()
    
