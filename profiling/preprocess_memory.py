"""
Memory profiling (line by line) for the preprocessing step

See this for usage:

https://github.com/pythonprofilers/memory_profiler

Run with:

mprof run preprocess_memory.py PATH_TO_CONFIG_FILE

Plot results:

mprof plot
"""
import logging
from datetime import datetime
from memory_profiler import profile
from yass import preprocess
import settings


if __name__ == '__main__':
    """Profiling memory in YASS pipeline
    """
    settings.run()
    start = datetime.now()
    logger = logging.getLogger(__name__)

    logger.info('Preprocessing started at second: %.2f',
                (datetime.now() - start).total_seconds())

    # preprocessing
    (standarized_path, standarized_params, channel_index,
     whiten_filter) = profile(preprocess.run)(output_directory='profiling',
                                              if_file_exists='overwrite')

    logger.info('Preprocessing finished at second: %.2f',
                (datetime.now() - start).total_seconds())
