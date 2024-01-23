---
title: "Data management & best practices"
start: true
teaching: 30
exercises: 15
questions:
- "How to deal with data"
- "Tips & tricks for good data mmanagement"
- "What is Biodiversity informatics"
- "What is a Biodiversity dataset"
objectives:
- "Introduction to data management & best practices"
- "Feel familiar with open data types"
- "understand the importance of Tidy data"

keypoints:
- "Understand some best data management practices"
---


### Presentation

<a href="https://docs.google.com/presentation/d/1xgCBYw0HCd2RHagOH4cL4xxK8fMSTyIPbqEQ8smULyo/edit?usp=sharing">
    <img src="{{ '/assets/img/data_management.PNG' | relative_url }}">
  </a>

> ## Exercise
> 
> **Challenge:** Make this data tidy.
> 
> 1. [SAMPLE_DATE](https://docs.google.com/spreadsheets/d/1SJ6Ng1Jol-zbDiLQlu-o2sqpbg73lViA/edit?usp=drive_link&ouid=106540432290122943029&rtpof=true&sd=true)
> 2. Open in spreadsheet programme (Excel, LibreOffice, Openoffice,....)
> 3. Make this data Tidy
>    (Each variable forms a column and contains values, Each observation forms a row, Each type of observational unit forms a table)
>    [Open this link for the complete excercise and tips](https://docs.google.com/document/d/1SJAcA83LBozLP0y2LGuFTP2KJcvZzgkP/edit#heading=h.gjdgxs)
> > ## Solution
> > 1. [`eventDate`](https://dwc.tdwg.org/terms/#dwc:eventDate)
> > 2. [`decimalLatitude`](https://dwc.tdwg.org/terms/#dwc:decimalLatitude)
> > 3. [`minimumDepthInMeters`](https://dwc.tdwg.org/terms/#dwc:minimumDepthInMeters) and [`maximumDepthInMeters`](https://dwc.tdwg.org/terms/#dwc:maximumDepthInMeters)
> > 4. [`vernacularName`](https://dwc.tdwg.org/terms/#dwc:vernacularName)
> > 5. [`organismQuantity`](https://dwc.tdwg.org/terms/#dwc:organismQuantity) and [`organismQuantityType`](https://dwc.tdwg.org/terms/#dwc:organismQuantityType)
> > 6. This one is tricky- it's two terms combined and will need to be split. [`indvidualCount`](https://dwc.tdwg.org/terms/#dwc:individualCount) and [`sex`](https://dwc.tdwg.org/terms/#dwc:sex)
> >
> > {: .output}
> {: .solution}
{: .challenge}
