from worlddata.APISections.base import WorldDataBase


class WorldDataAdvanceSearch(WorldDataBase):

    def advance_search(self, search_text, sector, sub_sector, super_region, source, meta_ids, size, offset, **kwargs):
        return self.call_api_post("advanced-search", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region,
                                  source=source, meta_ids=meta_ids, size=size, offset=offset, kwargs=kwargs)

    def advance_search_attributes(self, search_text, sector, sub_sector, super_region, source, meta_ids,
                                  **kwargs):
        return self.call_api_post("attributes", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region,
                                  source=source, meta_ids=meta_ids, kwargs=kwargs)
