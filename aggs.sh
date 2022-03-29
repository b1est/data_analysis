curl -XGET "http://localhost:9200/test/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "multi_match": {
      "query": "ЕС",
      "fields": ["title", "textBody"]
    }
  },
  "aggs": {
    "dates_with_holes": {
      "date_histogram": {
        "field": "PubDate",
        "interval": "day",
        "min_doc_count": 0
      }
    }
  },
  "size": 0
}'