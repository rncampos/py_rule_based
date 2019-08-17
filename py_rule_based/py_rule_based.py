import re
import time
from py_rule_based.validate_input import verify_temporal_tagger


def py_rule_based(text, date_granularity='full', begin_date=0, end_date=2100):
    result = verify_temporal_tagger(date_granularity, begin_date, end_date)
    if result == {}:
        return []
    else:
        dates_result = date_extraction(text, date_granularity, begin_date, end_date)
        return dates_result


def date_extraction(text, date_granularity, begin_date, end_date):
    dates_list = []
    date_dictionary = {}
    TempExpressions = []
    ExecTimeDictionary = {}
    exec_time_text_labeling = 0

    text_tokens = text.split(' ')
    c = re.compile('\d{2}[-/.]\d{2}[-/.]\d{4}|\d{4}[-/.]\d{2}[-/.]\d{2}|\d{4}[-/.]\d{4}|\d{4}[-/.]\d{2}|\d{2}[-/.]\d{4} |\d{4}s|\d{4}')
    extractor_start_time = time.time()
    try:
        for tk in range(len(text_tokens)):
            if c.match(text_tokens[tk]):

                dt = c.findall(text_tokens[tk])
                results = list(map(int, re.findall('\d{4}', dt[0])))

                y = results
                for x in results:
                    if x > int(end_date) or x < int(begin_date):
                        y = []
                if not y:
                    pass
                else:
                    provisional_list = []

                    if dt[0] not in date_dictionary:
                        date_dictionary[dt[0]] = [dt[0]]
                    else:
                        date_dictionary[dt[0]].append(dt[0])

                    if date_granularity == 'full':
                        dates_list.append(dt[0])
                        text_tokens[tk] = text_tokens[tk].replace(dt[0], '<d>' + dt[0] + '</d>')
                        TempExpressions.append((dt[0], dt[0]))
                    elif date_granularity != 'full':
                        try:
                            if date_granularity.lower() == 'year':

                                dt, dates_list, provisional_list, \
                                date_dictionary,striped_text  = date_granularity_format(dt, dates_list, provisional_list, date_dictionary, '\d{4}', tk, TempExpressions)

                            elif date_granularity.lower() == 'month':

                                dt, dates_list, provisional_list, \
                                date_dictionary, striped_text = date_granularity_format(dt, dates_list, provisional_list, date_dictionary,'\d{2}[-/.]\d{4}|\d{4}[-/.]\d{2}', tk, TempExpressions)

                            elif date_granularity.lower() == 'day':

                                dt, dates_list, provisional_list, \
                                date_dictionary, striped_text = date_granularity_format(dt, dates_list, provisional_list, date_dictionary,'\d{2,4}[-/.]\d{2}[-/.]\d{2,4}', tk, TempExpressions)

                            labeling_start_time = time.time()
                            text_tokens[tk] = text_tokens[tk].replace(dt[0], '<d>'+provisional_list[0][1]+'</d>')
                            label_text_exec_time = (time.time() - labeling_start_time)
                            exec_time_text_labeling += label_text_exec_time
                        except:
                            pass
                    else:
                        labeling_start_time = time.time()
                        text_tokens[tk] = text_tokens[tk].replace(dt[0], '<d>' + dt[0] + '</d>')
                        label_text_exec_time = (time.time() - labeling_start_time)
                        exec_time_text_labeling += label_text_exec_time

        tt_exec_time = (time.time() - extractor_start_time)
        ExecTimeDictionary['rule_based_processing'] = tt_exec_time - exec_time_text_labeling
        ExecTimeDictionary['rule_based_text_normalization'] = exec_time_text_labeling
    except ValueError:
        pass

    new_text = ' '.join(text_tokens)
    return [TempExpressions, new_text, ExecTimeDictionary]


def date_granularity_format(dt, dates_list, provisional_list, date_dictionary, granularity_rule, text, TempExpressions):

    years = re.findall(granularity_rule, str(dt))
    dates_list.append((years[0]))
    provisional_list.append((dt, years[0]))

    if years[0] not in date_dictionary:
        date_dictionary[years[0]] = dt
    else:
        date_dictionary[years[0]].append(dt[0])

    TempExpressions.append((years[0], dt[0]))
    return dt, dates_list, provisional_list, date_dictionary, text