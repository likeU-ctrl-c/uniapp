#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
from flask import Flask, request, jsonify, make_response, abort, json, send_from_directory
from flask_cors import *

import json


app = Flask(__name__)
#设置跨域
CORS(app, supports_credentials=True)

@app.route('/getlunbo', methods=['GET'])
def getlunbo():
    test={
        "swiper":[
                    {
                        "id": "1",
                        "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                    },
                    {
                        "id": "2",
                        "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=4974d8d16f0d5174bbd74e642028934b&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D3616242789%2C1098670747%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D900%26h%3D1350'
                    },
                    {
                        "id": "3",
                        "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=20a9cc1c409b7fbdd21ac624fcd53dfc&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2247852322%2C986532796%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853'
                    },
                    {
                        "id": "4",
                        "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                    },
                    {
                        "id": "5",
                        "picurl": 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg'
                    }
                ],
        "timeout":5000
    }
    return json.dumps(test)


@app.route('/gethotgoods/<int:pageindex>', methods=['GET'])
def gethotgoods(pageindex):
    print(pageindex)
    if pageindex > 5:
        test={
            "status":0,
            "message":[
                        {
                            "id": "5",
                            "title":'华为（HUAWEI）荣耀6Plus 16G双4G款',
                            "add_time":'2005-04-19T16:51:03.000z',
                            "zhaiyao":'荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版',
                            "sell_price":2195,
                            "make_price":2495,
                            "stock_quantity":60,
                            "picurl": 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg'
                        }
                    ],
            "timeout":5000
        }
        return test
    else:
        test={
            "status":0,
            "message":[
                        {
                            "id": "1",
                            "title":'华为（HUAWEI）荣耀6Plus 16G双4G款',
                            "add_time":'2005-04-19T16:51:03.000z',
                            "zhaiyao":'荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版',
                            "sell_price":2195,
                            "make_price":2495,
                            "stock_quantity":60,
                            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                        },
                        {
                            "id": "2",
                            "title":'华为（HUAWEI）荣耀6Plus 16G双4G款',
                            "add_time":'2005-04-19T16:51:03.000z',
                            "zhaiyao":'荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版',
                            "sell_price":2195,
                            "make_price":2495,
                            "stock_quantity":60,
                            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=4974d8d16f0d5174bbd74e642028934b&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D3616242789%2C1098670747%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D900%26h%3D1350'
                        },
                        {
                            "id": "3",
                            "title":'华为（HUAWEI）荣耀6Plus 16G双4G款',
                            "add_time":'2005-04-19T16:51:03.000z',
                            "zhaiyao":'荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版',
                            "sell_price":2195,
                            "make_price":2495,
                            "stock_quantity":60,
                            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=20a9cc1c409b7fbdd21ac624fcd53dfc&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2247852322%2C986532796%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853'
                        },
                        {
                            "id": "4",
                            "title":'华为（HUAWEI）荣耀6Plus 16G双4G款',
                            "add_time":'2005-04-19T16:51:03.000z',
                            "zhaiyao":'荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版',
                            "sell_price":2195,
                            "make_price":2495,
                            "stock_quantity":60,
                            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                        },
                        {
                            "id": "5",
                            "title":'华为（HUAWEI）荣耀6Plus 16G双4G款',
                            "add_time":'2005-04-19T16:51:03.000z',
                            "zhaiyao":'荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版',
                            "sell_price":2195,
                            "make_price":2495,
                            "stock_quantity":60,
                            "picurl": 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg'
                        }
                    ],
            "timeout":5000
        }
        return json.dumps(test)



@app.route('/getimgcategory/', methods=['GET'])
def getimgcategory():
    test={
        "status":0,
        "message":[
                    {"title":"家居生活","id":14},
                    {"title":"摄影设计","id":15},
                    {"title":"明星美女","id":16},
                    {"title":"空间设计","id":17},
                    {"title":"户型装修","id":18},
                    {"title":"广告摄影","id":19},
                    {"title":"摄影学习","id":20},
                    {"title":"摄影素材","id":21},
                    {"title":"明星写真","id":22},
                    {"title":"清纯美女","id":23},
                    {"title":"古典美女","id":24}
                ],
        "timeout":5000
    }
    return json.dumps(test)

@app.route('/getimg/<int:id>', methods=['GET'])
def getimg(id):
    print(id)
    imgsrc = [
        {
            "id": "1",
            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920',
            "text":"今天很难过"
        },
        {
            "id": "2",
            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=4974d8d16f0d5174bbd74e642028934b&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D3616242789%2C1098670747%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D900%26h%3D1350',
            "text":"今天很难过"
        },
        {
            "id": "3",
            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=20a9cc1c409b7fbdd21ac624fcd53dfc&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2247852322%2C986532796%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853',
            "text":"今天很难过"
        },
        {
            "id": "4",
            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920',
            "text":"今天很难过 ,因为不知道   ----==---- -- ===-=-=-"
        },
        {
            "id": "5",
            "picurl": 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg',
            "text":"今天很难过  因为不知道   ----==---- -- ===-=-=-"
        },
        {
            "id": "1",
            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920',
            "text":"今天很难过  因为不知道   ----==---- -- ===-=-=-"
        },
        {
            "id": "2",
            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=4974d8d16f0d5174bbd74e642028934b&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D3616242789%2C1098670747%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D900%26h%3D1350',
            "text":"今天很难过  因为不知道   ----==---- -- ===-=-=-"
        },
        {
            "id": "3",
            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=20a9cc1c409b7fbdd21ac624fcd53dfc&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2247852322%2C986532796%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853',
            "text":"今天很难过  因为不知道   ----==---- -- ===-=-=-"
        },
        {
            "id": "4",
            "picurl": 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920',
            "text":"今天很难过  因为不知道   ----==---- -- ===-=-=-"
        },
        {
            "id": "5",
            "picurl": 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg',
            "text":"今天很难过  因为不知道   ----==---- -- ===-=-=-"
        }
    ]
    id = id - 14
    # print(imgsrc[id])
    test={
        "status":0,
        "message":[imgsrc[id]],
        "timeout":5000
    }
    return json.dumps(test)


@app.route("/getnews/",methods=['GET'])
def getNews():
    tes={
        'status':0,
        'message':[
            {
                'id':2,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":1,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            },
            {
                'id':3,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":11,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            },
            {
                'id':4,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":111,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            },
            {
                'id':5,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":11111,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            },
            {
                'id':6,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":1111111,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            },
            {
                'id':7,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":11111,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            },
            {
                'id':8,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":1111,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            },
            {
                'id':9,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":111,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            },
            {
                'id':10,
                "title":"今天很难过，很难过，有些事不是不去想就不存在了。",
                "addtime":'2015-04-18T09:08:56.000Z',
                "zhaiyao":"今天很难过，很难过，也很难受。",
                "click":11,
                "imgurl":"https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg"
            }
        ]
    }
    return json.dumps(tes)


@app.route("/getdetail/<int:id>",methods=['GET'])
def getDetail(id):
    # print("====="+str(id))
    test = {
        "status":0,
        "message":[
            {
                "id":2,
                "title":"这是一个标题",
                "click":20,
                "add_time":"2015-04-18T09:08:56.000Z",
                "content":"""
                <p>1.除了这一生，我们又没有别的时间能走多远，就走多远——花儿与少年</p>\r\n<p>

2.

就算生活再累再辛苦只要有一个坚定的伙伴就可以了这就是人生。——《季春奶奶》\r\n</p><p>

3.

我活在世上，无非想要明白些道理，遇见些有趣的事，倘能如我愿，我的一生就算成功。——王小波\r\n</p><p>



4.

人们宁愿去关心一个蹩脚电影演员的吃喝拉撒和鸡毛蒜皮，\r\n</p><p>

而不愿了解一个普通人波涛汹涌的内心世界。\r\n</p><p>

——路遥《平凡的世界》\r\n</p><p>
"""
            }
        ]
    }
    return json.dumps(test)




@app.route("/getSwiper/<int:id>",methods=['GET'])
def getSwiper(id):
    print(id)
    test = {
       'message':[
                    {
                        "id": "1",
                        "picurl": ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                                    ,'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                                    ,'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                                  ]
                    },
                    {
                        "id": "2",
                        "picurl": ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=4974d8d16f0d5174bbd74e642028934b&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D3616242789%2C1098670747%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D900%26h%3D1350'
                                    ,'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=4974d8d16f0d5174bbd74e642028934b&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D3616242789%2C1098670747%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D900%26h%3D1350'
                                    ,'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=4974d8d16f0d5174bbd74e642028934b&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D3616242789%2C1098670747%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D900%26h%3D1350'                    
                                  ]
                    },
                    {
                        "id": "3",
                        "picurl": ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=20a9cc1c409b7fbdd21ac624fcd53dfc&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2247852322%2C986532796%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853'
                                    ,'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=20a9cc1c409b7fbdd21ac624fcd53dfc&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2247852322%2C986532796%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853'
                                    ,'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035892279&di=20a9cc1c409b7fbdd21ac624fcd53dfc&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D2247852322%2C986532796%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853'                     
                                  ]
                    },
                    {
                        "id": "4",
                        "picurl": ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                                    ,'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                                    ,'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1601035818949&di=f60ca61276f0ee664e68fc58caed4201&imgtype=0&src=http%3A%2F%2Ft7.baidu.com%2Fit%2Fu%3D1788978885%2C1014571020%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D1920'
                                  ]
                    },
                    {
                        "id": "5",
                        "picurl":[ 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg'
                                ,'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg'
                                ,'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg'
                                ]
                    
                    }
                ]
    }
    return json.dumps(test)


@app.route("/getgoodsInfo/<int:id>",methods=['GET'])
def getGoodsInfo(id):
    print(id)
    test={
        "status":0,
        "id": "5",
        "title":'华为（HUAWEI）荣耀6Plus 16G双4G款',
        "huohao":"sd12345",
        "kucun":200,
        "add_time":'2005-04-19T16:51:03.000z',
        "zhaiyao":'荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版,荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版,荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版,荣耀6Plus,该机想分为两款型号，分别为PF,华为（HUAWEI）荣耀6Plus 16G双4G版',
        "sell_price":2195,
        "make_price":2495,
        "stock_quantity":60,
        "picurl": 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=280591509,585529894&fm=26&gp=0.jpg'
    }
    return json.dumps(test)

# @app.route('/create/task', methods=["POST"])
# def submit_task():
#     global sandbox_db
#     # 获取发送过来的参数
#     file = request.files['file']
#     package = request.form.get("package", "")
#     if package == "":
#         return jsonify(success=False, msg="package not exit", data="")
#     timeout = request.form.get("timeout", "")
#     if timeout == "":
#         return jsonify(success=False, msg="timeout not exit", data="")
#     priority = request.form.get("priority", 1)
#     options = request.form.get("options", "")
#     if options != "":
#         options += ","
#     options += "procmemdump=yes,route=none"
#
#     machine = request.form.get("machine", "")
#     platform = request.form.get("platform", "")
#     if platform == "":
#         return jsonify(success=False, msg="platform not exit", data="")
#
#     r_taskid = int(request.form.get("taskid", ""))
#
#     tags = request.form.get("tags", None)
#     custom = request.form.get("custom", "")
#     owner = request.form.get("owner", "")
#     clock = request.form.get("clock", None)
#     memory = parse_bool(request.form.get("memory", 0))
#     enforce_timeout = parse_bool(request.form.get("enforce_timeout", 0))
#     # 获取文件名称
#     file_name = file.filename
#     # 获取文件内容
#     content = file.read()
#     # 创建临时文件
#     temp_path, temp_file_path = Files.create_temp_file(file_name, content)
#     # 创建sumbit
#     dict_data = {}
#     dict_data['errors'] = []
#     in_data = {}
#     in_data['data'] = temp_file_path
#     in_data['type'] = 'file'
#     in_data['options'] = {}
#     dict_data['data'] = []
#     dict_data['data'].append(in_data)
#     dict_data['options'] = {}
#
#     # 返回sumbit_id的值
#     submit_id = sandbox_db.add_submit(
#         temp_path, "files", dict_data
#     )
#     # 提交任务
#     task_id = sandbox_db.add_path(
#         file_path=temp_file_path,
#         package=package,
#         timeout=timeout,
#         priority=priority,
#         options=options,
#         machine=machine,
#         platform=platform,
#         tags=tags,
#         custom=custom,
#         owner=owner,
#         memory=memory,
#         enforce_timeout=enforce_timeout,
#         clock=clock,
#         submit_id=submit_id
#     )
#
#     remote_task_id = sandbox_db.add_rtask_id(r_taskid, task_id)
#
#     # 创建rule规则目录
#     if not os.path.exists("storage"):
#         os.mkdir("storage")
#     storage = "storage/" + str(task_id)
#     # 判断存储目录是否存在
#     if not os.path.exists(storage):
#         os.mkdir(storage)
#     rule_path = os.path.join(storage, "myrules")
#     os.mkdir(rule_path)
#
#     return jsonify(success=True, msg="build task", data=str(remote_task_id))
#
#
# @app.route('/task/result/<int:task_id>', methods=["GET"])
# def task_result(task_id):
#     local_task_id = sandbox_db.view_ltaskid_by_rtaskid(int(task_id))
#     result_file = "storage/" + str(local_task_id) + "/reports/result_2.json"
#     if os.path.exists(result_file):
#         try:
#
#             direcotry = "storage/" + str(local_task_id) + "/reports"
#             file_name = "result_2.json"
#             response = make_response(
#                 send_from_directory(direcotry, file_name, as_attachment=True))
#             return response
#         except Exception as e:
#             return jsonify({"code": "error", "message": "{}".format(e)})
#     else:
#         return jsonify({"code": "error", "message": "{no result file}"})
#
#
# @app.route('/task/pcap/<int:task_id>', methods=["GET"])
# def task_pcap(task_id):
#     local_task_id = sandbox_db.view_ltaskid_by_rtaskid(int(task_id))
#     result_file = "storage/" + str(local_task_id) + "/dump.pcap"
#     if os.path.exists(result_file):
#         try:
#             direcotry = "storage/" + str(local_task_id)
#             file_name = "dump.pcap"
#             response = make_response(
#                 send_from_directory(direcotry, file_name, as_attachment=True))
#             return response
#         except Exception as e:
#             return jsonify({"code": "error", "message": "{}".format(e)})
#     else:
#         return jsonify({"code": "error", "message": "{no result file}"})


def main():
    app.run(host='0.0.0.0', port=8808)


if __name__ == '__main__':
    main()
