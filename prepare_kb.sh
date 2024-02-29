#!/bin/bash

hackmd_auth_token_fp=${1:-""}
kb_store_folder=${2:-"./kb"}
if [ -z "$hackmd_auth_token_fp" ]; then
  echo "Usage: $0 <hackmd_auth_token>"
  exit 1
fi
mkdir -p $kb_store_folder
kb_data_folder=${kb_store_folder}/data
mkdir -p $kb_data_folder

#### Process CEL Knowledge Base ####
cel_root_folder=${kb_store_folder}/cel
cel_data_folder=${cel_root_folder}/data
mkdir -p $cel_root_folder
mkdir -p $cel_data_folder

####
# TODO: it would be good to only download if new files have been added or files changed
####
# # Download the knowledge base
# echo "Downloading CEL knowledge base from HackMD ..."
# token=$(cat $hackmd_auth_token_fp)
# echo $token
# flist=${cel_root_folder}/flist.json
# curl "https://api.hackmd.io/v1/teams/cryptoecon/notes" -H "Authorization: Bearer ${token}" > $flist

# # now use JQ to parse out the publish links
# jq -r '.[] | .publishLink' $flist > ${cel_root_folder}/publish_links.txt

# # download the data
# while read -r line; do
#   mdpath=$line/download
#   echo "Downloading $line"
#   curl -L $mdpath > ${cel_data_folder}/$(basename $line.md)
#   sleep 1
# done < ${cel_root_folder}/publish_links.txt

# clean up (remove some files that shouldn't be in the KB, primarily link files)
rm -f ${cel_data_folder}/almanac.md
rm -f ${cel_data_folder}/qredo-collab.md
rm -f ${cel_data_folder}/ideahub.md
rm -f ${cel_data_folder}/Bk2ks7BIj.md  # this is a research plan document
for file in ${cel_data_folder}/*.md; do
    if [ -f "$file" ]; then
        first_line=$(sed -n '1p' "$file")
        if [[ "$first_line" == "<!DOCTYPE html>" ]]; then
            echo "File '$file' starts with '<!DOCTYPE html>'. Removing from KB."
            # Add your desired action here (e.g., delete the file).
            rm -f "$file"
        fi
    fi
done

# # remove files that are less than 2kb
find ${cel_data_folder} -type f -size -2k -delete

# create symbolic links to all remaining CEL files in the root knowledgebase folder
for file in ${cel_data_folder}/*.md; do
    if [ -f "$file" ]; then
        abs_path=$(realpath $file)
        ln -s $abs_path ${kb_data_folder}/$(basename $file)
    fi
done

#### Process Filecoin FIPs ####
echo "Downloading Filecoin FIPs ..."
fip_folder=${kb_store_folder}/fips
# if folder doesn't exist, clone the repo
if [ ! -d "$fip_folder" ]; then
    mkdir -p $fip_folder
    git clone https://github.com/filecoin-project/FIPs.git $fip_folder
fi
# create symbolic links to all FIPs in the root knowledgebase folder
for file in ${fip_folder}/FIPS/*.md; do
    if [ -f "$file" ]; then
        abs_path=$(realpath $file)
        ln -s $abs_path ${kb_data_folder}/$(basename $file)
    fi
done

#### Process Filecoin Spec ####
echo "Downloading Filecoin Spec ..."
spec_folder=${kb_store_folder}/spec
# if folder doesn't exist, clone the repo
if [ ! -d "$spec_folder" ]; then
    mkdir -p $spec_folder
    git clone https://github.com/filecoin-project/specs.git $spec_folder
fi

# create symbolic links to all specs in the root knowledgebase folder
for file in $(find "${kb_store_folder}/spec/content" -type f -name "*.md"); do
    if [[ "$filename" != _* ]]; then
        if [ -f "$file" ]; then
            abs_path=$(realpath $file)
            ln -s $abs_path ${kb_data_folder}/$(basename $file)
        fi
    fi
done

# preprocess the data and injest the knowledge base
source activate llm
python3 prepare_kb.py