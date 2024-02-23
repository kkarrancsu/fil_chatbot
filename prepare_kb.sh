#!/bin/bash

hackmd_auth_token_fp=${1:-""}
kb_store_folder=${2:-"./kb/cel"}
if [ -z "$hackmd_auth_token_fp" ]; then
  echo "Usage: $0 <hackmd_auth_token>"
  exit 1
fi
mkdir -p $kb_store_folder
dest_folder=${kb_store_folder}/data
mkdir -p $dest_folder

# # Download the knowledge base
# echo "Downloading CEL knowledge base from HackMD ..."
# token=$(cat $hackmd_auth_token_fp)
# echo $token
# flist=${kb_store_folder}/flist.json
# curl "https://api.hackmd.io/v1/teams/cryptoecon/notes" -H "Authorization: Bearer ${token}" > $flist

# # now use JQ to parse out the publish links
# jq -r '.[] | .publishLink' $flist > ${kb_store_folder}/publish_links.txt

# # download the data
# while read -r line; do
#   mdpath=$line/download
#   echo "Downloading $line"
#   curl -L $mdpath > ${dest_folder}/$(basename $line.md)
#   sleep 1
# done < ${kb_store_folder}/publish_links.txt

# clean up (remove some files that shouldn't be in the KB, primarily link files)
rm -f ${dest_folder}/almanac.md
rm -f ${dest_folder}/qredo-collab.md
rm -f ${dest_folder}/ideahub.md
rm -f ${dest_folder}/Bk2ks7BIj.md  # this is a research plan document
for file in ${dest_folder}/*.md; do
    if [ -f "$file" ]; then
        first_line=$(sed -n '1p' "$file")
        if [[ "$first_line" == "<!DOCTYPE html>" ]]; then
            echo "File '$file' starts with '<!DOCTYPE html>'. Removing from KB."
            # Add your desired action here (e.g., delete the file).
            rm -f "$file"
        fi
    fi
done

# remove files that are less than 2kb
find ${dest_folder} -type f -size -2k -delete

# prepare the VectorStore object
source activate llm
python3 prepare_kb.py