CREATE TABLE health_users(
    id SERIAL PRIMARY KEY,
    name TEXT,
    age INT,
    gender TEXT
);

CREATE TABLE health_records(
    id SERIAL PRIMARY KEY,
    user_id INT,
    heart_rate INT,
    steps INT,
    sleep_hours FLOAT,
    created_at TIMESTAMP
);

CREATE TABLE medications(
    id SERIAL PRIMARY KEY,
    user_id INT,
    drug_name TEXT,
    dosage TEXT
);

CREATE TABLE alerts(
    id SERIAL PRIMARY KEY,
    user_id INT,
    alert_type TEXT,
    message TEXT,
    created_at TIMESTAMP
);