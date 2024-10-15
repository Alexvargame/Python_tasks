import importlib
import importlib.abc
import sys
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from html.parser import HTMLParser

import logging
log=logging.getLogger(__name__)


def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))
    links = set()
    try:
        log.debug('Getting links from %s' % url)
        u = urlopen(url)
        parser = LinkParser()
        parser.feed(u.read().decode('utf-8'))
    except Exception as e:
        log.debug('Could not get links. %s', e)
    log.debug('links: %r', links)
    return links

class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links = { }
        self._loaders = { baseurl : UrlModuleLoader(baseurl) }
    def find_module(self, fullname, path=None):
        log.debug('find_module: fullname=%r, path=%r', fullname, path)
        if path is None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]
        parts = fullname.split('.')
        basename = parts[-1]
        log.debug('find_module: baseurl=%r, basename=%r', baseurl, basename)
     # Проверка кеша ссылок
        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)
         # Проверка того, что это не пакет
        if basename in self._links[baseurl]:
            log.debug('find_module: trying package %r', fullname)
            fullurl = self._baseurl + '/' + basename
             # Попытка загрузить пакет (которая обращается к __init__.py)
            loader = UrlPackageLoader(fullurl)
            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug('find_module: package %r loaded', fullname)
            except ImportError as e:
                log.debug('find_module: package failed. %s', e)
                loader = None
            return loader
         # Обычный модуль
        filename = basename + '.py'
        if filename in self._links[baseurl]:
            log.debug('find_module: module %r found', fullname)
            return self._loaders[baseurl]
        else:
            log.debug('find_module: module %r not found', fullname)
            return None

    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links.clear()





# Загрузчик модуля из URL
class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}
    def module_repr(self, module):
        return '<urlmodule %r from %r>' % (module.__name__, module.__file__)
    # Требуемый метод
##    def load_module(self, fullname):
##        code = self.get_code(fullname)
##        mod = sys.modules.setdefault(fullname, imp.new_module(fullname))
##        mod.__file__ = self.get_filename(fullname)
##        mod.__loader__ = self
##        mod.__package__ = fullname.rpartition('.')[0]
##        exec(code, mod.__dict__)
##        return mod
    def load_module(self, fullname):
        ptint(fullname)
        u = urllib.request.urlopen(fullname)
        source = u.read().decode('utf-8')
        name=url.split('/')[-1].split('.')[0]
        print(name)
        mod = importlib.util.module_from_spec(importlib.util.find_spec(name))
        code = self.get_code(fullname)
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]
        exec(code, mod.__dict__)
        return mod
    # Необязательные расширения
    def get_code(self, fullname):
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), 'exec')
    def get_data(self, path):
        pass
    def get_filename(self, fullname):
        return self._baseurl + '/' + fullname.split('.')[-1] + '.py'
    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        log.debug('loader: reading %r', filename)
        if filename in self._source_cache:
            log.debug('loader: cached %r', filename)
            return self._source_cache[filename]
        try:
            u = urlopen(filename)
            source = u.read().decode('utf-8')
            log.debug('loader: %r loaded', filename)
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug('loader: %r failed. %s', filename, e)
            raise ImportError("Can't load %s" % filename)
    def is_package(self, fullname):
        return False
# Загрузчик пакета из URL
class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [ self._baseurl ]
        mod.__package__ = fullname
    def get_filename(self, fullname):
        return self._baseurl + '/' + '__init__.py'
    def is_package(self, fullname):
        return True
    # Вспомогательные функции для инсталляции/деинсталляции загрузчика
    _installed_meta_cache = { }
    def install_meta(address):
        if address not in _installed_meta_cache:
            finder = UrlMetaFinder(address)
            _installed_meta_cache[address] = finder
            sys.meta_path.append(finder)
            log.debug('%r installed on sys.meta_path', finder)
    def remove_meta(address):
        if address in _installed_meta_cache:
            finder = _installed_meta_cache.pop(address)
            sys.meta_path.remove(finder)
            log.debug('%r removed from sys.meta_path', finder)





import fib
print(fib.fib(10))
import spam
import grok.__init__

##def load_module(url):
##    u = urllib.request.urlopen(url)
##    source = u.read().decode('utf-8')
##    name=url.split('/')[-1].split('.')[0]
##    print(name)
##    mod = importlib.util.module_from_spec(importlib.util.find_spec(name))
##    code = compile(source, url, 'exec')
##    mod.__file__ = url
##    mod.__package__ = ''
##    exec(code, mod.__dict__)
##    return mod
##fib = load_module('http://localhost:15000/fib.py')
##print(fib.fib(10))
##print(fib)
