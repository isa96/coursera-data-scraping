import scrapy
import pandas as pd
    
class coursera_data(scrapy.Spider):
    
    name = "coursera_data" #this name must be unique within the project
    
    def __init__(self, course, page, **kwargs):
        super(coursera_data, self).__init__(**kwargs)
        self.course = course
        self.page = int(page)
        
    def start_requests(self):
        #create course path so we can use it into query string in coursera
        course_format = self.course.replace(" ", "+")
        
        for index in range(self.page):
            url = f"https://www.coursera.org/search?query={course_format}&page={index+1}"

            yield scrapy.Request(url = url, callback=self.parse)
            
    def parse(self, response):
        
        course_title = response.xpath('//h3[@class="cds-119 cds-CommonCard-title css-e7lgfl cds-121"]//text()').extract()
        course_by= response.xpath('//p[@class="cds-119 cds-ProductCard-partnerNames css-dmxkm1 cds-121"]//text()').extract()
        course_link = response.xpath('//a[@class="cds-119 cds-113 cds-115 cds-CommonCard-titleLink css-1smvlxt cds-142"]/@href').extract()
        
        clean_coursera_urls = []
        for course_url in course_link:
            clean_format = f"https://www.coursera.org{course_url}"
            clean_coursera_urls.append(clean_format)
        
        skills_you_gain = response.xpath('//div[@class="cds-CommonCard-bodyContent"]/p[@class="cds-119 css-dmxkm1 cds-121"]/text()').extract() 
        course_ratings = response.xpath('//div[@class="product-reviews css-pn23ng"]/p[@class="cds-119 css-11uuo4b cds-121"]/text()').extract()
        course_reviews = response.xpath('//div[@class="product-reviews css-pn23ng"]/p[@class="cds-119 css-dmxkm1 cds-121"]/text()').extract()
        course_levels = response.xpath('//div[@class="cds-CommonCard-metadata"]/p[@class="cds-119 css-dmxkm1 cds-121"]/text()').extract()
        
        data = {
            "course_title":  course_title,
            "course_by": course_by,
            "course_link":clean_coursera_urls,
            "skills_you_gain": skills_you_gain,
            "course_ratings": course_ratings,
            "course_reviews": course_reviews,
            "course_level": course_levels
        }
        
        if len(course_title) > 0 :  
            # Append data to "output.csv"
            first_df = pd.read_csv("output.csv")
            new_df = pd.DataFrame(data)
            
            pd.concat([first_df, new_df]).to_csv('output.csv', index=False)
        else:
            pass
                
        self.logger.info(data)
        
        yield data
    