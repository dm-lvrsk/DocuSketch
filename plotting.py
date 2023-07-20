import matplotlib.pyplot as plt
import pandas as pd
import os


class Plotter:
    def __init__(self):
        self.plot_dir = "plots"
        if not os.path.exists(self.plot_dir):
            os.makedirs(self.plot_dir)

    def draw_plots(self, json_file):
        df = pd.read_json(json_file)


        plot_paths = []

        plt.plot(df['gt_corners'], df['rb_corners'])
        plt.xlabel('gt_corners')
        plt.ylabel('rb_corners')
        plt.title('Dependency of gt_corners and rb_corners')
        plot_path = os.path.join(self.plot_dir, 'Dependency of gt_corners and rb_corners.png')
        plt.savefig(plot_path)
        plt.clf()
        plot_paths.append(plot_path)

        plt.plot(df['floor_max'], df['floor_mean'])
        plt.xlabel('floor_max')
        plt.ylabel('floor_mean')
        plt.title('Dependency of gt_corners and rb_corners')
        plot_path = os.path.join(self.plot_dir, 'Dependency of floor_max and floor_mean.png')
        plt.savefig(plot_path)
        plt.clf()
        plot_paths.append(plot_path)

        for column in df.columns:
            plot_path = os.path.join(self.plot_dir, f"{column}.png")
            plt.plot(df[column])
            plt.savefig(plot_path)
            plt.clf()
            plot_paths.append(plot_path)

        return plot_paths
