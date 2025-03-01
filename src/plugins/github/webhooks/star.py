#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Author         : yanyongyu
@Date           : 2022-12-18 13:44:11
@LastEditors    : yanyongyu
@LastEditTime   : 2022-12-21 20:02:36
@Description    : Webhook star event broadcast
@GitHub         : https://github.com/yanyongyu
"""
__author__ = "yanyongyu"

import asyncio
from datetime import timedelta

from nonebot import on_type
from nonebot.log import logger
from nonebot.params import Depends
from nonebot.plugin import PluginMetadata
from nonebot.adapters.github import StarCreated, StarDeleted

from src.plugins.github import config
from src.plugins.github.libs.message_tag import RepoTag
from src.plugins.github.libs.platform import get_user_bot, get_group_bot

from ._dependencies import (
    SEND_INTERVAL,
    Throttle,
    send_user_text,
    send_group_text,
    get_subscribed_users,
    get_subscribed_groups,
)

__plugin_meta__ = PluginMetadata(
    "GitHub Star 事件通知",
    "订阅 GitHub Star 事件来接收通知",
    "通知示例：\n用户 yanyongyu starred 仓库 cscs181/QQ-GitHub-Bot (共计 6666 个 star)",
)

THROTTLE_EXPIRE = timedelta(seconds=120)

star = on_type(
    (StarCreated, StarDeleted), priority=config.github_webhook_priority, block=True
)


@star.handle(
    parameterless=(Depends(Throttle((StarCreated, StarDeleted), THROTTLE_EXPIRE)),)
)
async def handle_star_event(event: StarCreated | StarDeleted):
    username = event.payload.sender.login
    repo_name = event.payload.repository.full_name
    action = event.payload.action
    star_count: int = event.payload.repository.stargazers_count
    action_name = "starred" if action == "created" else "unstarred"
    message = f"用户 {username} {action_name} 仓库 {repo_name} (共计 {star_count} 个 star)"

    owner, repo = repo_name.split("/", 1)
    tag = RepoTag(owner=owner, repo=repo, is_receive=False)

    for user in await get_subscribed_users(event):
        try:
            await send_user_text(user, get_user_bot(user), message, tag)
        except Exception as e:
            logger.opt(exception=e).warning(f"Send message to user {user} failed: {e}")
        await asyncio.sleep(SEND_INTERVAL)

    for group in await get_subscribed_groups(event):
        try:
            await send_group_text(group, get_group_bot(group), message, tag)
        except Exception as e:
            logger.opt(exception=e).warning(
                f"Send message to group {group} failed: {e}"
            )
        await asyncio.sleep(SEND_INTERVAL)
