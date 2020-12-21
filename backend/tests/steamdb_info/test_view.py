import pytest

from steamdb_info.services.utils import make_tag_info
from tests.steamdb_info.test_view_fixtures import *


@pytest.mark.asyncio
async def test_make_tag_info(make_tag_info_html, make_tag_info_result):
    result = await make_tag_info(make_tag_info_html)
    assert result[0] == make_tag_info_result
