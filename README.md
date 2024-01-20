## How to run this project

Navigate to project root directory where Docker file is present with cd command<br>

Build docker image using below command<br>
`docker build -t chess-game .`<br>

once docker image is build <br>
Run the docker image with below command<br>
`docker run -p 8000:8000 chess-game`<br>


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
<br>
#Alternate way to run project
pull the docker image from docker hub <br>
`docker pull akshraj98/chess-valid-moves-game:1.0.0` <br>
run the docker image with <br>
`docker run -p 8000:8000 chess-game`
`
