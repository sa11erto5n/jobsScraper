from scraper import jobsScraper
import random
if __name__ == "__main__" :
    while True :
        jobScraper  = jobsScraper()
        print("available jobs categories".capitalize() )
        print("______________________________________")
        # getiing jobs categories and show them to user and making them an indexed list
        jobs_categories = jobScraper.get_categories()
        keys = list( jobs_categories.keys() )
        for key_index,key in enumerate(keys) : 
            print(f"[{key_index}] - {key} |")
        print("_________________________________")
        # get the index of user's choice
        desired_category_index = int(input("Now Select A Category to fetch its jobs : " ))
        print("_____________________________________")
        # if the chosen index is in the list this will print the available jobs
        try :
            jobs_list =  jobScraper.get_jobs_list( jobs_categories[keys[desired_category_index]] ) 
            print( f"jobs of {keys[desired_category_index]}".capitalize() )
            print("_____________________________")
            for job in jobs_list :
                for key,value in job.items() :
                    print(f"{key} : {value}")
                print("_________________________________")
        except Exception as e :
            print(str(e))
        # Ask the user if they want to re-run the script
        user_input = input("Do you want to re-run the script? (yes/no): ")
        if user_input.lower() != "yes":
            break
    