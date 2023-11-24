from bs4 import BeautifulSoup as bs 
import requests 

class jobsScraper :
    def __init__(self ) :
        
        self.site_url = "https://www.sudancareers.com/job-vacancies-search-sudan"
        self.request_result = None
        self.request_content = None
        self.init()
    def init(self) :        
        # Configs 
        try :
            self.request_result = requests.get(self.site_url)
            self.request_content = bs(self.request_result.content , "html.parser")
            print("Site's GET request has beed finished successfully")
            print("_____________________________")
        except Exception as e :
            print(str(e))        

    def get_categories(self) :  # RETURN A LIST OF AVAILABLE JOBS CATEGORIES & THIER LINKS
        jobs_categories = self.request_content.find(attrs={"id" : "facetapi-facet-apachesolrsolr-block-im-field-offre-metiers"}).find_all("a")
        categories = {}
        for job_category in jobs_categories:
            category_name = job_category.find(string=True , recursive = False)
            category_url = job_category["href"]
            categories[category_name] = f"https://www.sudancareers.com{category_url}"
        return categories        
    def get_jobs_list(self , url : str) :
        category_url = url
        category_request_result = None
        category_request_content = None
        job_details = []
        
        try :
            category_request_result = requests.get(category_url)
            category_request_content = bs(category_request_result.content , "html.parser")
            print("Category site's GET request has beed finished successfully")
            print("_____________________________")
            jobs_list = category_request_content.find_all(attrs={"class" : "job-description-wrapper"} )
            for job in jobs_list :
                # job = job_details.fi(nd(attrs={"class" : "col-lg-5 col-md-5 col-sm-5 col-xs-12 job-title"})
                job_title = job.find("h5" , recursive = True).text
                job_date = job.find(attrs={"class" : "job-recruiter"}).find(string=True , recursive=False).replace("|" , "")
                job_recruiter = job.find(attrs={"class":"job-recruiter"}).find("b").text
                job_description = job.find(attrs={"class" : "search-description"}).text
                # region = job.find("p" , recursive=True).text
                job_tags = job.find(attrs={"class" : "job-tags"}).find_all(attrs={"class" : "badge"} )
                job_details.append(
                    {"job title" : job_title ,
                    "job date" : job_date ,
                    "job recuiter" : job_recruiter ,
                    "job description" : job_description ,
                    # "region" : region ,
                    "required skills" : [tag.text for tag in job_tags  ] ,
                     }
                )             
        except Exception as e :
            print(str(e))        
        return job_details