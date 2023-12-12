import unittest
from datetime import date, timedelta
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        battery = NubbinBattery(current_date=date.today(), last_service_date=date.today() - timedelta(days=365 * 4))
        result = battery.needs_service()
        self.assertTrue(result, f"NubbinBattery needs_service returned {result}. Last service date: {battery.last_service_date}, Current date: {battery.current_date}")

    if __name__ == '__main__':
        unittest.main()

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        battery = SpindlerBattery(current_date=date.today(), last_service_date=date.today() - timedelta(days=365*2))
        result = battery.needs_service()
        self.assertTrue(result, f"SpindlerBattery needs_service returned {result}")

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        result = engine.needs_service()
        self.assertTrue(result, f"CapuletEngine needs_service returned {result}")

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = SternmanEngine(warning_light_is_on=True)
        result = engine.needs_service()
        self.assertTrue(result, f"SternmanEngine needs_service returned {result}")

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        engine = WilloughbyEngine(current_mileage=60000, last_service_mileage=0)
        result = engine.needs_service()
        self.assertTrue(result, f"WilloughbyEngine needs_service returned {result}")

class TestCar(unittest.TestCase):
    def test_needs_service(self):
        engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
        battery = SpindlerBattery(current_date=date.today(), last_service_date=date.today())
        car = Car(engine, battery)
        result = car.needs_service()
        self.assertTrue(result, f"Car needs_service returned {result}")

if __name__ == '__main__':
    unittest.main()