"""
This script will take the json file provided by HackerRank under
"Export Data" at https://www.hackerrank.com/settings/account and
produce a directory tree of the highest scoring solutions for
each challenge sorted by Contest, Language, and Challenge.

To use this script simply download the json file, rename it to
'data.json' and run the script. The solutions will be duplicated
in each root folder so you can use one or all of the sortings. 

I created this as a means to upload my own work from HackerRank
to github. Unfortunately HackerRank does not provide the
challenge description or a link to the description in the
aforementioned json file, so there is no way to provide the
context for each solution.
"""

import json, os
from collections import defaultdict

extensions = {'javascript':'.js',
              'php':'.php',
              'cpp':'.cpp',
              'perl':'.pl',
              'python':'.py',
              'python3':'.py',
              'pypy':'.py',
              'ruby':'.rb'}

windowsforbidden = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']

submissions = {'By Contest':defaultdict(dict),
               'By Language':defaultdict(dict),
               'By Challenge':defaultdict(dict)}

with open('data.json', 'r') as infile:
    data = json.load(infile)
    for d in data['submissions']:
        if not submissions['By Contest'][d['contest']]:
            submissions['By Contest'][d['contest']] = defaultdict(list)
        submissions['By Contest'][d['contest']][d['challenge']].append({'code':d['code'],
                                                                      'score':d['score'],
                                                                      'language':d['language']})

        if not submissions['By Language'][d['language']]:
            submissions['By Language'][d['language']] = defaultdict(list)
        submissions['By Language'][d['language']][d['challenge']].append({'code':d['code'],
                                                                        'score':d['score'],
                                                                        'language':d['language']})

        if not submissions['By Challenge'][d['challenge']]:
            submissions['By Challenge'][d['challenge']] = defaultdict(list)
        submissions['By Challenge'][d['challenge']][d['language']].append({'code':d['code'],
                                                                         'score':d['score'],
                                                                         'language':d['language']})


for root in submissions.keys():
    for k1 in submissions[root].keys():
        for k2 in submissions[root][k1].keys():
            best = sorted(submissions[root][k1][k2], key=lambda k: float(k['score']))[-1]

            language = best['language']

            if language == '["html", "js", "css"]':
                # for whatever reason the json from HackerRank does not contain
                # the actual code for these submissions
                continue

            if language == 'text':
                # theres no point in keeping these
                continue

            if best['score'] == 0:
                # these are not solutions
                continue
            
            k1 = ''.join(c for c in k1 if not c in windowsforbidden)
            k2 = ''.join(c for c in k2 if not c in windowsforbidden)
            
            fullname = os.path.join(os.getcwd(),
                                    root,
                                    k1.strip(),
                                    k2.strip(),
                                    'solution' + extensions[language])
            
            os.makedirs(os.path.dirname(fullname), exist_ok=True)
            
            with open(fullname, 'w') as outfile:
                outfile.write(best['code'])
