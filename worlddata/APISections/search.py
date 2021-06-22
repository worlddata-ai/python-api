from worlddata.APISections.base import WorldDataBase


class WorldDataSearch(WorldDataBase):

    def search(self, search_text, **kwargs):
        return self.call_api_post("search", search_text=search_text, kwargs=kwargs)
    