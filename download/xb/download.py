from html.parser import HTMLParser
from urllib.request import Request, urlopen
from .models import Thread, Image
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/<int:thread>/<int:start_page>/<int:end_page>')
# def parse(thread, start_page=None, end_page=None):
#     img_list = get_image_list(thread, start_page, end_page)
#     return render_template('page.html', list=img_list)

url = 'https://xossip.com/printthread.php?t={0}&page={1}'

def update_images(thread):
    if thread and thread.in_progress is not None:
        thread.in_progress = True
        thread.save()
        img_urls = get_image_list(thread.thread_id, thread.start_page, thread.end_page)
        for img_url in img_urls:
            Image(thread=thread, image_url=img_url).save()
        thread.in_progress = False
        thread.save()

def get_image_list(thread, start_page, end_page):
    img_urls = []
    for page in range(start_page, end_page + 1):
        img_urls += _get_image_from_page(url.format(thread, page))
    return _formatify_image_urls(img_urls)

def _get_image_from_page(url):
    print('Parsing {0}'.format(url))
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(request)
    parser = XBParser()
    parser.feed(response.read().decode('utf-8'))
    return parser.get_images()

def _formatify_image_urls(img_urls):
    return list(set(img_urls))



class XBParser(HTMLParser):
    img_urls = []
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for k, v in attrs:
                if 'src' in k and 'pzy.be' in v:
                    self.img_urls.append(v.replace('/v/','/i/').replace('/t/','/i/'))
                    break
  
    def get_images(self):
        return self.img_urls