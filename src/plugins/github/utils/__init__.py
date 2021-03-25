#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2021-03-25 15:32:20
@LastEditors    : yanyongyu
@LastEditTime   : 2021-03-25 15:37:16
@Description    : None
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

from typing import Any, Type, Union

from nonebot.matcher import Matcher
from nonebot.adapters import Message, MessageSegment

from ..libs.redis import set_message_info


async def send_github_message(
        matcher: Type[Matcher], owner: str, repo: str, number: int,
        message: Union[str, Message, MessageSegment]) -> Any:
    message_id: int = await matcher.send(message)
    set_message_info(str(message_id), owner, repo, number)
    return message_id
