import scrapy

from posts.items import PostsItem

class PostSpider(scrapy.Spider):
    name = "post"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverflow.com/questions/"]

    def parse(self, response):
        for post in response.css('div.s-post-summary.js-post-summary'):
            item = PostsItem()
            #check to see if tag we want exists for the question
            tagline = post.css('ul.ml0 list-ls-none js-post-tag-list-wrapper d-inline')
            # if the tagline exists
            if tagline is not None:
                #grab the tags
                tags = post.css('li.d-inline.mr4.js-post-tag-list-item')
                for tag in tags:
                    #check to see if that tags are ones we want
                    #check to see if tag is java
                    if tag.css('a.s-tag.post-tag.flex--item.mt0.js-tagname-java'):
                        item["tagtype"] = tag.css('a.s-tag.post-tag.flex--item.mt0.js-tagname-java::text').get()
                        item["title"] = post.css('a.s-link::text').get() 
                        yield item
                    elif tag.css('a.s-tag.post-tag.flex--item.mt0.js-tagname-cçç'):
                        #check to see if tag is c++
                        item["tagtype"] = tag.css('a.s-tag.post-tag.flex--item.mt0.js-tagname-cçç::text').get()
                        item["title"] = post.css('a.s-link::text').get()
                        yield item
                    else:
                        break
            else:
                item["tagtype"] = "cannot find tagline"
                item["title"] = "cannot find title"
                yield item

                        
            
           
            
       
