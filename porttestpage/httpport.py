# _*_ coding: utf-8 _*_
# @Time     : 2022/4/22 11:43
# @Author   : Mr_Li
# @FileName : httpport.py
from base.base_util import logger
import requests
import json


class HttpRequests():

    def __init__(self):
        self.session = requests.session()

    def send_request(self, method, url, headers, params_type='form', data=None, **kwargs):

        method = method.upper()
        params_type = params_type.upper()

        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception:
                data = eval(data)

        if 'GET' == method:

            response = self.session.request(method=method, url=url, headers=headers, data=data, **kwargs)

        elif 'POST' == method:

            if params_type == 'FORM':  # 发送表单数据，使用data传递参数
                logger.info("正在发送post请求，请求地址：{}， 请求参数{}".format(url, data))
                response = self.session.request(method=method, url=url, headers=headers, data=data, **kwargs)

            elif params_type == 'JSON':  # 使用JSON传递参数
                logger.info("正在发送post请求，请求地址：{}， 请求参数{}".format(url, json))
                response = self.session.request(method=method, url=url, headers=headers, json=data, **kwargs)

            else:

                response = self.session.request(method=method, url=url, headers=headers, **kwargs)
        else:

            raise ValueError('request method "{}" error ! please check'.format(method))

        return response

    def __call__(self, method, url, headers, params_type='form', data=None, **kwargs):

        return self.send_request(method, url, headers=headers, params_type=params_type, data=data, **kwargs)

    def close_session(self):

        self.session.close()
        try:
            del self.session.cookies['JSESSIONID']
        except:
            pass


request = HttpRequests()
if __name__ == '__main__':
    pass
