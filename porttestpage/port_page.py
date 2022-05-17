# _*_ coding: utf-8 _*_
# @Time     : 2022/4/21 20:26
# @Author   : Mr_Li
# @FileName : port_page.py


class PortElement:

    gw_port = r'http://39.108.184.75:9073/timeline?versionFlag=-1'
    # 登录接口
    login_url = r'http://kbs.matrixdesign.cn/api/pmtapi/base_Account/login?username=wuyue&password=abc123456'
    loggin_headers = {"Content-Type": "application/json;charset=UTF-8"}
    # 测试数据
    login_test_value = '{"Content-Type": "application/json;charset=UTF-8"}'

    # 执行项目查询
    action_select_url = r'http://kbs.matrixdesign.cn/api/authapi/bsProInfo/getPagedList'
    # 请求数据
    action_projedt_select_value = {
        "skipCount": 1,
        "maxResultCount": 10,
        "sorting": "id descending",
        "auditStatus": "1",
        "module": 1
    }
    # 投标项目新增接口请求
    bid_project_save_port = r'http://kbs.matrixdesign.cn/api/authapi/bsProInfo/save'
    # 投标项目新增参数
    add_bid_project = {
        "bsType": "1280327614988423169",
        "proName": "新增硬装地产投标测试项目202204260001",
        "proType": "1284015946851291137",
        "bidAmount": 0,
        "proProvince": "130000",
        "proCity": "130300",
        "customerId": "1331086994964615170",
        "proAddress": "测试1",
        "sybCategory": "hardType",
        "bsDirectorId": "15531517835544798",
        "bsDirector": "何婷婷",
        "bsManager": "伍月",
        "bsManagerId": "15583162931904359",
        "bsProgress": "1458618619943587842",
        "planFinishDate": "2022-04-26 10:29:16",
        "proStartDate": "2022-04-26 10:29:18",
        "designDirection": "测试1213",
        "proSource": "1302936105011777538",
        "matrixArea": "华北",
        "adminArea": "华北地区",
        "companyEntity": "2",
        "isSupAgreement": "no",
        "createBy": "伍月",
        "createDate": "2022-04-27 10:28:07",
        "proRegister": "15583162931904359",
        "proRegisterTime": "2022-04-27 10:28:07",
        "isMineHard": "1326127662460178433",
        "signCompany": "厦门亿联软件有限公司",
        "bsProTender": {
            "commercialRate": "50",
            "returnTime": "2022-04-26 10:29:34",
            "skillRate": "50",
            "wasCooperation": "yes",
            "tenderStartTime": "2022-04-26 10:29:31",
            "isTech": "1395277357299929090"
        },
        "proStatus": "商务投标",
        "proStage": "1284035196542390273"
    }

    # 执行项目新增接口请求
    action_project_save_port = r'http://kbs.matrixdesign.cn/api/authapi/bsProInfo/save'
    # 执行项目新增参数
    action_add_project = {
        "bidAmount": 0,
        "bsPaymentList": [
            {
                "entityStatus": 0,
                "index": 0
            }
        ],
        "proName": "软装执行项目测试中2022042103",
        "bsType": "1280327578854494209",
        "proType": "1284015946851291137",
        "customerId": "1331086994964615170",
        "signCompany": "厦门亿联软件有限公司",
        "bsDirectorId": "15531517835544798",
        "bsDirector": "何婷婷",
        "bsManager": "伍月",
        "bsManagerId": "15583162931904359",
        "proSource": "1302935975869157378",
        "sybCategory": "softType",
        "auditStatus": 50,
        "proStage": "1284035504538521602",
        "sapNumber": "CS11434421",
        "proProvince": "210000",
        "proCity": "210400",
        "matrixArea": "东北",
        "adminArea": "东北地区",
        "proAddress": "测试1",
        "companyEntity": "2",
        "bsProDetailsList": [
            {
                "entityStatus": 1,
                "index": 0,
            }
        ],
        "isSupAgreement": "no",
        "isEstate": 1,
        "isWarrantyPeriod": "no",
        "createBy": "伍月",
        "createDate": "2022-04-21 11:13:02",
        "proRegister": "15583162931904359",
        "proRegisterTime": "2022-04-21 11:13:03",
        "isMineHard": "1326127662460178433",
        "hardCompany": "矩阵纵横设计股份有限公司",
        "designDirection": "1测试1",
        "preference": "测1试",
        "isArtNeeds": "暂无1",
        "isSingleList": "yes",
        "isPleasedHard": "yes",
        "planFinishDate": "2022-04-21 11:22:53",
        "proStartDate": "2022-04-21 11:22:58",
        "expectContractSignTime": "2022-04-21 11:23:01",
        "bsProgress": "1326161122331594754",
        "proStatus": "直委项目",
        "bsProFollowRecordList": [
            {
                "entityStatus": 1,
                "hasError": 'false',
                "index": 0
            }
        ]
    }

    # 执行项目查看项目接口请求
    action_project_examine_port = r'http://kbs.matrixdesign.cn/api/authapi/bsProInfo/getSWById'
    # 执行项目查看参数
    action_examine = '{"id": 1518864408166666241}'
