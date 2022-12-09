def add_rank(first_data, second_data, left_on, right_on, way_or_home):
    first_data = first_data.merge(second_data,
                                  left_on=left_on,
                                  right_on=right_on,
                                  how='left').rename(columns={
                                    'rank' : f'{way_or_home}_rank',
                                    'total_points' : f'{way_or_home}_ranking_points'
                                  })
    return first_data