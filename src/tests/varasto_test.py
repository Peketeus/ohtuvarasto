import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virhevarasto = Varasto(-10, -5) # väärillä arvoilla luotu varasto
        self.fullvarasto = Varasto(10, 11) # saldo suurempi kuin tilavuus

# omat testit ---------------------------------------------------------------------------------

    def test_konstruktori_luo_virheellisen_varaston_tilavuuden(self):
        self.assertAlmostEqual(self.virhevarasto.tilavuus, 0)

    def test_konstruktori_luo_virheellisen_varaston_saldon(self):
        self.assertAlmostEqual(self.virhevarasto.saldo, 0)

    def test_konstruktori_luo_liian_tayden_varaston(self):
        self.assertAlmostEqual(self.fullvarasto.saldo, 10)

    def test_lisays_lisaa_negatiivinen_saldo(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_varastoon_enemman(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_negatiivinen_arvo(self):
        self.fullvarasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.fullvarasto.saldo, 10)

    def test_ottaminen_saldoa_suurempi(self):
        self.fullvarasto.ota_varastosta(11)

        self.assertAlmostEqual(self.fullvarasto.saldo, 0)

    def test_paljonko_tilaa(self):
        self.assertEqual(str(self.fullvarasto), "saldo = 10, vielä tilaa 0")

# omien testien loppu -------------------------------------------------------------------------

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
