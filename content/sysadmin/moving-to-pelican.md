Date: 2013-04-22
Title: Moving to Pelican
slug: moving-to-pelican
tags: blogging, pelican

# If it ain't broke... fix it
For some time now I have been meaning to do something about my blog. I wasn't sure what it is that I wanted to do, however, something needed to be done. It was an unmaintained atrocity and needed to be taken behind the barn. Today, as it turns out, was that day. I did my research prior to today and decided that I was going to use pelican. I wanted a statically generated site, I love python, writing in markdown is a lot more fun than writing in the wordpress editor, templates are jinja2... I could go on and on about all of the pros. Long story short, wordpress is too much for me. I don't need a MySQL backend to write my thoughts down. So out it goes.

# How
Installing pelican was a breeze

    mkvirtualenv alexenko.com
    pip install pelican Markdown BeautifulSoup
    pelican-quickstart alexenko.com
    cd alexenko.com
    git init
    git remote add origin git@github.com:alexenko/alexenko.com.git

All that was left to do was import the old content from WordPress. I exported the site (under Tools > Export) and then re-imported it into pelican

    pelican-import -m markdown --wp-import alexenko.xml -o content

After editing the config file, you can find mine at https://github.com/alexenko/alexenko.com/blob/master/pelicanconf.py,

    make html && make serve

allowed me to view the site

	make publish
	make ssh_upload

BAM, done

# wrapup
Overall the process, after deciding which theme to use, took less than 1/2 hour. I spent way too long clicking at the different themes, trying to decide which one I could live with the longest.