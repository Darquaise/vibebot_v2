from __future__ import annotations

import discord
from discord.ext import bridge
from typing import Union


class VibeBot(bridge.Bot):
    inst: VibeBot = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, command_prefix=self._get_prefix_command, case_insensitive=True)

    @classmethod
    def _get_prefix_command(cls, _client, _: discord.Message):
        return '!'

    async def is_owner(self, user: Union[discord.User, discord.Member, int]) -> bool:
        if self.owner_id:
            if self.owner_ids:
                self.owner_ids.append(self.owner_id)
            else:
                self.owner_ids = [self.owner_id]
            self.owner_id = None
        elif not self.owner_ids:
            app = await self.application_info()
            if app.team:
                self.owner_ids = {m.id for m in app.team.members}
            else:
                self.owner_ids = [app.owner.id]

        if isinstance(user, int):
            return user in self.owner_ids
        else:
            return user.id in self.owner_ids

    def is_self(self, member: Union[discord.Member, discord.User]):
        return self.user.id == member.id
