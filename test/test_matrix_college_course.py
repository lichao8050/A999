# _*_ coding: utf-8 _*_
# @Time    : 2021/5/13 0013 23:15
# @Author  : Mr_Li
# @FileName: test_add_customer.py
from base.base_util import BaseUtil
from pageobject.matrix_college_course import MatrixCollegeCourse


class TestMatrixCollegeCourse(BaseUtil):
    """矩阵学院"""

    def test_matrixcollege(self):
        xz_kh1 = MatrixCollegeCourse(self.driver)
        xz_kh1.test_matrix_college(username='renzhaopan', password='abc123456')
