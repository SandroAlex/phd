#!/bin/bash

# This script is intended for copying modifications of local version of my
# repository into aerossol remote server. 

local="/home/alex/Dropbox/repositories/cdlearn/"
remote="sandroal@aerossol.if.usp.br:/LFASGI/sandroal/cdlearn/"

rsync --progress --verbose --compress --human-readable --archive \
$local $remote
