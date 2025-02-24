from datetime import datetime
import pytz

class MyGreeter:
    """
    一个根据当前时间返回不同问候语的类
    """
    
    def __init__(self):
        """
        初始化MyGreeter实例
        """
        pass

    def greeting(self, user_timezone: str = 'Asia/Shanghai') -> str:
        """
        Args:
            user_timezone: 用户所在时区，可以从请求头或参数获取
        """
        user_tz = pytz.timezone(user_timezone)
        user_time = datetime.now(pytz.UTC).astimezone(user_tz)
        hour = user_time.hour
        
        if 6 <= hour < 12:
            return "Good morning"
        elif 12 <= hour < 18:
            return "Good afternoon"
        else:
            return "Good evening" 