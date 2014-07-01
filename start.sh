#!/bin/bash

./main.py $* 2>>bot.log & tail -f bot.log
