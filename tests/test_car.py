from src.car import Car
from unittest.mock import Mock, call
from unittest import TestCase, main


class TestCar_public_interface(TestCase):
    def setUp(self):
        self.temp = Car()
    def test_needsFuel(self):
        #prepare mock
        test_object = self.temp
        test_object.needsFuel = Mock(name = "needsFuel")
        test_object.needsFuel.return_value = False

        result = test_object.needsFuel()
        self.assertFalse(result, "incorrect")

    def test_getEngineTemperature(self):
        #prepare mock
        test_object = self.temp
        test_object.getEngineTemperature = Mock(name = "getEngineTemperature")
        test_object.getEngineTemperature.return_value = 60

        result = test_object.getEngineTemperature()
        self.assertEqual(60, result, "incorrect")

    def test_driveTo(self):
        #prepare mock
        test_object = self.temp
        test_object.driveTo = Mock(name = "driveTo")
        test_object.driveTo.return_value = "Warsaw"

        result = test_object.driveTo()
        self.assertEqual("Warsaw", result, "incorrect")

if __name__ == "main":
    main()