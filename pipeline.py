"""Data processing pipeline."""

import itertools
import logging
import luigi
import pandas as pd

import quicksilver.code.applications.qs_predict as pred


class FetchDataSet(luigi.Task):
    path = '/dataset/'

    def requires(self):
        pass

    def run(self):
        logging.error('dataset missing at %s' % self.path)

    def output(self):
        return luigi.LocalTarget(self.path)


class ComputeDistances(luigi.Task):
    def compute_distances(permutations):
        args = pred.args
        moving_images = ['../CUMC_examples/m1.nii']
        target_images = ['../CUMC_examples/21.nii']
        output_prefixes = ['/tmp/']
        test = pred.predict_image(
            args, moving_images, target_images, output_prefixes)

    def requires(self):
        return {'dataset': FetchDataSet()}

    def run(self):
        all_permutations = itertools.permutations(
            pd.read_csv(self.input()['dataset']), 2)
        self.compute_distances(all_permutations)

    def output(self):
        return luigi.LocalTarget(self.path)


class RunAll(luigi.Task):
    def requires(self):
        return ComputeDistances()

    def output(self):
        return luigi.LocalTarget('dummy')


def init():
    logging.basicConfig(level=logging.INFO)
    logging.info('start')
    luigi.run(
        main_task_cls=RunAll(),
        cmdline_args=[
            '--local-scheduler',
        ])


if __name__ == "__main__":
    init()
