set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\Oleg_Degay\Downloads\samp-170518-b142b06d3b48.json

to Enable Python virtual env

pip install virtualenv
virtualenv <your-env>
cd <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-cloud-video-live-stream

https://googleapis.dev/python/livestream/latest/index.html

PROJECT_ID = 29375673872
LOCATION = us-east1
OPERATION_ID = test29375673872


create_input.py [-h] --project_id PROJECT_ID [--location LOCATION] --input_id INPUT_ID
create_input.py [-h] --project_id 29375673872 --location us-east1 --input_id test29375673872

https://www.100ms.live/blog/webrtc-python-react-app
https://www.hackster.io/whitebank/rasbperry-pi-ffmpeg-install-and-stream-to-web-389c34

set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\Oleg_Degay\Downloads\samp-170518-b142b06d3b48.json
gcloud auth application-default print-access-token

ya29.c.b0AUFJQsG4D34bu-kLrdkY4d84blANNyLW8kBko-L2w6yazUWEl_9P0pHeJoTjb7mV6HbyESGlMmpowwRuFkab7T86zAzQkDJuICHMbuxJWBDMsFFu4bLNDFdKYDcqKcr9d8Zaw0Dag4e2swX7431n6Dy8ma0VxmaH8ZdXaxZQqBOk702xFQuqR1YhzExqgm55-Wb5hH8ENr7Q2r-yJJwfWmNTMQ6IRw

1. CREATE INPUT ENDPOINT:
https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/inputs?inputId=INPUT_ID
GET https://livestream.googleapis.com/v1/projects/29375673872/locations/us-east1/inputs?inputId=test29375673872
test29375673872
test29375673872a
test29375673872b

2. CREATE CHANNEL:
https://livestream.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/channels?channelId=CHANNEL_ID"
POST https://livestream.googleapis.com/v1/projects/29375673872/locations/us-east1/channels?channelId=test29375673872_ch
Request body: 
{
  "inputAttachments": [
    {
      "key": "test29375673872_ch1",
      "input": "projects/29375673872/locations/us-east1/inputs/test29375673872"
    }
  ],
  "output": {
    "uri": "gs://remote-robot-translation"
  },
  "elementaryStreams": [
    {
      "key": "es_video",
      "videoStream": {
        "h264": {
          "profile": "high",
          "widthPixels": 1280,
          "heightPixels": 720,
          "bitrateBps": 3000000,
          "frameRate": 30
        }
      }
    },
    {
      "key": "es_audio",
      "audioStream": {
        "codec": "aac",
        "channelCount": 2,
        "bitrateBps": 160000
      }
    }
  ],
  "muxStreams": [
    {
      "key": "mux_video",
      "elementaryStreams": ["es_video"],
      "segmentSettings": { "segmentDuration": "2s" }
    },
    {
      "key": "mux_audio",
      "elementaryStreams": ["es_audio"],
      "segmentSettings": { "segmentDuration": "2s" }
    }
  ],
  "manifests": [
    {
      "fileName": "main.mpd",
      "type": "DASH",
      "muxStreams": [
        "mux_video",
        "mux_audio"
      ],
      "maxSegmentCount": 5
    }
  ]
}

Response
{
    "name": "projects/29375673872/locations/us-east1/operations/operation-1663934839625-5e957050b979d-289e3407-899ff979",
    "metadata": {
        "@type": "type.googleapis.com/google.cloud.video.livestream.v1.OperationMetadata",
        "createTime": "2022-09-23T12:07:19.673779655Z",
        "target": "projects/29375673872/locations/us-east1/channels/test29375673872ch",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
    },
    "done": false
}

GET https://livestream.googleapis.com/v1/projects/29375673872/locations/us-east1/channels/test29375673872ch
 
