def test_advance_search(world_data):
    search_result = world_data.advance_search(search_text='india', sector='MACROECONOMICS, FINANCE',
                                              sub_sector='GLOBAL ECONOMIC MONITOR',
                                              super_region='GLOBAL DATA', source='WORLD BANK', size=10, offset=0)
    return search_result


def test_advance_search_attributes(world_data):
    attributes = world_data.advance_search_attributes(search_text='india', sector='MACROECONOMICS, FINANCE',
                                                      sub_sector='GLOBAL ECONOMIC MONITOR',
                                                      super_region='GLOBAL DATA', source='WORLD BANK', attributes=[])
    return attributes


def test_news_search(world_data):
    attributes = world_data.news_search(search_text='corn india', size=10, offset=0)
    return attributes

