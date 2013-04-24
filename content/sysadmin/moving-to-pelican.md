Date: 2013-04-22
Title: Moving to Pelican
slug: moving-to-pelican
status: draft

# Moving to Pelican
## Describe why you're moving to pelican
For some time now I have been meaning to do something about my blog. I wasn't sure what it is that I wanted to do, however, something needed to be done. It was an atrocity that needed to be wiped off the internet. Today, as it turns out, it was that day. I did my research prior to today and decided that I was going to use pelican. I wanted a statically generated site, I love python, writing in markdown is a lot more fun than writing in the wordpress editor, templates are jinja2... The amount of benefits I could list at this point is huge. Long story short, wordpress is too much for me. I don't need a MySQL backend to write my thoughts down. So out it goes.
I initially decided to replace my blog at the beginning of this year. However, things kept getting in the way and I wasn't sure I wanted to use pelican. Maybe it was too complicated?

## short process of moving
Today, I decided to change the blog.
Installing pelican was a breeze

    mkvirtualenv alexenko.com
    pip install pelican Markdown BeautifulSoup
    pelican-quickstart alexenko.com
    git clone TK

All that was left to do was import the old content from WordPress. I exported the site (under Tools > Export) and then re-imported it into pelican
    pelican-import -m markdown --wp-import alexenko.xml -o content
BAM, done

After editing the config file, you can find mine at TK,

    make html && make serve

allowed me to view the site

    make publish
    make ssh_upload

BAM, done

## summary of events
Overall the process, after deciding which theme to use, took less than 1/2 hour. I spent way too long clicking at the different themes, trying to decide which one I could live with the longest.