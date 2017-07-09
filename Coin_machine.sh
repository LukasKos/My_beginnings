#!/bin/bash
echo -n "Select the amount of money: "
read input

function change {
  let a50=$input/50
  echo '50: ' $a50
  let a20=($input%50)/20
  echo '20: ' $a20
  let a10="(($input%50)%20)/10"
  echo '10: ' $a10
  let a5="((($input%50)%20)%10)/5"
  echo ' 5: ' $a5
  let a2="(((($input%50)%20)%10)%5)/2"
  echo ' 2: ' $a2
  let a1="((((($input%50)%20)%10)%5)%2)/1"
  echo ' 1: ' $a1
  }

change
