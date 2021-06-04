# coding=utf-8


class Singleton(object):
    """
    Singleton
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)  # python3
            # cls._instance = super(Singleton, cls).__new__(cls，*args, **kwargs)     # python2
        return cls._instance


class Logger(Singleton):
    """
    Log
    """

    def __init__(self, file_name):
        self.filename = file_name

    def _write_log(self, level, msg):
        with open(self.filename, "a") as log_file:
            log_file.write("[{0}]{1}\n".format(level, msg))

    def critical(self, msg):
        self._write_log("CRITICAL", msg)

    def error(self, msg):
        self._write_log("ERROR", msg)

    def warn(self, msg):
        self._write_log("WARN", msg)

    def info(self, msg):
        self._write_log("INFO", msg)

    def debug(self, msg):
        self._write_log("DEBUG", msg)


if __name__ == "__main__":
    log1 = Logger("logger1.log")
    log2 = Logger("logger2.log")
    print(id(log1), log1.filename)
    print(id(log2), log2.filename)
    log1.info("log1************")
    log1.warn("log1************")
    log2.info("log2************")
    log2.warn("log2************")
