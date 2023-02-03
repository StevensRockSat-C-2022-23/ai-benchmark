# -*- coding: utf-8 -*-
# Copyright 2019-2020 by Andrey Ignatov. All Rights Reserved.

from __future__ import print_function
from ai_benchmark.utils import *


class AIBenchmark:

    def __init__(self, use_CPU=None, verbose_level=1):

        self.tf_ver_2 = parse_version(tf.__version__) > parse_version('1.99')
        self.verbose = verbose_level

        if verbose_level > 0:
            printIntro()

        #np.warnings.filterwarnings('ignore') # NumPy seems to have discarded this method.

        try:

            if verbose_level < 3:

                os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

                if self.tf_ver_2:
                    import logging
                    logger = tf.get_logger()
                    logger.disabled = True
                    logger.setLevel(logging.ERROR)

                elif parse_version(tf.__version__) > parse_version('1.13'):
                    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

                else:
                    tf.logging.set_verbosity(tf.logging.ERROR)

            else:

                if self.tf_ver_2:
                    import logging
                    logger = tf.get_logger()
                    logger.disabled = True
                    logger.setLevel(logging.INFO)

                elif parse_version(tf.__version__) > parse_version('1.13'):
                    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)

                else:
                    tf.logging.set_verbosity(tf.logging.INFO)

        except:
            pass

        np.random.seed(42)
        self.cwd = path.dirname(__file__)

        self.use_CPU = False
        if use_CPU:
            self.use_CPU = True

    def run(self, precision="normal", batch_mul=1):
        return run_tests(training=True, inference=True, micro=False, nano=False, verbose=self.verbose,
                         use_CPU=self.use_CPU, precision=precision, _type="full", start_dir=self.cwd, batch_mul=batch_mul)

    def run_inference(self, precision="normal", batch_mul=1):
        return run_tests(training=False, inference=True, micro=False, nano=False, verbose=self.verbose,
                         use_CPU=self.use_CPU, precision=precision, _type="inference", start_dir=self.cwd, batch_mul=batch_mul)

    def run_training(self, precision="normal", batch_mul=1):
        return run_tests(training=True, inference=False, micro=False, nano=False, verbose=self.verbose,
                         use_CPU=self.use_CPU, precision=precision, _type="training", start_dir=self.cwd, batch_mul=batch_mul)

    def run_micro(self, precision="normal", batch_mul=1):
        return run_tests(training=False, inference=False, micro=True, nano=False, verbose=self.verbose,
                         use_CPU=self.use_CPU, precision=precision, _type="micro", start_dir=self.cwd, batch_mul=batch_mul)

    def run_nano(self, precision="normal", batch_mul=1):
        return run_tests(training=False, inference=False, micro=False, nano=True, verbose=self.verbose,
                         use_CPU=self.use_CPU, precision=precision, _type="nano", start_dir=self.cwd, batch_mul=batch_mul)


if __name__ == "__main__":

    benchmark = AIBenchmark(use_CPU=None, verbose_level=1)
    results = benchmark.run(precision="normal")
