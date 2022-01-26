
import logging


def log_decorator(hw_function):
    def log_function(*args, **kwargs):

        name = log_decorator.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(f'{name}.log')
        fh_formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s.%(funcName)s: %(message)s',
            datefmt = '%d/%m/%Y %H:%M:%S ')
        fh.setFormatter(fh_formatter)
        logger.addHandler(fh)

        logger.info(f'---------------- RECORD START ----------------')
        logger.info(f'Вызов функции {hw_function.__name__}.')
        try:
            result = hw_function(*args, **kwargs)
            logger.info(f'Параметры функции {hw_function.__name__}: {args}, {kwargs}')
            logger.info(f'Результат функции {hw_function.__name__}: {result}')
            logger.info(f'Путь к логу {fh.baseFilename}')
            logger.info(f'---------------- RECORD STOP -----------------')
        except OSError:
            logger.error('----------------------------------------------')
            logger.error(f'Ошибка в логируемой функции {hw_function.__name__}')
            logger.error('----------------------------------------------')
        return hw_function

    return log_function
