#!/bin/sh

query = $1
src = $2

curl -XGET 'http://localhost:9200/test/_all/_search?pretty=true' -H 'Content-Type: application/json' -d '
{
        "query": {
            "bool": {
                "must": [{
                    "multi_match": {
                        "query": "'$query'",
                        "fields": ["textBody", "title"]
                    }
                }],
                "filter": [{
                    "match": {
                        "source": "'$src'"
                    }
                }]
            }
        }
    }
' | /usr/lib/cgi-bin/prog2_html.py
