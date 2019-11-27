'''import urllib3, requests, json
# Paste your Watson Machine Learning service apikey here
# Use the rest of the code sample as written
apikey = "DhyRJeFThb3Am9RJD6BVNmovN1J2OnwQgf10p8g1wO6G"
wml_instance = "5a2cb777-7359-4e4e-919e-df85b91c52bb"
wml_deployment = '***'
wml_service_credentials_url = 'https://us-south.ml.cloud.ibm.com'

# Get an IAM token from IBM Cloud
url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded", "Accept": "application/json" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]
ml_instance_id = "5a2cb777-7359-4e4e-919e-df85b91c52bb"


header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': wml_instance}
oNOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
#array = '[234786.75, 12795.5, 247582.25, 36037, 742518.25, 46695.75, 124880.25, 570893.5, 109443.75, 325634.5, 125730.25, 496055, 289388.75, 166927.5, 241175.5, 1754355.25]'
payload_scoring = {"input_data": ["empleo_sector_a", "empleo_sector_b", "empleo_sector_ab", "empleo_sector_c", "empleo_sector_d", "empleo_sector_e", "empleo_sector_f", "empleo_sector_g", "empleo_sector_h", "empleo_sector_i", "empleo_sector_j", "empleo_sector_k", "empleo_sector_m", "empleo_sector_n", "empleo_sector_o", "empleo_sector_serv"], "values": [234786.75, 12795.5, 247582.25, 36037, 742518.25, 46695.75, 124880.25, 570893.5, 109443.75, 325634.5, 125730.25, 496055, 289388.75, 166927.5, 241175.5, 1754355.25]}



response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/14e10e11-db13-4469-9727-d04528b5ad23/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))'''


import urllib3, requests, json
apikey = "UTGr2Pv-8o-lAAVo9Vc9GZuxBzccLPumvfFMJfFN-zmk"
ml_instance_id = "5a2cb777-7359-4e4e-919e-df85b91c52bb"
# Get an IAM token from IBM Cloud
url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]
# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation	
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}
array = [234786.75, 12795.5, 247582.25, 36037, 742518.25, 46695.75, 124880.25, 570893.5, 109443.75, 325634.5, 125730.25, 496055, 289388.75, 166927.5, 241175.5, 1754355.25]
# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields":["empleo_sector_a", "empleo_sector_b", "empleo_sector_ab", "empleo_sector_c", "empleo_sector_d", "empleo_sector_e", "empleo_sector_f", "empleo_sector_g", "empleo_sector_h", "empleo_sector_i", "empleo_sector_j", "empleo_sector_k", "empleo_sector_m", "empleo_sector_n", "empleo_sector_o", "empleo_sector_serv"], "values": [array]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v4/deployments/14e10e11-db13-4469-9727-d04528b5ad23/predictions', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))