
import requests
import datetime
import json

POST_CODE = "411027"
age = 52

pinCodes = ["411027", "411045", "411033", "411057", "411017", "411067", "411061",\
             "411057", "411001", "411045", "410038", "411003", "411007", "411012",\
                 "411016", "411023", "411029", "411036", "411041", "411007", "411012"]

# Print details flag
print_flag = 'Y'

numdays = 30

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

count = 0

for pinCode in pinCodes:    
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pinCode, INP_DATE)
        response = requests.get(URL)
        if response.ok:
            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            flag = False
            if resp_json["centers"]:            
                if(print_flag=='y' or print_flag=='Y'):
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if ( session["min_age_limit"] <= age and session["available_capacity"] > 0 ) :
                                print(pinCode)
                                print("Available on: {}".format(INP_DATE))
                                print("\t", center["name"])
                                print("\t", center["block_name"])
                                print("\t Price: ", center["fee_type"])
                                print("\t Available Capacity: ", session["available_capacity"])
                                if(session["vaccine"] != ''):
                                    print("\t Vaccine: ", session["vaccine"])
                                print("\n")
                                count = count + 1
                            else:
                                b = 25
                                #print("No available slots on {}".format(INP_DATE))
            else:
                a = 25
                #print("No available slots on {}".format(INP_DATE))

if(count == 0):
    print("No Vaccination center avaliable.")
print("Completed...")