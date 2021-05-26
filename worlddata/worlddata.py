# -*-coding:utf-8-*-

from worlddata.APISections.advance_search import WorldDataAdvanceSearch
from worlddata.APISections.search import WorldDataSearch
from worlddata.APISections.time_series import WorldDataTimeSeries


class WorldData(
    WorldDataSearch,
    WorldDataTimeSeries,
    WorldDataAdvanceSearch
):
    pass
