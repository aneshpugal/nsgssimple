import logging,os
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from azure.data.tables import TableServiceClient
# from logger import configure_logging
# from BlobForwarder import BlobDetails,Checkpoint,blob_Sender
# from datetime import datetime

blob_connection_string = os.environ["blobconnectionstring"]
table_connection_string = os.environ["AzureWebJobsStorage"]
initialized = False

def initialize_app():
    global initialized
    if not initialized:
        with TableServiceClient.from_connection_string(table_connection_string) as table_service_client:
            table_service_client.create_table_if_not_exists(table_name="Checkpoints")
        initialized = True

try:
    initialize_app()
except Exception as e:
    print(str(e))

# try:
#     timestamp = os.environ["CollectionTime"]
# except Exception as e:
#     print(str(e))


# timestamp = datetime.fromisoformat(timestamp_str)

def main(myblob: func.InputStream):
    try:
        print("triggerd properly")
        return
    except Exception as e:
        print(str(e))