import os
import glob
import markdown2

DEBUG = False

template = open('template.html').read()
for fn in glob.glob('*.md'):
    contests = open(fn).read()
    title = contests.split('\n')[0]
    md = markdown2.markdown('\n'.join(contests.split('WriteUp')[0].split('\n')[1:]))
    if DEBUG:
        md = markdown2.markdown('\n'.join(contests.replace('WriteUp','---').split('\n')[1:]))
    print(fn, title, len(md))
    with open('./site/' + fn.replace('.md','.html'), 'w') as f:
        f.write(template.format(title=title, data=md))
