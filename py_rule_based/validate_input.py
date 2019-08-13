def verify_temporal_tagger(date_granularity, begin_date, end_date):
    if date_granularity != 'full' and date_granularity != 'day'and date_granularity != 'month' and date_granularity != 'year':
        print('Please specify a valid date_granularity.\n'
              'options:\n'
              '     full;\n'
              '     year;\n'
              '     month:\n'
              '     day;')
        return {}
    elif not isinstance(begin_date, int) or 0 > begin_date > 2100:
        print('Please specify a number for begin_date between 0 and 2100.')
        return {}
    elif not isinstance(end_date, int) or 0 > end_date > 2100:
        print('Please specify a number for end_date between 0 and 2100.')
        return {}
    elif begin_date > end_date:
        print('Please specify a number for begin_date lower than end_date.')
        return {}