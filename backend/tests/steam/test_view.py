import pytest

from steam.services.utils import Game
from tests.steam.test_view_fixtures import *


@pytest.mark.asyncio
async def test_make_game_list(make_game_list_html_text, make_game_list_result):
    result = await Game.make_game_list(make_game_list_html_text)
    assert result[0] == make_game_list_result
