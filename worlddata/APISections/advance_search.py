from worlddata.APIExceptions.WorldDataExceptions import WorldDataException

from worlddata.APISections.base import WorldDataBase


class WorldDataAdvanceSearch(WorldDataBase):

    def advance_search(self, search_text, sector, sub_sector, super_region, source, size, offset, **kwargs):
        return self.call_api_post("advanced-search", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region, source=source, size=size, offset=offset, kwargs=kwargs)

    def advance_search_attributes(self, search_text, sector, sub_sector, super_region, source, **kwargs):
        return self.call_api_post("attributes", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region, source=source, kwargs=kwargs)
    
    def news_sentiment(self, search_text, sector, sub_sector, super_region, source, type, **kwargs):
        return self.call_api_post("news/sentiment", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region, source=source, type = type, kwargs=kwargs)
    
    def news_entity_mapping(self, search_text, sector, sub_sector, super_region, source, **kwargs):
        return self.call_api_post("news/entity-mappings", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region, source=source, kwargs=kwargs)

    def news_search(self, search_text, size, offset, **kwargs):
        search_buckets = set()
        outputs = search_text.split()
        for search in outputs:
            search_buckets.update(search.split(','))

        if len(search_buckets) > 30:
            raise WorldDataException("Search term should be less than or equal to 30")
        
        search_text = ",".join(outputs)
        return self.call_api_post("advanced-search", search_text=search_text, sector='NEWS AI, SENTIMENTS', size=size,
                                  offset=offset, kwargs=kwargs)
