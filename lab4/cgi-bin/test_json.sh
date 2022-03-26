#!/bin/sh



curl -XGET 'http://localhost:9200/test/_all/_search?pretty=true' -H 'Content-Type: application/json' -d '
{
        "query": {
            "bool": {
                "must": [{
                    "multi_match": {
                        "query": "'$1'",
                        "fields": ["textBody", "title"]
                    }
                }],
                "filter": [{
                    "match": {
                        "source": "'$2'"
                    }
                }]
            }
        }
    }
' | ./cgi-bin/prog2_html.py
