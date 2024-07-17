import unittest
import pandas as pd
from main import PlotDrawer


class TestPlotDrawer(unittest.TestCase):
    def setUp(self):
        self.plot_drawer = PlotDrawer('deviation.json')

    def test_load_data(self):
        self.assertIsInstance(self.plot_drawer.df, pd.DataFrame)

    def test_draw_plots(self):
        plots = self.plot_drawer.draw_plots()
        self.assertGreater(len(plots), 0)


if __name__ == '__main__':
    unittest.main()
