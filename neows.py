#!/usr/bin/python3
import requests
import time

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read().strip()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    userstartdate=input("Enter a start date (yyyy-mm-dd) [default=2019-11-11]" or "2019-11-11")
    startdate = (f"start_date=" + userstartdate)
    print(startdate)
    time.sleep(1)

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"
    userenddate=input("Optionally enter an end date (yyyy-mm-dd)").strip("/n")
    #if nothing entered then run without end date
    if not userenddate: 
        print ("Empty enddate" + userenddate)
        time.sleep(1)
        #make a request with the request library
        neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

        # strip off json attachment from our response
        neodata = neowrequest.json()

        ## display NASAs NEOW data
        print(neodata)

    #Print with end date value
    else: 
       enddate = (f"end_date=" + userenddate)
       print(enddate)
       time.sleep(1)

       # make a request with the request library
       neowrequest = requests.get(NEOURL + startdate + enddate + "&" + nasacreds)

       # strip off json attachment from our response
       neodata = neowrequest.json()

       ## display NASAs NEOW data
       print(neodata)

if __name__ == "__main__":
    main()

