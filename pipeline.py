"""Data processing pipeline."""

import itertools
import logging
import luigi
import os
import warnings
warnings.filterwarnings("ignore")  # NOQA

import pandas as pd

import qs_predict

HOME_DIR = '/scratch/users/nmiolane'
DATA_DIR = os.path.join(HOME_DIR, 'dataset')
OUTPUT_DIR = os.path.join(HOME_DIR, 'output')


class FetchDataSet(luigi.Task):
    path = os.path.join(DATA_DIR, 'participants.csv')

    def requires(self):
        pass

    def run(self):
        logging.error('dataset missing at %s' % self.path)

    def output(self):
        return luigi.LocalTarget(self.path)


class ComputeDistances(luigi.Task):
    path = os.path.join(OUTPUT_DIR)

    def compute_distances(self, permutations):
        args = qs_predict.args

        i = 0
        for moving, target in permutations:
            if i > 0:
                break
            moving_images = ['../CUMC_examples/m1.nii']
            target_images = ['../CUMC_examples/21.nii']
            output_prefixes = self.path

            test = qs_predict.predict_image(
                args, moving_images, target_images, output_prefixes)
            i += 1

    def requires(self):
        return {'dataset': FetchDataSet()}

    def run(self):
        csv_path = self.input()['dataset'].path
        all_permutations = itertools.permutations(
            pd.read_csv(csv_path), 2)
        self.compute_distances(all_permutations)

    def output(self):
        return luigi.LocalTarget(self.path)


class RunAll(luigi.Task):
    def requires(self):
        return ComputeDistances()

    def output(self):
        return luigi.LocalTarget('dummy')


def init():
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    logging.basicConfig(level=logging.INFO)
    logging.info('start')
    luigi.run(
        main_task_cls=RunAll(),
        cmdline_args=[
            '--local-scheduler',
        ])


if __name__ == "__main__":
    init()
