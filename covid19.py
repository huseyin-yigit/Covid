from covid import Covid

def getCovid(country):
    covid = Covid()
    return covid.get_status_by_country_name(country)
    
        
        