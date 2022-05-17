# _*_ coding: utf-8 _*_
# @Time    : 2021/8/21 0021 12:05
# @Author  : Mr_Li
# @FileName: read_config.py
import yaml
import os


class ReadConfig:

    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            xs_dict = yaml.load(stream=f.read(), Loader=yaml.FullLoader)
            print(xs_dict)

    # 写入yaml文件
    def write_yaml(self):
        """mode=w写入 mode=r读取  mode=a 追加写入 """
        with open(self.yaml_file, encoding='utf-8', mode='a') as f:
            data = ('heqiangming', 'abc123456')
            yaml.dump(data, stream=f, allow_unicode=True)


if __name__ == '__main__':
    rc = ReadConfig('E:\\A999\\yaml\\purchasing_class.yaml')
    # 读取yaml文件内容
    rc.read_yaml()
    # 写入yaml文件
    # rc.write_yaml()
