import logging, os, json, uuid
import boto3

from flask_lambda import FlaskLambda
from flask_cors import CORS
from flask import jsonify, make_response, request

from error_handler import error_handler, BadRequestException

s3 = boto3.client("s3")

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s')
lambda_handler = FlaskLambda(__name__)
CORS(lambda_handler)
logger = logging.getLogger(__name__)

def check_environment():
  if "BUCKET" not in os.environ:
    logger.error("Missing BUCKET environment variable")
    exit(-1)

check_environment()

def success_json_response(payload):
  """
  Turns payload into a JSON HTTP200 response
  """
  response = make_response(jsonify(payload), 200)
  response.headers["Content-type"] = "application/json"
  return response

@lambda_handler.route("/save", methods=["POST"])
@error_handler
def trigger_api():
  """
  Routine which saves request body as a JSON file to S3 if it is valid JSON

  It adds an ID field which is also used as the file name
  """
  if request.json:
    # need to save the file as JSON
    localdict = request.json
    localdict["id"] = str(uuid.uuid4())
    s3.put_object(
      Body=json.dumps(localdict),
      Bucket=os.environ.get("BUCKET"),
      Key=localdict["id"]
    )
    return(success_json_response(localdict))
  else:
    raise BadRequestException("Request must be JSON")

if __name__ == "__main__":
  lambda_handler.run(debug=True, port=5001, host="0.0.0.0", threaded=True)