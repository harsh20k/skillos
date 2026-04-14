---
title: Open source etiquette
category: General
priority: Medium
starred: None
created: 2025-12-04T22:02:16.568604
updated: 2025-12-06T09:03:21.483124
dg-publish: true
---
# Open source etiquette

**Priority:** Medium

## Conversation

### Assistant

Here is a **simplified relational schema + CREATE TABLE statements** for the entities in your diagram (no separate relationship tables; relationships are captured via FKs already present in attributes).

---

### Simplified Schema (Overview)

- **Species domain**
  - `Species(species_id, common_name, conservation_status, alert_priority)`
  - `SpeciesLifeStage(lifestage_id, species_id FK, stage_name)`
  - `TrophicLevel(trophic_id, species_id FK, trophic_level)`
  - `HabitatPreference(habitat_pref_id, species_id FK, preferred_temp_range)`

- **Spatial / monitoring domain**
  - `WaterBody(waterbody_id, waterbody_name, waterbody_type)`
  - `MarineEcoregion(ecoregion_id, ecoregion_name, ecosystem_type)`
  - `ProtectedZone(zone_id, zone_name, geometry, region_code, buffer_distance_km, ecoregion_id FK)`
  - `SensorStation(station_id, station_name, latitude, longitude, region_code, waterbody_id FK)`
  - `SpeciesDetection(detection_id, station_id FK, species_id FK, detection_timestamp, estimated_count, confidence_score)`
  - `EnvironmentalCondition(condition_id, station_id FK, water_temp_celsius, ph, salinity_ppt)`

- **Vessels / alerts / compliance**
  - `Vessel(vessel_id, mmsi UNIQUE, vessel_name, vessel_type, org_id FK)`
  - `VesselPosition(position_id, mmsi FK, latitude, longitude, position_timestamp)`
  - `Alert(alert_id, vessel_id FK, zone_id FK, alert_timestamp, alert_severity)`
  - `FishingLicense(license_id, vessel_id FK, target_species, quota_kg)`
  - `ComplianceLog(compliance_id, alert_id FK, vessel_id FK, action_taken)`

- **Surveys / historical data / tagging / genetics**
  - `Survey(survey_id, survey_name, survey_type)`
  - `MonitoringEvent(event_id, waterbody_id FK, event_date, sampling_method, survey_id FK)`
  - `HistoricalObservation(observation_id, event_id FK, species_id FK, count, biomass_kg)`
  - `TaggingRecord(tag_id, observation_id FK, tag_number, tagging_date)`
  - `GeneticSample(sample_id, species_id FK, detection_id FK, collection_date)`

- **Organizations / people / quality**
  - `Organization(org_id, org_name, org_type)`
  - `Researcher(researcher_id, org_id FK, first_name, last_name)`
  - `DataQuality(quality_id, validated_by FK → Researcher, validation_status)`

---

### SQL: Table Creation Statements (Generic SQL / PostgreSQL-ish)

```sql
-- 1. Core species tables
CREATE TABLE Species (
    species_id          SERIAL PRIMARY KEY,
    common_name         VARCHAR(255) NOT NULL,
    conservation_status VARCHAR(100),
    alert_priority      INTEGER
);

CREATE TABLE SpeciesLifeStage (
    lifestage_id  SERIAL PRIMARY KEY,
    species_id    INTEGER NOT NULL REFERENCES Species(species_id),
    stage_name    VARCHAR(100) NOT NULL
);

CREATE TABLE TrophicLevel (
    trophic_id     SERIAL PRIMARY KEY,
    species_id     INTEGER NOT NULL REFERENCES Species(species_id),
    trophic_level  VARCHAR(50) NOT NULL
);

CREATE TABLE HabitatPreference (
    habitat_pref_id       SERIAL PRIMARY KEY,
    species_id            INTEGER NOT NULL REFERENCES Species(species_id),
    preferred_temp_range  VARCHAR(50) -- e.g., "5–12°C"
);

-- 2. Spatial / monitoring context
CREATE TABLE WaterBody (
    waterbody_id    SERIAL PRIMARY KEY,
    waterbody_name  VARCHAR(255) NOT NULL,
    waterbody_type  VARCHAR(100) -- e.g., "ocean", "bay", "estuary"
);

CREATE TABLE MarineEcoregion (
    ecoregion_id    SERIAL PRIMARY KEY,
    ecoregion_name  VARCHAR(255) NOT NULL,
    ecosystem_type  VARCHAR(100) -- e.g., "coastal", "pelagic"
);

CREATE TABLE ProtectedZone (
    zone_id             SERIAL PRIMARY KEY,
    zone_name           VARCHAR(255) NOT NULL,
    geometry            TEXT,              -- simplified; could be WKT/GeoJSON
    region_code         VARCHAR(50),
    buffer_distance_km  NUMERIC(6,2),
    ecoregion_id        INTEGER REFERENCES MarineEcoregion(ecoregion_id)
);

CREATE TABLE SensorStation (
    station_id    SERIAL PRIMARY KEY,
    station_name  VARCHAR(255) NOT NULL,
    latitude      NUMERIC(9,6) NOT NULL,
    longitude     NUMERIC(9,6) NOT NULL,
    region_code   VARCHAR(50),
    waterbody_id  INTEGER REFERENCES WaterBody(waterbody_id)
);

CREATE TABLE SpeciesDetection (
    detection_id        SERIAL PRIMARY KEY,
    station_id          INTEGER NOT NULL REFERENCES SensorStation(station_id),
    species_id          INTEGER NOT NULL REFERENCES Species(species_id),
    detection_timestamp TIMESTAMP NOT NULL,
    estimated_count     INTEGER,
    confidence_score    NUMERIC(3,2)      -- 0.00–1.00
);

CREATE TABLE EnvironmentalCondition (
    condition_id         SERIAL PRIMARY KEY,
    station_id           INTEGER NOT NULL REFERENCES SensorStation(station_id),
    water_temp_celsius   NUMERIC(4,1),
    ph                   NUMERIC(3,2),
    salinity_ppt         NUMERIC(5,2)
);

-- 3. Organizations and people
CREATE TABLE Organization (
    org_id    SERIAL PRIMARY KEY,
    org_name  VARCHAR(255) NOT NULL,
    org_type  VARCHAR(100) -- e.g., "NGO", "Research", "Regulator"
);

CREATE TABLE Researcher (
    researcher_id  SERIAL PRIMARY KEY,
    org_id         INTEGER REFERENCES Organization(org_id),
    first_name     VARCHAR(100) NOT NULL,
    last_name      VARCHAR(100) NOT NULL
);

-- 4. Vessels, licenses, positions, alerts, compliance
CREATE TABLE Vessel (
    vessel_id    SERIAL PRIMARY KEY,
    mmsi         BIGINT NOT NULL UNIQUE,
    vessel_name  VARCHAR(255),
    vessel_type  VARCHAR(100),
    org_id       INTEGER REFERENCES Organization(org_id)
);

CREATE TABLE VesselPosition (
    position_id         SERIAL PRIMARY KEY,
    mmsi                BIGINT NOT NULL REFERENCES Vessel(mmsi),
    latitude            NUMERIC(9,6) NOT NULL,
    longitude           NUMERIC(9,6) NOT NULL,
    position_timestamp  TIMESTAMP NOT NULL
);

CREATE TABLE Alert (
    alert_id        SERIAL PRIMARY KEY,
    vessel_id       INTEGER NOT NULL REFERENCES Vessel(vessel_id),
    zone_id         INTEGER NOT NULL REFERENCES ProtectedZone(zone_id),
    alert_timestamp TIMESTAMP NOT NULL,
    alert_severity  VARCHAR(50)  -- e.g., "LOW", "MEDIUM", "HIGH"
);

CREATE TABLE FishingLicense (
    license_id     SERIAL PRIMARY KEY,
    vessel_id      INTEGER NOT NULL REFERENCES Vessel(vessel_id),
    target_species VARCHAR(255),
    quota_kg       NUMERIC(10,2)
);

CREATE TABLE ComplianceLog (
    compliance_id  SERIAL PRIMARY KEY,
    alert_id       INTEGER NOT NULL REFERENCES Alert(alert_id),
    vessel_id      INTEGER NOT NULL REFERENCES Vessel(vessel_id),
    action_taken   TEXT
);

-- 5. Surveys, events, observations, tagging, genetics
CREATE TABLE Survey (
    survey_id    SERIAL PRIMARY KEY,
    survey_name  VARCHAR(255) NOT NULL,
    survey_type  VARCHAR(100) -- e.g., "acoustic", "trawl"
);

CREATE TABLE MonitoringEvent (
    event_id        SERIAL PRIMARY KEY,
    waterbody_id    INTEGER NOT NULL REFERENCES WaterBody(waterbody_id),
    event_date      DATE NOT NULL,
    sampling_method VARCHAR(100),
    survey_id       INTEGER REFERENCES Survey(survey_id)
);

CREATE TABLE HistoricalObservation (
    observation_id  SERIAL PRIMARY KEY,
    event_id        INTEGER NOT NULL REFERENCES MonitoringEvent(event_id),
    species_id      INTEGER NOT NULL REFERENCES Species(species_id),
    count           INTEGER,
    biomass_kg      NUMERIC(10,2)
);

CREATE TABLE TaggingRecord (
    tag_id         SERIAL PRIMARY KEY,
    observation_id INTEGER NOT NULL REFERENCES HistoricalObservation(observation_id),
    tag_number     VARCHAR(100) NOT NULL,
    tagging_date   DATE
);

CREATE TABLE GeneticSample (
    sample_id       SERIAL PRIMARY KEY,
    species_id      INTEGER NOT NULL REFERENCES Species(species_id),
    detection_id    INTEGER NOT NULL REFERENCES SpeciesDetection(detection_id),
    collection_date DATE
);

-- 6. Data quality
CREATE TABLE DataQuality (
    quality_id        SERIAL PRIMARY KEY,
    validated_by      INTEGER REFERENCES Researcher(researcher_id),
    validation_status VARCHAR(50) -- e.g., "PENDING", "VALIDATED", "REJECTED"
);
```

You can adapt this to:

- **PostgreSQL**: as-is (or swap `SERIAL` to `GENERATED ALWAYS AS IDENTITY`).
- **MySQL**: change `SERIAL` → `INT AUTO_INCREMENT`, timestamp types if needed.
- Add `ON DELETE CASCADE`/`ON UPDATE` rules where you need stronger referential behavior.

If you tell me your target DBMS (Postgres/MySQL/MariaDB/SQLite), I can adjust this to be 100% syntactically correct for that engine.

---

