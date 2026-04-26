COPY INTO weather_db.weather_schema.weather_gold
FROM @weather_db.weather_schema.weather_stage
FILE_FORMAT = (TYPE = CSV SKIP_HEADER=1)
ON_ERROR = 'CONTINUE'
FORCE = FALSE;