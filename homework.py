"""
作业：
下面的程序实现了从网站交易所实时获取k线数据，
1、读懂下面的基本程序
2、通过循环的功能实现程序能循环获取数据,获取成功k线数据后，休息10秒钟再次运行。
3、引入容错机制，如果抓取数据出错，报错，提示“获取K线数据，失败，稍后重试。”，30秒后重试。超过5次自动跳出程序。
4、把上面的功能封装成函数,函数名为"fetch_candle_data",需要设置参数，控制stock_code,k_type,num,max_try_amount。
"""
from urllib.request import urlopen  # python自带爬虫库
import json  # python自带的json数据库
from random import randint  # python自带的随机数库
import pandas as pd
import time
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 5000)  # 最多显示数据的行数


# =====创建随机数的函数
def _random(n=16):
    """
    创建一个n位的随机整数
    :param n:
    :return:
    """
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))

def fetch_candle_data(stock_code,k_type,num,max_try_amount):
    # =====获取分钟级别的K线
    # 获取K线数据：http://ifzq.gtimg.cn/appstock/app/kline/mkline?param=sz000001,m5,,640&_var=m5_today&r=0.6508601564534552   平安银行
    # 正常网址：http://stockhtm.finance.qq.com/sstock/ggcx/000001.shtml
    num=0
    # ===构建网址
    # 参数
    #stock_code = 'sh600000'  # # 正常股票sz000001，指数sh000001, ETF sh510500
    #k_type = 1  # 1, 5, 15, 30, 60
    #num = 10  # 最多不能超过320
    while(1):
        try:
    # 构建url
            url = 'http://ifzq.gtimg.cn/appstock/app/kline/mkline?param=%s,m%s,,%s&_var=m%s_today&r=0.%s'
            url = url % (stock_code, k_type, num, k_type, _random())

            # ===获取数据
            content = urlopen(url=url, timeout=15).read().decode()  # 使用python自带的库，从网络上获取信息

            # ===将数据转换成dict格式
            content = content.split('=', maxsplit=1)[-1]
            content = json.loads(content)

            # ===将数据转换成DataFrame格式
            k_data = content['data'][stock_code]['m'+str(k_type)]
            df = pd.DataFrame(k_data)

            # ===对数据进行整理
            rename_dict = {0: 'candle_end_time', 1: 'open', 2: 'close', 3: 'high', 4: 'low', 5: 'amount'}
            # 其中amount单位是手
            df.rename(columns=rename_dict, inplace=True)
            df['candle_end_time'] = df['candle_end_time'].apply(lambda x: '%s-%s-%s %s:%s' % (x[0:4], x[4:6], x[6:8], x[8:10], x[10:12]))
            df['candle_end_time'] = pd.to_datetime(df['candle_end_time'])
            df = df[['candle_end_time', 'open', 'high', 'low', 'close', 'amount']]
            print(df)
            time.sleep(10)
        except Exception:
            print("获取K线数据，失败，稍后重试。")
            num+=1
            if num>max_try_amount:
                return
            time.sleep(30)
fetch_candle_data('sh600000',1,10,5)


    # ===考察其他周期、指数、ETF

    # ===考察特殊情况
    # 正常股票：sz000001 sz000002，退市股票：sh600002 sz000003、停牌股票：sz300124，上市新股：sz002952，除权股票：sh600276，





















