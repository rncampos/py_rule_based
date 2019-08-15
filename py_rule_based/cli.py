from py_rule_based import py_rule_based

def dates():
    import sys
    arg = []
    for i in range(len(sys.argv)):
        opt = sys.argv[i].lower()
        arg.append(opt)
    t = '''
Usage_examples (make sure that the input parameters are within quotes):

  Default Parameters: py_rule_based -t "2011 Haiti Earthquake Anniversary." 
    
  All the Parameters: py_rule_based -t "2011 Haiti Earthquake Anniversary." -dg "year" -bd "2000" -ed "2015"
    
  Output: the output will be a list of temporal expressions (TE) in the format [(normalized TE; TE as it is found in the text),….] or an empty list [] if no temporal expression is found in the text.

Options:
  [required]: either specify a text or an input_file path.
  ----------------------------------------------------------------------------------------------------------------------------------
  -t, --text TEXT                       Input text.
                                        Example: “2011 Haiti Earthquake Anniversary.”.

  -i, --input_file TEXT                 Text path.
                                        Example: “C:\\text.txt


  [not required]
  -----------------------------------------------------------------------------------------------------------------------------------
  -dg, --date_granularity TEXT          Date granularity
                                        Default: "full"
                                        Options:
                                                "full" - (means that all types of granularity will be retrieved, from the coarsest to the finest-granularity).
                                                "day" - (means that for the date YYYY-MM-DD-HH:MM:SS it will retrieve YYYY-MM-DD).
                                                "month" (means that for the date YYYY-MM-DD-HH:MM:SS only the YYYY-MM will be retrieved);
                                                "year" (means that for the date YYYY-MM-DD-HH:MM:SS only the YYYY will be retrieved);

  -bd, --begin_date TEXT                begin date.
                                        Options:
                                                any integer > 0
                                            
  -ed, --end_date TEXT                  begin date.
                                        Options:
                                                any integer > 0


  --help                                Show this message and exit.
    '''

    def run_py_rule_based(text):
        date_granularity = get_arguments_values(arg, '-dg', '--date_granularity', 'full')
        begin_date = get_arguments_values(arg, '-bd', '--begin_date', 0)
        end_date = get_arguments_values(arg, '-ed', '--end_date', 2100)

        try:
            begin_date = int(begin_date)
        except:
            print('Please specify a number for begin_date between 0 and 2100.')
            return {}
        try:
            end_date = int(end_date)
        except:
            print('Please specify a number for begin_date between 0 and 2100.')
            return {}

        result = py_rule_based(text, date_granularity, begin_date, end_date)
        print(result)

    if '--help' in arg:
        print(t)
        exit(1)

    # make sure if was input text arugument
    elif '-t' in arg or '--text' in arg:
        position = verify_argument_pos(arg, '-t', '--text')
        text = arg[position+1]
    elif '-i' in arg or '--input_file' in arg:
        position = verify_argument_pos(arg, '-i', '--input_file')
        path = arg[position+1]

        try:
            file = open(path)
            text = file.read()
        except:

            print('''Sorry something went wrong while reading from this file.
Make sure that is a txt file and check his format.
            ''')
            exit(1)
    else:
        print('Bad arguments [--help]')
        exit(1)
    run_py_rule_based(text)


def get_arguments_values(arg_list, argument, extense_argument, defaut_value):
    value = ''
    try:
        try:
            position = arg_list.index(argument)
        except:
            position = arg_list.index(extense_argument)

        if argument in arg_list or extense_argument in arg_list:
            value = arg_list[position + 1]
    except:
        value = defaut_value
    return str(value)


def verify_argument_pos(arg_list, argument, extense_argument):
    try:
        position = arg_list.index(argument)
    except:
        position = arg_list.index(extense_argument)
    return position


if __name__ == "__main__":
    dates()
