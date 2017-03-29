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
if 'VCAP_SERVICES' not in os.environ:
	print 'hey'
	from scripts.credentials import *
	aws_id = AWS_ACCESS_KEY_ID
	aws_key=AWS_SECRET_ACCESS_KEY
else:
	aws_id = os.getenv('AWS_ACCESS_KEY_ID')
	aws_key=os.getenv('AWS_SECRET_ACCESS_KEY')


app = Flask(__name__)


string = 'echo "[default]\naws_access_key_id=%s\naws_secret_access_key=%s">~/.aws/credentials' %(aws_id,aws_key)

subprocess.Popen(string, shell=True)


stubhub = Stubhub(account="LABO")

#parser = reqparse.RequestParser()

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/helloworld')

# class EventDate(Resource):
# 	def get(self):
# 		parser.add_argument('eventId', type=int, help='Get event data for this event Id')
# 		args = parser.parse_args()
# 		return args

# api.add_resource(EventDate, '/eventdata')

def construct_error(code, message):
	return json.dumps({"Error_Code": "%d" %code, "Error_Message": "%s" %message})

def error_1(param):
	return construct_error(1, "Missing required parameter '%s'" %param)

def error_2(param):
	return construct_error(2, "Unsuccessful call to StubHub - Invalid %s" %param)


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

	required = ['eventId','quantity','section','row', 'price']

	#params =  request.form["myvar"]

	data = request.data
	dataDict = json.loads(data)

	missing_array = []
	
	# First check if something is missing
	for param in required:
		if param not in dataDict:
			# Missing Param error
			missing_array.append(param)
			

	if missing_array:
		response = error_1(missing_array)

	else:

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


	if request.args.get('stubhublistingid'):


		if request.args.get('price'):

			x = getfirstprice(310,9445091)

			return x
		else:
			response = error_1('price')

	else:
			response = error_1('stubhublistingid')

@app.route('/weekly_consolidate', methods = ['GET'])
def weekly_consolidate():

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



	if request.args.get('first_day') and request.args.get('last_day'):

		aws_consolidate(client, request.args.get('first_day'),request.args.get('last_day'))

	else:
		aws_consolidate(client,1,8)
	
	return 'success' 


@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
