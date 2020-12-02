from src.checker import Checker
from unittest.mock import Mock, patch
from unittest import TestCase, main


class TestCheckerPatch(TestCase):
    def setUp(self):
        self.temp = Checker()

    def test_checker_remainder_before_17(self):
        test_object = self.temp
        test_object.env.getTime = Mock(name = "getTime")
        test_object.env.getTime.return_value = 16
        file_name = "vlog1.wav"
        test_object.env.resetWav = Mock(name = "resetWav")
        test_object.env.resetWav.return_value = False

        result = test_object.remainder(file_name)
        self.assertFalse(result, "incorrect value")

    def test_checker_remainder_after_17(self):
        test_object = self.temp
        test_object.env.getTime = Mock(name = "getTime")
        test_object.env.getTime.return_value = 18
        file_name = "vlog1.wav"
        test_object.env.wasWavPlayed = Mock(name = "wasWavPlayed")
        test_object.env.wasWavPlayed.return_value = True

        result = test_object.remainder(file_name)
        self.assertTrue(result, "incorrect value")

    def tearDown(self):
        self.temp = None

