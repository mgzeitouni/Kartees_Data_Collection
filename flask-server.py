# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
from flask import Flask, request, jsonify
import json
from scripts.stubhub import Stubhub
from scripts.stubhub import *
from scripts.aws_consolidate import *
import pdb
import subprocess
import logging
import threading
from scripts.cron_functions import *
from scripts.price_through_time import *
import time
# from xml import etree
# import xmltodict

logging.basicConfig()


from flask_apscheduler import APScheduler

if 'VCAP_SERVICES' not in os.environ:
	print('Running on Local')
	from scripts.credentials import *
	aws_id = AWS_ACCESS_KEY_ID
	aws_key=AWS_SECRET_ACCESS_KEY
else:
	print ('Running on Bluemix')
	aws_id = os.getenv('AWS_ACCESS_KEY_ID')
	aws_key=os.getenv('AWS_SECRET_ACCESS_KEY')

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
global accounts
global limit_per_minute

limit_per_minute = 2

accounts = {"get_event":{"MO":[],"LABO":[]} ,
			"get_event_inventory":{"MO":[],"LABO":[]} }

string1 = 'export AWS_ACCESS_KEY_ID=%s' %aws_id
string2 = 'export AWS_SECRET_ACCESS_KEY=%s' %aws_key
#string = 'echo "[default]\naws_access_key_id=%s\naws_secret_access_key=%s">~/.aws/credentials' %(aws_id.strip(),aws_key.strip())

#subprocess.Popen(string, shell=True)
subprocess.Popen(string1, shell=True)
subprocess.Popen(string2, shell=True)

stubhub = Stubhub(account="LABO")

cron = {"LABO" :{"time": time.time(), "number": 1},
		"MO":{"time": time.time(), "number": 1}}



if 'VCAP_SERVICES' in os.environ:

    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)

else:

	client = Cloudant(CLOUDANT['username'], CLOUDANT['password'], url=CLOUDANT['url'],connect=True,auto_renew=True)


#cron_LABO = {'current':1, 1:'NA', 2:'NA', 3:'NA', 4: 'NA', 5:'NA', 6:'NA', 7:'NA', 8:'NA', 9:'NA', 10:'NA'}


def construct_error(code, message):
	return json.dumps({"Error_Code": "%d" %code, "Error_Message": "%s" %message})

def error_1(param):
	return construct_error(1, "Missing required parameter '%s'" %param)

def error_2(param):
	return construct_error(2, "Unsuccessful call to StubHub - Invalid %s" %param)

def stubhub_session(account):

	stubhub = Stubhub(account=account)

	return stubhub


@app.route('/getevent', methods = ['GET'])
def getevent():

	# First check if eventId was passed in
	if request.args.get('eventId'):

		event_id = request.args.get('eventId')

		# Call stubhub
		stubhub_response = stubhub.get_event(event_id)

		# If nothing returned, send back error message
		if str(stubhub_response) == '<Response [200]>':

			response = stubhub_response.text

		else:

			response = error_2('eventId')

	else:
		response = error_1('eventId')

	return response

@app.route('/geteventinventory', methods = ['GET'])
def geteventinventory():

	# First check if eventId was passed in
	if request.args.get('eventId'):

		event_id = request.args.get('eventId')

		# Call stubhub
		stubhub_response = stubhub.get_event_inventory(event_id)

		# If nothing returned, send back error message
		if stubhub_response['eventId'] != 'None' and stubhub_response['eventId']  != None:

			response = json.dumps(stubhub_response)

		else:

			response = error_2('eventId')

	else:
		response = error_1('eventId')

	return response

@app.route('/postlisting', methods = ['POST'])
def postlisting():

	required = ['account', 'eventId','quantity','section','row', 'price']
	
	#params =  request.form["myvar"]

	data = request.data

	dataDict = json.loads(data)
	
	missing_array = []

	response=None

	# First check if something is missing
	for param in required:
		if param not in dataDict:
			# Missing Param error
			missing_array.append(param)


	if missing_array:
		response = error_1(missing_array)

	else:
		stubhub = stubhub_session(dataDict['account'])

		response_dict = json.dumps(stubhub.create_listing(dataDict))

		if 'id' in response_dict:

			response = response_dict
			#response = {"Status":response_dict['status'], "Stubhub Listing Id": response_dict['id']}

		else:
			error_2('call')


	return response


@app.route('/getfirstprice', methods = ['GET'])
def getfirstprice():

	# First check that sectionId was passed in

	if request.args.get('sectionId'):

		section_id = request.args.get('sectionId')
		# Second, check if eventId was passed in
		if request.args.get('eventId'):

			event_id = request.args.get('eventId')

			# Call stubhub
			stubhub_response = stubhub.get_event_inventory(event_id)

			# If nothing returned, send back error message
			if stubhub_response['eventId'] != 'None' and stubhub_response['eventId']  != None:

				listings = stubhub_response

				min_buyer_price = 1000000.0
				listing_id = None

				# Loop to look for the cheapest
				for listing in listings['listing']:


					if listing['sectionName'] and listing['currentPrice']['amount'] and listing['quantity']:

						current_section_name = str(listing['sectionName'][-3:])
						current_price = float(listing['currentPrice']['amount'])
						current_quantity = int(listing['quantity'])

						if current_section_name== section_id and current_price < min_buyer_price and current_quantity > 1 :

							min_buyer_price = current_price
							listing_id = int(listing['listingId'])


				# Get details of other listing for the actual listing price
				min_listing_price = stubhub.get_other_listing(listing_id)['ListingResponse']['listing']['currentPrice']['amount']
				markup=10
				decision_price = '%.2f' %(min_listing_price * markup)

				response = json.dumps({"Section": section_id,
										"Event": event_id,
										"Cheapest Listing Price":min_listing_price,
										"price":decision_price})

			else:
				response = error_2('eventId')
		else:
			response = error_1('eventId')

	else:
		response = error_1('sectionId')

	return str(response)

@app.route('/reprice', methods = ['GET'])
def reprice():

	required = ['stubhublistingid', 'new_price']

	data = request.data

	dataDict = json.loads(data)
	
	missing_array = []

	response=None

	# First check if something is missing
	for param in required:
		if param not in dataDict:
			# Missing Param error
			missing_array.append(param)


	if missing_array:
		response = error_1(missing_array)

	else:
		stubhub = stubhub_session(dataDict['account'])

		response_dict = json.dumps(stubhub.change_price(stubhublistingid,new_price))

		if 'id' in response_dict:
			response = response_dict
		else:
			error_2('call')


	return response

@app.route('/weekly_consolidate', methods = ['GET'])
def weekly_consolidate():

	requests.get('https://stubhub-services-node-red-dev.mybluemix.net/flask_status')


	# if request and request.args.get('first_day') and request.args.get('last_day'):

	# 	print 'We have a request and params'
	# 	params = [request.args.get('first_day'),request.args.get('last_day')]

	# else:
	# 	print 'No params given, looking for last week of data'
	# 	params = [1,8]

	# threads = []
	# for i in range(4):
	# 	t = threading.Thread(target=worker, args=(i,))
	# 	t.start()


	return 'success'

@app.route('/remove_spaces', methods = ['GET'])
def remove_spaces_api():

	threads = []
	for i in range(1):
	    t = threading.Thread(target=worker, args=(i,))
	    threads.append(t)
	    t.start()

	return 'success'

@app.route('/get_data', methods = ['GET'])
def get_data():

	try:
		requests.get('https://stubhub-services-node-red-dev.mybluemix.net/flask-cron-running-status')

	except:
		print ('node red down')

	use_cron = ""

	resp = {"result":False,
			"data":[]}

	# with open('cron_test.csv', 'wb') as file:
	# 	writer = csv.writer(file)
	# 	writer.writerow(['hey'])


	try:

		account = request.args.get("account")
		stubhub = stubhub_session(account)

	    # Get game to use from second command line arg
		event_id = request.args.get("event_id")
		team = request.args.get("team")
		sport = request.args.get("sport")



		columns = update_event_data(stubhub,event_id, team, sport)

		resp["data"] = columns
		resp["result"] = True



	except Exception as e:

		 print ('problem')

	print(use_cron)

	return jsonify(resp)




def worker(schedule_type):


	aws_consolidate(client,1,4,schedule_type)

	return


@app.route('/thread', methods = ['GET'])
def test_cron():
	threads = []
	for i in range(5):
	    t = threading.Thread(target=worker, args=(i,))
	    threads.append(t)
	    t.start()

	return 'hi'




# class Config(object):

#         JOBS = [
#         {
#             'id': 'consolidate totals',
#             'func': collect_data,
#              'trigger': {
#         		'type': 'cron',
#         		'day_of_week': '*',
#         		'hour': '*',
#         		'minute': '0,30'
# 			}
#         }
#     ]


#     	SCHEDULER_API_ENABLED = True

#     	print "Current Time: %s" %datetime.datetime.now()


@app.route('/average',methods = ['POST'])
def average():

	data = eval(request.data)

	averages = {}

	for team in data:

		averages[team] = np.mean(data[team])

	return jsonify(averages)

@app.route('/std', methods = ['POST'])
def std():

	data = eval(request.data)

	stds = {}

	for team in data:

		stds[team] = np.std(data[team])

	return jsonify(stds)

@app.route('/login', methods = ['GET'])
def login():
	stubhub = Stubhub(account="LABO")
	event = stubhub.get_event(9710889)

	return event.text

def get_account(request):

	global accounts
	global limit_per_minute

	account_to_use = False

	waiting_for_resource = True

	while waiting_for_resource:

		timestamp = int(datetime.datetime.utcnow().strftime("%s")) * 1000

		for account in accounts[request]:
			if len(accounts[request][account])<limit_per_minute:
				accounts[request][account].append(timestamp)
				account_to_use = account
				waiting_for_resource = False
				break

			elif timestamp - accounts[request][account][0] > 60000:
				#print timestamp - accounts[request][account][0]
				account_to_use = account
				accounts[request][account] = []

				accounts[request][account].append(timestamp)
				waiting_for_resource = False
				break

			else:
				new_timestamp = int(datetime.datetime.utcnow().strftime("%s")) * 1000
				sleep_time = 60 - (new_timestamp-accounts[request][account][0])/1000
				print(sleep_time)
				# time.sleep(sleep_time)


	return account_to_use

def get_date_obj():

	date = datetime.datetime.utcnow()
	month = date.month
	day = date.day
	year = date.year
	readable = date.strftime('%m-%d-%y, %H:%M:%S %p')
	date_object = dict({"date_object":date, "month":month, "year":year, "day":day, "readable":readable})

	return date_object

def get_timestamp():

	return int(datetime.datetime.utcnow().strftime("%s")) * 1000

@app.route('/get_event_data',methods = ['GET'])
def get_event_data():

	account = request.args.get('account')
	data_type = request.args.get('dataType')
	event = request.args.get('eventId')

	try:
		stubhub = stubhub_session(account)
		
		try:
			if data_type == 'meta':
				event_data_object = stubhub.get_event(event)
				#event_data_object = eval(json.dumps(xmltodict.parse(event_data)))
			elif data_type == 'inventory':
				event_data_object = stubhub.get_event_inventory(event)
			else:
				response = jsonify({"message":"dataType must be either 'meta' or 'inventory'", "success":0})
				response.status_code = 400
				return response

			response = event_data_object

			response['current_timestamp'] = get_timestamp()
			response['current_date'] = get_date_obj()
			response['success']=1

			return jsonify(response)

		except:
			response = jsonify({"message":"Data Acquisition for %s unsuccesful" %eventId, "success":0})
			response.status_code = 400
			return response
	except:
		response = jsonify({"message":"Account %s unsuccesful login"%account, "success":0})
		response.status_code = 400
		return response

@app.route('/get_team_performance')
def get_team_performance():
	sport = request.args.get('sport')
	team = request.args.get('team')
	try:
		wins, losses, l_10 = espn.get_team_performance(sport, team)
		response = {"wins":wins,
		"losses":losses,
		"last_10":l_10}

		response['current_timestamp'] = get_timestamp()
		response['current_date'] = get_date_obj()

		return jsonify(response)

	except:
		response = jsonify({"message":"Performance data for %s unavailable" %team})
		response.status_code = 400
		return response



@app.route('/')
def Welcome():
    return "Hey there this is Kartees's python web server running on Bluemix. Time - %s" %datetime.datetime.now()

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

port = os.getenv('PORT', '5000')
if __name__ == "__main__":

	# app.config.from_object(Config())

	# scheduler = APScheduler()
	# scheduler.init_app(app)
	# scheduler.start()
	app.run(host='0.0.0.0', port=int(port))
