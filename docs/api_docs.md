# Health API Documentation

## Base URL
http://localhost:8000

## Endpoints

### GET /cached-health/{user_id}
Returns cached health data

### GET /secure-data
Requires header:
x-token: health123

### GET /patients
Query Params:
- limit
- offset