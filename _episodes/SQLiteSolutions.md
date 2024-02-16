# Data cleaning with SQLite
## Exercise 1 : Download from GBIF.org
### Instructions
- Select at least one of the use cases
- Follow the use case dataset links:
    - A. [iNaturalist Research-grade Observations](https://www.gbif.org/dataset/50c9509d-22c7-4a22-a47d-8c48425ef4a7)
    - B.[Italian official Adriatic  landings between 1953 and 2012](https://www.gbif.org/dataset/6e0f65ad-8ffb-4a07-ac53-2efe9153e994)
    - C.[Naturgucker](https://www.gbif.org/dataset/6ac3f774-d9fb-4796-b3e9-92bf6c81c084)
    - D.[Trawl survey data from the Jabuka Pit area](https://www.gbif.org/dataset/29719761-2d0e-4fef-bfcb-764b20c07d40)
- Click on the **occurrences** button
- On the left panel, filter by **CountryOrArea**
- How many occurrences to you see for **Croatia**?
- ⬇️ Download in **simple CSV** format
- Open the downloaded file with a text editor

### Solution 1
- Your downloads should looks like this:
	- A. [GBIF Download](https://doi.org/10.15468/dl.t2hj6v) (116,575 occurrences)
	- B. [GBIF Download](https://doi.org/10.15468/dl.6gfwt3) (15,077 occurrences)
	- C. [GBIF Download](https://doi.org/10.15468/dl.qy93m6) (13,668 occurrences)
	- D. [GBIF Download](https://doi.org/10.15468/dl.6mf27m) (9,723 occurrences)

## Exercise 2 : Import data
### Instructions
- Open the DBrowser application
- Create a new empty database
- Import the GBIF downloaded data into an SQL table named ‘occ’
- How many records do you have?
- Save your database

### Solution 2
```sql
select count(*) from occ;
```

## Exercise 3 : Explore data
### Instructions
- (Re)Open your database with DBBrowser
- Do you ALWAYS have **scientificName, date and coordinates**?
- How complete are the data? (describe)
- Put special attention to **individualCount, taxonRank, coordinatesUncertainty, license, issues** fields
- Are all records suitable for your study(**fitness for use**)? Explain why?
- Would you **filter out** some data? Explain why?

### Solution 3
```sql
select * from occ where scientificName is null;
select * from occ where eventdate is null;
select * from occ where year is null or month is null or day is null;
select * from occ where decimalLatitude is null or decimalLongitude is null;

select count(*) from occ where individualCount is null;
select taxonRank, count(*) from occ group by taxonRank;
select phylum, count(*) from occ group by phylum;
select license, count(*) from occ group by license;
```

## Exercice 4 : Discard data
### Instructions
- Do you have absence data? (see **occurrenceStatus** field)
- Discard absence data
- Create a **trusted** view to eliminate **absence data** and data with **taxonRank different from SPECIES**
- How many records do you have in this trusted view?

### Solution 4
```sql
select count(*) from occ where occurrenceStatus='ABSENT';

create view trusted as select * from occ where occurrenceStatus='PRESENT' and taxonRank='SPECIES';
select count(*) from trusted;
```


## Exercice 5 : Filter data
### Instructions
- Do you have data without **coordinatesUncertaintyInMeters**?
- Do you have data with coordinates uncertainty > 10 km?
- Update your **trusted** view to filter out these **records**
- Select only these **fields** in your view:
    - scientificName, Date, coordinates, uncertainty and occurrenceID
- How many records do you have now?

### Solution 5
```sql
select count(*) from occ where coordinateUncertaintyInMeters is null;
select coordinateUncertaintyInMeters, count(*) from occ group by coordinateUncertaintyInMeters;
select * from occ where CAST(coordinateUncertaintyInMeters as INTEGER) > 10000;

drop view if exists trusted ;
create view trusted as select scientificName, year,month,day,decimalLatitude, decimalLongitude,  CAST(coordinateUncertaintyInMeters as INTEGER) as uncertainty, occurrenceID from occ where occurrenceStatus='PRESENT'  and taxonRank='SPECIES' and uncertainty <= 10000;
select count(*) from trusted;

select eventdate, strftime('%d',eventdate) as day, strftime('%m',eventdate) as month, strftime('%Y', eventdate) as year from occ;
```

## Exercice 6 : Annotate data
### Instructions
- IndividualCound is not a mandatory field, set it to 1 when null
- Add a **withMedia** field,  set it to True when mediaType is not null
- Add these two fields to your **trusted** view
- Export the **trusted** view results in a CSV file
- (Now you are ready to merge this online data with your own data)
 
### Solution 6
```sql
update occ set individualCount=1 where individualCount is null;

drop view if exists trusted ;
create view trusted as select scientificName, year,month,day,decimalLatitude, decimalLongitude,  CAST(coordinateUncertaintyInMeters as INTEGER) as uncertainty, occurrenceID, individualCount, mediaType is not null as withMedia from occ where occurrenceStatus='PRESENT' and taxonRank='SPECIES' and uncertainty <= 10000;
```
