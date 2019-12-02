const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const btoa = require("btoa");
const wml_credentials = new Map();
var request = require( 'request' );
var iam_token
// Paste your Watson Machine Learning service apikey here


function apiPost(scoring_url, token, mlInstanceID, payload, loadCallback, errorCallback){
	const oReq = new XMLHttpRequest();
	oReq.addEventListener("load", loadCallback);
	oReq.addEventListener("error", errorCallback);
	oReq.open("POST", scoring_url);
	oReq.setRequestHeader("Accept", "application/json");
	oReq.setRequestHeader("Authorization", token);
	oReq.setRequestHeader("ML-Instance-ID", mlInstanceID);
	oReq.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	oReq.send(payload);
}
var apikey = "UTGr2Pv-8o-lAAVo9Vc9GZuxBzccLPumvfFMJfFN-zmk";

// Use this code as written to get an access token from IBM Cloud REST API
//
var IBM_Cloud_IAM_uid = "bx";
var IBM_Cloud_IAM_pwd = "bx";

var options = { url     : "https://iam.bluemix.net/oidc/token",
                headers : { "Content-Type"  : "application/x-www-form-urlencoded",
                            "Authorization" : "Basic " + btoa( IBM_Cloud_IAM_uid + ":" + IBM_Cloud_IAM_pwd ) },
                body    : "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey" };

request.post( options, function( error, response, body )
{
	iam_token = JSON.parse( body )["access_token"];
} );
// NOTE: generate iam_token based on provided documentation
const wmlToken = "Bearer " + iam_token;

// NOTE: retrieve ml_instance_id based on provided documentation
const mlInstanceId = "5a2cb777-7359-4e4e-919e-df85b91c52bb";

// NOTE: manually define and pass the array(s) of values to be scored in the next line
const payload = '{"input_data": [{"fields": ["empleo_sector_a", "empleo_sector_b", "empleo_sector_ab", "empleo_sector_c", "empleo_sector_d", "empleo_sector_e", "empleo_sector_f", "empleo_sector_g", "empleo_sector_h", "empleo_sector_i", "empleo_sector_j", "empleo_sector_k", "empleo_sector_m", "empleo_sector_n", "empleo_sector_o", "empleo_sector_serv"], "values": [234786.75, 12795.5, 247582.25, 36037, 742518.25, 46695.75, 124880.25, 570893.5, 109443.75, 325634.5, 125730.25, 496055, 289388.75, 166927.5, 241175.5, 1754355.25]}]}';
const scoring_url = "https://us-south.ml.cloud.ibm.com/v4/deployments/14e10e11-db13-4469-9727-d04528b5ad23/predictions";

apiPost(scoring_url, wmlToken, mlInstanceId, payload, function (resp) {
	let parsedPostResponse;
	try {
		parsedPostResponse = JSON.parse(this.responseText);
	} catch (ex) {
		// TODO: handle parsing exception
	}
	console.log("Scoring response");
	console.log(parsedPostResponse);
}, function (error) {
	console.log(error);
});