import os
import logging


def param_decor(parameter):
    if not os.path.isdir(parameter):
        os.mkdir(parameter)

    def log_decorator(hw_function):
        def log_function(*args, **kwargs):
            hw_func_name = hw_function.__name__
            log_func_name = log_function.__name__
            logger = logging.getLogger(log_func_name)
            logger.setLevel(logging.DEBUG)
            logger.info(f'---------------- RECORD START ----------------')

            fh = logging.FileHandler(f'{parameter}/param_decor.log')
            fh_formatter = logging.Formatter(
                '%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s',
                datefmt = '%d/%m/%Y %H:%M:%S '
            )
            fh.setFormatter(fh_formatter)
            logger.addHandler(fh)

            logger.info(f'Вызов функции {hw_func_name}.')

            try:
                result = hw_function(*args, **kwargs)
                logger.info(f'Параметры функции {hw_func_name}: {args}, {kwargs}')
                logger.info(f'Результат функции {hw_func_name}: {result}')
                logger.info(f'Путь к логу {fh.baseFilename}')

            except OSError:
                logger.error('----------------------------------------------')
                logger.error(f'Ошибка в логируемой функции {hw_func_name}')
                logger.error('----------------------------------------------')

            logger.info(f'---------------- RECORD STOP -----------------')

            return result

        return log_function

    return log_decorator
