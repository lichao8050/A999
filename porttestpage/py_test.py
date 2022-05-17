# _*_ coding: utf-8 _*_
# @Time     : 2022/4/20 9:37
# @Author   : Mr_Li
# @FileName : py_test.py

import requests
import json

s = requests.session()
url = "http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login?username=chenyinyan&password=abc123456"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8"
}
data = {"Content-Type" : "application/x-www-form-urlencoded"}
r = s.post(url, headers, json=data)
print(r.status_code)
print(r.headers['Set-Cookie'])
print(r.url)
url1 = "http://kbs.matrixdesign.cn/api/authapi/bsProInfo/getPagedList"
data = {
        "skipCount": 1,
        "maxResultCount": 10,
        "sorting": "id descending",
        "pro_stage": "1280322514521821185"
    }
r2 = s.post(url=url1, headers=headers, json=data)
print(r2.text)


# r.encoding = "UTF-8"
# print(r.json())
# url1 = "http://kbs.matrixdesign.cn/api/authapi/bsProInfo/getPagedList"
# data = {
#     "skipCount": 1,
#     "maxResultCount": 10,
#     "module": 1,
#     "proName": "测试2204201112"
# }
#
# r2 = s.post(url=url1, headers=headers, json=data)
# print(r2.text)
# url2 = "http://kbs.matrixdesign.cn/api/authapi/bsCustomer/save"
# data2 = {
#     "customerName": "栋来西往12",
#     "ownerName": "郑鸿晖",
#     "owner": "16073917709738137",
#     "customerArea": "华南",
#     "customerProvince": "440000",
#     "customerCity": "440200",
#     "adminArea": "华南地区",
#     "customerType": "1280319512448733185",
#     "customerGrade": "customer_grade_d",
#     "bsStakeholderList": [
#         {
#             "entityStatus": 0,
#             "index": 0,
#             "name": "测试张三丰2",
#             "phone": "16548754512",
#             "address": "测试阿萨达11",
#             "type": "1280322115026948097",
#             "job": "1测试121"
#         }
#     ],
#     "groupName": "测试港深集团013"
# }
# r3 = s.post(url=url2, headers=headers, json=data2)
# print(r3.text)
'''执行项目新增'''
# url3 = "http://kbs.matrixdesign.cn/api/authapi/bsProInfo/save"
# data3 = {
#     "bidAmount": 0,
#     "bsPaymentList": [
#         {
#             "entityStatus": 0,
#             "index": 0
#         }
#     ],
#     "proName": "软装执行项目测试中2022042102",
#     "bsType": "1280327578854494209",
#     "proType": "1284015946851291137",
#     "customerId": "1331086994964615170",
#     "signCompany": "厦门亿联软件有限公司",
#     "bsDirectorId": "15531517835544798",
#     "bsDirector": "何婷婷",
#     "bsManager": "伍月",
#     "bsManagerId": "15583162931904359",
#     "proSource": "1302935975869157378",
#     "sybCategory": "softType",
#     "auditStatus": 50,
#     "proStage": "1284035504538521602",
#     "sapNumber": "CS11434421",
#     "proProvince": "210000",
#     "proCity": "210400",
#     "matrixArea": "东北",
#     "adminArea": "东北地区",
#     "proAddress": "测试1",
#     "companyEntity": "2",
#     "bsProDetailsList": [
#         {
#             "entityStatus": 1,
#             "index": 0,
#         }
#     ],
#     "isSupAgreement": "no",
#     "isEstate": 1,
#     "isWarrantyPeriod": "no",
#     "createBy": "伍月",
#     "createDate": "2022-04-21 11:13:02",
#     "proRegister": "15583162931904359",
#     "proRegisterTime": "2022-04-21 11:13:03",
#     "isMineHard": "1326127662460178433",
#     "hardCompany": "矩阵纵横设计股份有限公司",
#     "designDirection": "1测试1",
#     "preference": "测1试",
#     "isArtNeeds": "暂无1",
#     "isSingleList": "yes",
#     "isPleasedHard": "yes",
#     "planFinishDate": "2022-04-21 11:22:53",
#     "proStartDate": "2022-04-21 11:22:58",
#     "expectContractSignTime": "2022-04-21 11:23:01",
#     "bsProgress": "1326161122331594754",
#     "proStatus": "直委项目",
#     "bsProFollowRecordList": [
#         {
#             "entityStatus": 1,
#             "hasError": 'false',
#             "index": 0
#         }
#     ]
# }
# r4 = s.post(url=url3, headers=headers, json=data3)
# print(r4.text)
# '''增加合同详情'''
# url4 = "http://kbs.matrixdesign.cn/api/authapi/bsProDetails/batchSave"
# data4 = {
#     "adminArea": "东北地区",
#     "auditStatus": "50",
#     "auditStatusName": "未提交",
#     "bidAmount": 2200000.55,
#     "bsDirector": "何婷婷",
#     "bsDirectorId": "15531517835544798",
#     "bsManager": "伍月",
#     "bsManagerId": "15583162931904359",
#     "bsProDetailsList": [
#         {
#             "contractArea": "1",
#             "actualTotaltax": "1000000",
#             "contractPrice": "1",
#             "houseTypeList": [
#                 {
#                     "datastatus": 0,
#                     "houseName": "售楼处\\会所",
#                     "id": "3125768993969508698",
#                     "parentId": "1458255025502556162",
#                     "parentName": "地产"
#                 },
#                 {
#                     "datastatus": 0,
#                     "houseName": "别墅\\合院",
#                     "id": "3125768993969508699",
#                     "parentId": "1458255025502556162",
#                     "parentName": "地产"
#                 },
#                 {
#                     "datastatus": 0,
#                     "houseName": "创意样板间",
#                     "id": "3125768993969508700",
#                     "parentId": "1458255025502556162",
#                     "parentName": "地产"
#                 },
#                 {
#                     "datastatus": 0,
#                     "houseName": "批量精装(5套以上)",
#                     "id": "3125768993969508701",
#                     "parentId": "1458255025502556162",
#                     "parentName": "地产"
#                 },
#                 {
#                     "datastatus": 0,
#                     "houseName": "公区\\大堂\\架空层",
#                     "id": "3125768993969508702",
#                     "parentId": "1458255025502556162",
#                     "parentName": "地产"
#                 },
#                 {
#                     "datastatus": 0,
#                     "houseName": "集团标准化",
#                     "id": "3125768993969508703",
#                     "parentId": "1458255025502556162",
#                     "parentName": "地产"
#                 },
#                 {
#                     "datastatus": 0,
#                     "houseName": "其他地产",
#                     "id": "3125768993969508704",
#                     "parentId": "1458255025502556162",
#                     "parentName": "地产"
#                 },
#                 {
#                     "datastatus": 0,
#                     "houseName": "精装样板间(5套以下)不含5",
#                     "id": "3125768993972140981",
#                     "parentId": "1458255025502556162",
#                     "parentName": "地产"
#                 }
#             ],
#             "houseTypeDetialString": "精装样板间(5套以下)不含5",
#             "entityStatus": 1,
#             "index": 0,
#             "executeRatio": 20,
#             "sybCompany": "beijingCompany",
#             "oldSybCategory": "ruanzhuangSyb",
#             "sybCategory": "ruanzhuangSyb",
#             "designDirectorId": "03635351101229430",
#             "principalId": "151850500129493911",
#             "designDirectorName": "陈达",
#             "principalName": "田佳艺",
#             "isExecute": "yes",
#             "teamId": "113691687",
#             "teamName": "SZRZ田佳艺组",
#             "houseType": "1458255025502556162",
#             "houseTypeDetial": "3125768993972140981",
#             "houseTypeRemark": "测试户型1",
#             "contractNum": "1",
#             "contractTotaltax": "1",
#             "contractOtherrequire": "暂无1",
#             "businessId": "1516983746484637697"
#         },
#         {
#             "sybCompany": "shenzhenCompany",
#             "oldSybCategory": "ruanzhuangSyb",
#             "sybCategory": "ruanzhuangHzSyb",
#             "teamName": "小雨组",
#             "teamId": "618361125",
#             "designDirectorId": "213616121837730958",
#             "principalId": "16448043650439695",
#             "designDirectorName": "陈小灵",
#             "principalName": "聂瓅",
#             "houseType": "1458255269879484417",
#             "contractNum": "1",
#             "contractOtherrequire": "暂无1",
#             "isExecute": "yes",
#             "contractTotaltax": "1",
#             "contractPrice": "1",
#             "contractArea": "1",
#             "actualTotaltax": "1200000.5",
#             "indexs": 1,
#             "index": 1,
#             "executeRatio": 23,
#             "houseTypeRemark": "豪宅1",
#             "businessId": "1516983746484637697"
#         }
#     ],
#     "bsProgress": "1326161122331594754",
#     "bsType": "1280327578854494209",
#     "changeDetails": "yes",
#     "companyEntity": "2",
#     "contracts": [
#         {
#             "datastatus": 0,
#             "id": "1516981119923392513"
#         }
#     ],
#     "createBy": "15583162931904359",
#     "createDate": "2022-04-21 11:13:02",
#     "customerId": "1331086994964615170",
#     "datastatus": 0,
#     "designDirection": "测试1",
#     "designDirectorId": "213616121837730958",
#     "designDirectorName": "陈小灵",
#     "expectContractSignTime": "2022-04-21 11:23:01",
#     "hardCompany": "矩阵纵横设计股份有限公司",
#     "id": "1516983746484637697",
#     "isArtNeeds": "暂无1",
#     "isEstate": 1,
#     "isMineHard": "1326127662460178433",
#     "isPleasedHard": "yes",
#     "isSingleList": "yes",
#     "isSupAgreement": "no",
#     "isWarrantyPeriod": "no",
#     "matrixArea": "东北",
#     "planFinishDate": "2022-04-21 00:00:00",
#     "preference": "测试",
#     "proAddress": "测试1",
#     "proCity": "210400",
#     "proCode": "RZ118202",
#     "proName": "软装执行项目测试中2022042102",
#     "proProvince": "210000",
#     "proSource": "1302935975869157378",
#     "proStage": "1284035504538521602",
#     "proStartDate": "2022-04-21 00:00:00",
#     "proStatus": "直委项目",
#     "proType": "1284015946851291137",
#     "sapNumber": "CS11434421",
#     "signCompany": "厦门亿联软件有限公司",
#     "sybCategory": "softType",
#     "updateBy": "15583162931904359",
#     "updateDate": "2022-04-21 11:24:18"
# }
# r5 = s.post(url=url4, headers=headers, json=data4)
# print(r5.text)
