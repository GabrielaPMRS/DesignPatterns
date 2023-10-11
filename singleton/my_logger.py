import logging

class MyLogger:
    _logger = None

    def __new__(cls):
        if cls._logger is None:

            print("Logger new")
            cls._logger = logging.getLogger("logger_name")

            # Setar o nível mais baixo do logger (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            cls._logger.setLevel(logging.DEBUG)
            
            formatter = logging.Formatter(
                '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

            streamHandler = logging.StreamHandler()

            streamHandler.setFormatter(formatter)

            cls._logger.addHandler(streamHandler)

        return cls._logger

if __name__ == "__main__":
    logger1 = MyLogger()
    print(logger1)
    logger1.info("Hello, Logger")
    logger2 = MyLogger()
    print(logger2)
    logger2.warning("bug occured")