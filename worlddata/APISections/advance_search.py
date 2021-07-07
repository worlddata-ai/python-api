import re
from operator import itemgetter

from worlddata.APIExceptions.WorldDataExceptions import WorldDataException
from worlddata.APISections.base import WorldDataBase


class WorldDataAdvanceSearch(WorldDataBase):

    def advance_search(self, search_text, sector, sub_sector, super_region, source, size, offset, **kwargs):
        return self.call_api_post("advanced-search", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region, source=source, size=size, offset=offset, kwargs=kwargs)
    
    def advance_search_with_bucket(self, bucket, size, offset, **kwargs):
        return self.call_api_post("advanced-search-with-bucket", bucket=bucket, size=size, offset=offset, kwargs=kwargs)

    def advance_search_attributes(self, search_text, sector, sub_sector, super_region, source, **kwargs):
        return self.call_api_post("attributes", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region, source=source, kwargs=kwargs)

    def news_sentiment(self, search_text, sector, sub_sector, super_region, source, type, **kwargs):
        return self.call_api_post("news/sentiment", search_text=search_text, sector=sector, sub_sector=sub_sector,
                                  super_region=super_region, source=source, type=type, kwargs=kwargs)

    def news_entity_mapping(self, search_text, sector, sub_sector, super_region, source, **kwargs):
        news_json = self.call_api_post("news/entity-mappings", search_text=search_text, sector=sector,
                                       sub_sector=sub_sector,
                                       super_region=super_region, source=source, kwargs=kwargs)
        text = ''
        for item in news_json:
            for key in item:
                if item[key] and len(item[key]) > 0:
                    if len(text) == 0:
                        text = item[key][0].replace(';', ',')
                    else:
                        text = text + ',' + item[key][0].replace(';', ',')

        lines = re.split("\s|(?<!\d)[,.](?!\d)", text)

        str2 = []
        data = []
        # loop till string values present in list str
        for i in lines:

            # checking for the duplicacy
            if i not in str2:
                # insert value in str2
                str2.append(i)

        for i in range(0, len(str2)):
            if len(str2[i]) > 1:
                obj = {
                    'name': str2[i],
                    'weight': lines.count(str2[i])
                }
                data.append(obj)

        data.sort(key=itemgetter('weight'), reverse=True)

        data = data[0:25:]

        data_list = []

        for fromIndex, fromItem in enumerate(data):
            for toIndex, toItem in enumerate(data):
                if fromIndex == toIndex:
                    continue

                data_item = {'from': fromItem['name'], 'to': toItem['name'], 'weight': 0};
                for item in news_json:
                    for key in item:
                        join_list = ' '.join(item[key])
                        if join_list and len(join_list) > 0 and join_list.find(data_item['from']) > -1:
                            str_reg_ex_pattern = '\\b' + data_item['to'] + '\\b'
                            rg = re.compile(str_reg_ex_pattern)
                            count = len(rg.findall(join_list))
                            data_item['weight'] += count

                data_list.append(data_item)
        return data_list

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
