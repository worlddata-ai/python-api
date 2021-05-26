def test_time_series(world_data):
    time_series = world_data.time_series(sector='MACROECONOMICS, FINANCE', sub_sector='GLOBAL ECONOMIC MONITOR',
                                         super_region='GLOBAL DATA', source='WORLD BANK', trend_ids=[
            'NTEyNzExMzUyMzc0MzQ2MDIxJCRDRENfTkVXJCRjZGMyNDFfVjJfREFUQV9WQUxVRQ=='])
    return time_series
