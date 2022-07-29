from os import getenv

# Database Config
dbconfig = dict(
    host=getenv("MYSQL_HOST","customer-accounts.clu4325ulqiy.us-west-1.rds.amazonaws.com"),
    port=getenv("MYSQL_PORT","3306"),
    user=getenv("MYSQL_USER","admin"),
    password=getenv("MYSQL_PASSWORD","qLPDbOaZlKnr"),
    database=getenv("MYSQL_DATABASE","pluralsight_microservice")
)