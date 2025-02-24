import unittest
from src.my_greeter import MyGreeter
from unittest.mock import patch
from datetime import datetime
import pytz

class TestMyGreeter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """测试类初始化时创建MyGreeter实例"""
        cls._my_greeter = MyGreeter()

    def test_init(self):
        """测试MyGreeter类是否可以正确实例化"""
        self.assertIsInstance(self._my_greeter, MyGreeter)

    def test_greeting_returns_non_empty_string(self):
        """测试greeting方法是否返回非空字符串"""
        self.assertTrue(len(self._my_greeter.greeting()) > 0)

    @patch('src.my_greeter.datetime')
    def test_morning_boundary_cases(self, mock_datetime):
        """测试早上时段的边界情况（上海时区）"""
        # 早上6:00
        mock_datetime.now.return_value = datetime(2024, 1, 1, 6, 0, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good morning")
        
        # 早上6:01
        mock_datetime.now.return_value = datetime(2024, 1, 1, 6, 1, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good morning")
        
        # 中午11:59
        mock_datetime.now.return_value = datetime(2024, 1, 1, 11, 59, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good morning")

    @patch('src.my_greeter.datetime')
    def test_afternoon_boundary_cases(self, mock_datetime):
        """测试下午时段的边界情况（上海时区）"""
        # 中午12:00
        mock_datetime.now.return_value = datetime(2024, 1, 1, 12, 0, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good afternoon")
        
        # 下午5:59
        mock_datetime.now.return_value = datetime(2024, 1, 1, 17, 59, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good afternoon")

    @patch('src.my_greeter.datetime')
    def test_evening_boundary_cases(self, mock_datetime):
        """测试晚上时段的边界情况（上海时区）"""
        # 晚上6:00
        mock_datetime.now.return_value = datetime(2024, 1, 1, 18, 0, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good evening")
        
        # 午夜0:00
        mock_datetime.now.return_value = datetime(2024, 1, 1, 0, 0, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good evening")
        
        # 凌晨5:59
        mock_datetime.now.return_value = datetime(2024, 1, 1, 5, 59, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good evening")

    @patch('src.my_greeter.datetime')
    def test_typical_times(self, mock_datetime):
        """测试各时段的典型时间点（上海时区）"""
        # 早上8:30
        mock_datetime.now.return_value = datetime(2024, 1, 1, 8, 30, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good morning")
        
        # 下午2:30
        mock_datetime.now.return_value = datetime(2024, 1, 1, 14, 30, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good afternoon")
        
        # 晚上9:30
        mock_datetime.now.return_value = datetime(2024, 1, 1, 21, 30, tzinfo=pytz.timezone('Asia/Shanghai'))
        self.assertEqual(self._my_greeter.greeting(), "Good evening")

    @patch('src.my_greeter.datetime')
    def test_different_timezones(self, mock_datetime):
        """测试不同时区的问候语"""
        # 设置一个固定的UTC时间：2024-01-01 12:00 UTC
        mock_datetime.now.return_value = datetime(2024, 1, 1, 12, 0, tzinfo=pytz.UTC)
        
        # 测试不同时区的问候语
        # 上海 UTC+8:00 -> 20:00
        self.assertEqual(self._my_greeter.greeting('Asia/Shanghai'), "Good evening")  
        # 纽约 UTC-5:00 -> 7:00
        self.assertEqual(self._my_greeter.greeting('America/New_York'), "Good morning")  
        # 伦敦 UTC+0:00 -> 12:00
        self.assertEqual(self._my_greeter.greeting('Europe/London'), "Good afternoon")  

    @patch('src.my_greeter.datetime')
    def test_invalid_timezone(self, mock_datetime):
        """测试无效时区处理"""
        mock_datetime.now.return_value = datetime(2024, 1, 1, 0, 0, tzinfo=pytz.UTC)
        with self.assertRaises(pytz.exceptions.UnknownTimeZoneError):
            self._my_greeter.greeting('Invalid/Timezone')

if __name__ == '__main__':
    unittest.main() 