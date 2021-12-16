from colorama import init, Fore, Style
# colorama 模块安装
# pip install colorama
# or
# pip3 install colorama

# 官方说明
# https://pypi.org/project/colorama/


init()  # 为了在 Windows 上正常工作，需要调用这行
LevelNameMap = {
    'DEBUG': 'D',
    'INFO': 'I',
    'WARNING': 'W',
    'ERROR': 'E',
    'EXCEPTION': 'E',
    'CRITICAL': 'C',
}


class Log(object):
    ColorFormat = {
        'D': Fore.WHITE + "%s" + Style.RESET_ALL,
        'I': Fore.GREEN + "%s" + Style.RESET_ALL,
        'W': Fore.YELLOW + "%s" + Style.RESET_ALL,
        'E': Fore.RED + "%s" + Style.RESET_ALL,
        'C': Fore.MAGENTA + "%s" + Style.RESET_ALL,
    }

    @classmethod
    def format(cls, level, text):
        return cls.ColorFormat[level] % text

    @classmethod
    def Debug(cls, text):
        print(cls.format('D', text))

    @classmethod
    def Info(cls, text):
        print(cls.format('I', text))

    @classmethod
    def Warn(cls, text):
        print(cls.format('W', text))

    @classmethod
    def Error(cls, text):
        print(cls.format('E', text))

    @classmethod
    def Critical(cls, text):
        print(cls.format('C', text))


if __name__ == '__main__':
    Log.Debug("这是一条调试信息")
    Log.Info("这是一条普通信息")
    Log.Warn("这是一条警告信息")
    Log.Error("这是一条错误信息")
    Log.Critical("这是一条紧急信息")