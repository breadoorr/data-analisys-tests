import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json


class PlotDrawer:
    def __init__(self, json_file):
        self.json_file = json_file
        self.df = self.load_data()

    def load_data(self):
        try:
            with open(self.json_file, 'r') as f:
                data = json.load(f)
            print("JSON data loaded successfully.")
            df = pd.DataFrame(data)
            print(df.columns)
            print("DataFrame created successfully.")
            return df
        except Exception as e:
            print(f"Error loading JSON file: {e}")
            return None

    def draw_plots(self):
        if not os.path.exists('plots'):
            os.makedirs('plots')

        plots = []
        columns = self.df.columns
        for column in columns:
            if column not in ['room_name', 'gt_corners', 'rb_corners']:
                plt.figure(figsize=(10, 6))
                sns.histplot(self.df[column], kde=True)
                plt.title(f'Distribution of {column}')
                plot_path = os.path.join('plots', f'{column}_distribution.png')
                plt.savefig(plot_path)
                plots.append(plot_path)
                plt.close()

            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=self.df, x='gt_corners', y='rb_corners', hue=column, palette='viridis')
            plt.title(f'Ground Truth vs Predicted Corners ({column})')
            plot_path = os.path.join('plots', f'gt_vs_rb_{column}.png')
            plt.savefig(plot_path)
            plots.append(plot_path)
            plt.close()

        return plots


if __name__ == '__main__':
    plot_drawer = PlotDrawer('deviation.json')
    plot_paths = plot_drawer.draw_plots()
    print(f'Plots saved at: {plot_paths}')
