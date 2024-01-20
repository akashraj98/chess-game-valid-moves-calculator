## How to run this project

Navigate to project root directory where Docker file is present with cd command

Build docker image using below command
`docker build -t chess-game .`

once docker image is build 
Run the docker image with below command
`docker run -p 8000:8000 chess-game`


Sample curl request to test the endpoint
`curl  -X POST \
  'http://127.0.0.1:8000/chess/knight' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "postions": {
    "Queen": "E7",
    "Bishop": "B7",
    "Rook": "G5",
    "Knight": "C3"
  }
}'
`
