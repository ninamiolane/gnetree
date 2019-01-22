"""Data processing pipeline."""

import itertools
import logging
import luigi
import pandas as pd


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
        # TODO(johmathe): call quicksilver.
        pass

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
