# vax_apt_alerter
Covid Vaccine Appointment Alerter - checks vaccinespotter.org and uses twilio to text you if an appointment is available near you

N.B. doesn't notify you of currently available appointments, only changes. There's no point running this if you check https://www.vaccinespotter.org and see there are already appointments available for you
# Installation instructions

1. `git clone https://github.com/MarvinT/vax_apt_alerter.git`
2. `cd vax_apt_alerter`
3. `pip install -r requirements.txt`
4. set up your [twilio](www.twilio.com) account, get a twilio phone number
5. open main.py in favorite editor and update all parameters
6. `python main.py`
