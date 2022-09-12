#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2022-09-07 11:48:48
@LastEditors    : yanyongyu
@LastEditTime   : 2022-09-07 12:13:55
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent

QQ_USER_MSG_EVENT = (PrivateMessageEvent,)
QQ_GROUP_MSG_EVENT = (GroupMessageEvent,)

USER_MSG_EVENT = QQ_USER_MSG_EVENT
GROUP_MSG_EVENT = QQ_GROUP_MSG_EVENT
