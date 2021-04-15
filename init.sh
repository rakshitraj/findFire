#!/usr/bin/bash

## On-site (local) Module

# 1. Create directory for raw images
echo "Create local/raw"
mkdir local/raw || echo "Requirement already satisfied"

## Server-side 

# 1. CSV file to store predictions
echo "Create server/preds.csv"
touch server/preds.csv || echo "Requirement already satisfied"
# 2. Source Environment Variable
source server/twilio.env || echo "Twilio credentials could not be loaded. Please ensure that you have the required credentials."

echo "init DONE!"