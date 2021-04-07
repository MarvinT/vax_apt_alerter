import requests
from geopy.distance import distance
import time
from twilio.rest import Client


### PARAMETERS ###
# Home location, where to measure distance from
# can use https://www.latlong.net/convert-address-to-lat-long.html
longitude = -75.2
latitude = 39.9
# STATE, only looks for appointments from this state
state = "PA"
# Radius from home location, in miles
radius = 5
# Your Account SID from twilio.com/console
account_sid = "AC110f25ea406fe1a688ada3e935e5ab8f"
# Your Auth Token from twilio.com/console
auth_token = "your_auth_token"

your_phone_num = "+15558675309"
twilio_phone_num = "+15017250604"
send_initial_twilio_msg = True
##################


def main():
    home = (latitude, longitude)
    client = Client(account_sid, auth_token)
    current_ids = []
    prev_ids = []
    i = 0
    if send_initial_twilio_msg:
        message = client.messages.create(
            body="vax_apt_alerter running and twilio correctly configured",
            from_=twilio_phone_num,
            to=your_phone_num,
        )

    while True:
        data = requests.get(
            f"https://www.vaccinespotter.org/api/v0/states/{state}.json"
        ).json()
        print("counter:", i)
        for feature in data["features"]:
            if feature["properties"]["appointments_available"]:
                loc = feature["geometry"]["coordinates"][::-1]
                dist = distance(home, loc).miles
                if dist < radius:
                    print(dist, "miles")
                    print(feature)
                    current_ids.append(feature["properties"]["id"])
                    if i >= 1 and feature["properties"]["id"] not in prev_ids:
                        print("change detected")
                        msg = f"apt found. {dist} miles away. {feature['properties']['id']}. {feature['properties']['name']}. {feature['properties']['address']}"
                        print(msg)
                        message = client.messages.create(
                            body=msg, from_=twilio_phone_num, to=your_phone_num
                        )
        prev_ids, current_ids = current_ids, []
        i += 1
        time.sleep(15)  # sleep 15 seconds


if __name__ == "__main__":
    main()
