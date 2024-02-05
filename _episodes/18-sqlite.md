---
title: "SQLite"
start: true
teaching: 0
exercises: 90
questions:
- "Data cleaning with SQLite"

objectives:
- "Understand how SQLite can help cleaning data"

keypoints:
- "How explore GBIF downloaded data?"
---

## 1: [SQLite](https://docs.google.com/presentation/d/1oMPNqm4tU9BwnUo1zJxI0nlXMPfIljYeAqh4vEdJZ_0/edit?usp=sharing)

![SQLite](../assets/img/SQLite.png)

---
## Exercise 1 : Download from GBIF.org
 
- Follow the use case dataset link, then click on **occurrences**
- See how many records per CountryOrArea?
- Filter occurrences with CountryOrArea= Croatia
- ⬇️ Download in **simple CSV format**

## Solution 1
The use cases download should look like this:
- A. [GBIF Download](https://doi.org/10.15468/dl.t2hj6v) (116,575 occurrences)
- B. [GBIF Download](https://doi.org/10.15468/dl.6gfwt3) (15,077 occurrences)
- C. [GBIF Download](https://doi.org/10.15468/dl.qy93m6) (13,668 occurrences)
- D. [GBIF Download](https://doi.org/10.15468/dl.6mf27m) (9,723 occurrences)

---
## Exercise 2 : Import into SQLite

Within DBrowser application
- Create a new empty database    
- Import the GBIF downloaded CSV as table named ‘occ’
- How many records do you have?
- Save your database

## Solution 2
```sql
select count(*) from occ; 
```

---
### Exercise 3 : Explore with DBBrowser
-Do you ALWAYS have **date, coordinates and scientificName**
-How complete are the data? Describe their data completeness
-Put your attention to **individualCount, taxonRank, coordinatesUncertainty, license,...**
-Will you take all records for your study(fitness for use)? Explain why? 
-Will you filter out some data? Explain why? 

## Solution 3
```sql
select * from occ where scientificName is null;
select * from occ where year is null or month is null or day is null;
select * from occ where decimalLatitude is null or decimalLongitude is null;

select count(*) from occ where individualCount is null;

select taxonRank, count(*) from occ group by taxonRank;
select phylum, count(*) from occ group by phylum;
select license, count(*) from occ group by license;
```
