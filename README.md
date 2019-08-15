

    # py_rule_based
py_rule_based is a python wrapper that use a self-defined rule-based approach in regex which is able to detect the following patterns:

   - yyyy(./-)mm(./-)dd
   - dd(./-)mm(./-)yyyy
   - yyyy(./-)yyyy
   - yyyys
   - yyyy

This wrapper has been developed by Jorge Mendes under the supervision of [Professor Ricardo Campos](http://www.ccc.ipt.pt/~ricardo/) in the scope of the Final Project of the Computer Science degree at the [Polytechnic Institute of Tomar](http://portal2.ipt.pt/), Portugal.

Our aim for this package was six-fold:

 - To provide a multi-platform (windows, Linux, Mac Os);
 - To make it user-friendly not only in terms of installation but also in its usage;
 - To make it lightweight without compromising its behavior;
 - To give the user the chance to choose the granularity (e.g., year, month, etc) of the dates to be extracted;
 - To give the user the chance to choose the range of begin_date and end_date (e.g., begin_date=0, end_date=2100, etc);
 - To retrieve to the user a normalized version of the text (where each temporal expression is replaced by the normalized Heideltime version); and

## How to install py_rule_based

```bash
pip install git+https://github.com/JMendes1995/py_rule_based.git
```

## How to use py_rule_based
``` bash
from py_rule_based import py_rule_based

text = "The start of the war in Europe is generally held to be 1 September 1939,"\
        "beginning with the German invasion of Poland; the United Kingdom and France declared war on Germany two days later."\
        "The dates for the beginning of war in the Pacific include the start of the Second Sino-Japanese War on 7 July 1937,"\
        "or even the Japanese invasion of Manchuria on 19-09-1931."
```

#### _With the default parameters_
Default date_granularity is "full", begin_date is 0 and end_date is 2100 which means the range of dates that will be considered:

```` bash
results = py_rule_based(text)
````

or:

```` bash
results = py_rule_based(text, date_granularity='full', begin_date=2000, end_date=2100)
````
is exactly the same thing and produces the same results.

###### Output
The output will be a list of 4 elements or an empty list [] if no temporal expression is found in the text. The four elements are:

- a list of tuples with two positions (e.g., ('2011-01-02', '2011-01-02')). The first one is the detected temporal expression normalized by heideltime. The second is the temporal expression as it was found in the text;
- a normalized version of the text, where each temporal expression is replaced by its original date format;
- the execution time of the algorithm, divided into `rule_based_processing` (i.e., the time spent by the rule_based algorithm in extracting temporal expressions) and `text_normalization` (the time spent by the program in labelling the temporal expressions found in the text with a tag <d>).

```` bash
TempExpressions = results[0]
TempExpressions
````
```` bash
[('1939', '1939'), ('1937', '1937'), ('19-09-1931', '19-09-1931')]
````

```` bash
TextNormalized = results[1]
TextNormalized
````
```` bash
'The start of the war in Europe is generally held to be 1 September <d>1939</d>,beginning with the German invasion of Poland; the United Kingdom and France declared war on Germany two days later.The dates for the beginning of war in the Pacific include the start of the Second Sino-Japanese War on 7 July <d>1937</d>,or even the Japanese invasion of Manchuria on 19 September <d>1931</d>.'
````

```` bash
ExecutionTime = results[3]
ExecutionTime
````
```` bash
{'rule_based_processing': 0.000993490219116211, 'rule_based_text_normalization': 0}
````

#### _Optional parameters_
Besides running py_rule_based with the default parameters, users can also specify more advanced options. These are:
- `date granularity`: <b>"full"</b> (Highest possible granularity detected will be retrieved); <b>"year"</b> (YYYY will be retrieved); <b>"month"</b> (YYYY-MM will be retrieved); <b>"day"</b> (YYYY-MM-DD will be retrieved)
- `begin_date` <b>0</b> (Defines the minimum value of date to be considered)
- `end_date` <b>2100</b> (Defines the maximum value of date to be considered)

```` bash
result = py_rule_based(text, date_granularity='year', begin_date=0, end_date=2100)
````

###### Output
The output follows the same patterns as described above.


```` bash
TempExpressions = results[0]
TempExpressions
````
```` bash
[('1939', '1939'), ('1937', '1937'), ('1931', '19-09-1931')]
````

```` bash
TextNormalized = results[1]
TextNormalized
````
```` bash
'The start of the war in Europe is generally held to be 1 September <d>1939</d>,beginning with the German invasion of Poland; the United Kingdom and France declared war on Germany two days later.The dates for the beginning of war in the Pacific include the start of the Second Sino-Japanese War on 7 July <d>1937</d>,or even the Japanese invasion of Manchuria on <d>1931</d>.'
````

```` bash
ExecutionTime = results[3]
ExecutionTime
````
```` bash
{'rule_based_processing': 0.0, 'rule_based_text_normalization': 0.0}
````

### Python CLI (Command Line Interface)
#### Help
``` bash
py_heideltime --help
```
#### Usage Examples
Make sure that the input parameters are within quotes.

Default Parameters:
``` bash
py_rule_based -t "2011 Haiti Earthquake Anniversary." 
```

All the Parameters:
``` bash
py_rule_based -t "2011 Haiti Earthquake Anniversary." -dg "year" -bd "2000" -ed "2015"
```

#### Options
``` bash
  [required]: either specify a text or an input_file path.
  ----------------------------------------------------------------------------------------------------------------------------------
  -t, --text TEXT                       Input text.
                                        Example: “2011 Haiti Earthquake Anniversary.”.

  -i, --input_file TEXT                 Text path.
                                        Example: “C:\\text.txt

```

``` bash
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
                                                
  --help                           - Show this message and exit.

```

Please check [Time-Matters](https://github.com/LIAAD/Time-Matters) if you are interested in detecting the relevance (score) of dates in a text.
