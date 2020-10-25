from unittest import TestCase
from app.geomath import distance_in_km
from app.locations import london, dublin


class TestGeoMath(TestCase):
    def test_distance_london_dublin(self):
        distance = distance_in_km(london, dublin)
        self.assertAlmostEqual(distance, 463, 0)

    def test_commutative(self):
        self.assertEqual(distance_in_km(london, dublin), distance_in_km(dublin, london))
