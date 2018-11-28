import logging
import os
import datetime

class loghelper(object):

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        self.log_in_file()

    def get_logger(self):
        return self.logger

    def getLog_path(self):
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[
                   :curPath.find("InterfaceAutoTest\\") + len("InterfaceAutoTest\\")]  # InterfaceAutoTest，也就是项目的根路径
        logpaths = os.path.abspath(rootPath + 'logs')  # 获取logs文件夹的路径
        return logpaths

    """以日期生成日志文件名称 """
    def log_file(self):
        log_name = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_path = self.getLog_path() + "/" + log_name
        return log_path

    def log_in_file(self):
        """ 日志输入到文件"""
        self.fileHandler = logging.FileHandler(self.log_file(), "a", encoding="utf-8")
        self.formatter = logging.Formatter('%(asctime)s----日志级别:%(levelname)s---行号: %(lineno)d ---函数名:%(funcName)s--日志内容: %(message)s ')
        self.fileHandler.setFormatter(self.formatter)
        self.logger.addHandler(self.fileHandler)

    def close_handler(self):
        """日志中流的关闭 """
        self.fileHandler.close()
        self.logger.removeHandler(self.fileHandler)


