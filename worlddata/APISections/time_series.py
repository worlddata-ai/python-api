from worlddata.APISections.base import WorldDataBase


class WorldDataTimeSeries(WorldDataBase):

    def time_series(self, sector, sub_sector, super_region, source, trend_ids):
        return self.call_api_post("time-series", sector=sector, subSector=sub_sector, superRegion=super_region,
                                  source=source, trendIds=trend_ids)
