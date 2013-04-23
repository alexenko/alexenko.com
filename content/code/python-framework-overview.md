Title: Python framework overview
Date: 2012-08-31 21:57
slug: python-framework-overview
Tags: framework, list, python, django

I initially chose Pyramid as the framework of choice for a webapp I'm
working on. I did some surveying prior to making the choice and settled
on Pyramid as it's the middle ground between a full-blown framework like
Django, and a minimal one like Flask/Bottle. However, after a lengthy
email discussion with Ari, I realized that my surveying of the framework
landscape wasn't quite good enough.

This is the first in a series of posts summarizing my research. A lot of
information was found on other sites and they were linked to where
possible.

Blatantly stolen from [Hacker News][]

[http://en.wikipedia.org/wiki/Pyramid\_%28web\_framework%29][]

### Pro

</p>

-   faster than Django
-   better quality (100% statement coverage via unit tests)
-   supports latest python (3.3 vs 2.7)
-   great documentation (including free up to date book). There's also a
    separate pyramid cookbook (debatable)
-   simplicity. If you just see a pyramid app, you can dive right in
    fairly easily without learning lots of alien stuff
-   sensible defaults, and you can choose to swap out parts easily if
    you want (templates, ORM, etc)
-   works well with other python software, doesn't bundle everything in,
    with NIH syndrome
-   great tools. like the web console that drops straight into a
    debugger when an exception happens on the page you're looking at
-   <span style="color: #000000;"> Powerful when it comes to fine
    grained security utilizing access control lists</span>
-   <span style="color: #000000;">Integrates really well with the major
    python libraries out there.</span>

</p>

### Con

</p>

-   It's complicated (point made by another comment, contrast to
    simplicity, probably learning curve)
-   It doesn't really do much for you (have to spend lots of
    effort/time/learning plumbing in all the 3rd party libs)
-   Lacks sensible defaults for many things
-   Documentation is rather lacking. Oh, there's tons of it, but it's
    rather maze-like and hard to use if you don't actually understand
    the system. High-level overview/cookbook type stuff is severely
    lacking.

</p>

Django
------

</p>

### Pros

</p>

-   Tonnes of documentation and examples available on the internet
-   Easy to [get started][]
-   Used by Instagram, Pinterest, OpenStack, Mozilla, Disqus and many
    many others
-   All in one package that does not need many 3rd party plugins/addons
    (ORM, templates, cache)

</p>

### Cons

</p>

-   Using packages like SQLAlchemy gets rid of the "djangoness" of
    Django
-   Designed for a newspaper model, pushing content, editing deadlines,
    doing something non-standard is much harder in Django

</p>

web2py
------

</p>
stolen from [Quora][]

### Pros

</p>

-   Web-based IDE/admin to create, manage, and edit apps and plugins,
    including database administration, code editing and debugging,
    doctests, versioning, error ticketing, bytecode compiling,
    packing/installing, an app creation wizard,
-   Easy Google App Engine deployment
-   jQuery integration and built-in AJAX support. (Note, web2py can be
    used with any Javascript framework. Use of jQuery is not required,
    though convenient for some functionality.).
-   Works on Google App Engine (GAE) out of the box (with code that is
    portable to other platforms).
-   Works with 10 database backends (in addition to GAE).
-   Powerful access control system. Every app can be both a provider and
    a client for CAS 2.0.
-   Easy web services and automatic RESTful API generation
-   Built-in scheduler for background tasks
    (http://web2py.com/books/default/...)

</p>

### Minor Pros (to me, YMMV)

</p>

-   Database abstraction layer (http://web2py.com/book/default/c...) --
    A bit closer to SQL (though doesn't require knowledge of SQL), and
    therefore somewhat more flexible and typically faster than an ORM.
-   Components (http://web2py.com/book/default/c...)
-   Plugins

</p>

More resources
--------------

</p>

-   [Web micro-framework BATTLE!][] -
    ...<span style="color: #000000;">he's mainly concerned with
    publishing existing python apps he's already written as simple web
    services, not writing a complete web site from scratch</span>...
-   [Pillars of Python: Six Python Web frameworks compared][]
-   [web2py feature comparison with other frameworks][] - Taken from
    web2py's website, biased :)
-   [Rewindy][] and [Rewindy tech stack][] and [discussion about it][]
-   [Pyramid vs Flask][]
-   [Django vs Pylons][]
-   [Top 10 JavaScript MVC frameworks][]

</p>

  [Hacker News]: http://hackerne.ws/item?id=3765610
  [http://en.wikipedia.org/wiki/Pyramid\_%28web\_framework%29]: http://en.wikipedia.org/wiki/Pyramid_%28web_framework%29
  [get started]: http://tech.yipit.com/2012/08/21/how-i-taught-myself-to-code-in-8-weeks/
  [Quora]: http://www.quora.com/What-are-the-advantages-of-web2py-over-Django/answer/Anthony-Bastardi
  [Web micro-framework BATTLE!]: http://www.slideshare.net/r1chardj0n3s/web-microframework-battle
  [Pillars of Python: Six Python Web frameworks compared]: http://www.infoworld.com/d/application-development/pillars-python-six-python-web-frameworks-compared-169442?page=0,0
  [web2py feature comparison with other frameworks]: http://www.web2py.com/examples/static/web2py_vs_others.pdf
  [Rewindy]: http://www.rewindy.com/
  [Rewindy tech stack]: http://www.mikkolehtinen.com/blog/2012/05/25/rewindy-tech-stack/
  [discussion about it]: http://news.ycombinator.com/item?id=4024923
  [Pyramid vs Flask]: http://news.ycombinator.com/item?id=4026913
  [Django vs Pylons]: http://stackoverflow.com/questions/48681/pros-cons-of-django-vs-pylons
  [Top 10 JavaScript MVC frameworks]: http://codebrief.com/2012/01/the-top-10-javascript-mvc-frameworks-reviewed/

