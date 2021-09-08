#!/bin/sh
curl -d"score=70" -X POST http://localhost:5000/scores
curl http://localhost:5000/lookup?index=0
curl http:localhost:5000/avg/
