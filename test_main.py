import cProfile
import pstats
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

    def test_draw_plots_performance(self):
        profile = cProfile.Profile()
        profile.enable()

        # Run the method or code you want to profile
        self.plot_drawer.draw_plots()

        profile.disable()

        profile_stats_file = 'profile_stats.txt'

        # Open the file in write mode and save the profiling stats
        with open(profile_stats_file, 'w') as f:
            stats = pstats.Stats(profile, stream=f)
            stats.print_stats()


if __name__ == '__main__':
    unittest.main()
