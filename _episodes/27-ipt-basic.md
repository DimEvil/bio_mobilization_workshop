---
title: "How to publish biodiversity data through GBIF.org"
start: true
teaching: 30
exercises: 30
questions:
- "What is IPT for the GBIF node"
- "How is IPT organized"
objectives:
- "Understand how IPT works."
keypoints:
- "IPT is the main tool to publish your data to GBIF"
---

GBIF—the Global Biodiversity Information Facility—is an international network and data infrastructure funded by the world's governments and aimed at providing anyone, anywhere, open access to data about all types of life on Earth.



# Presentation: Data Publication workflow 'generic'

<a href="https://docs.google.com/presentation/d/1FPRafCOs8YUawLi3zIUEJ4HHYULgqVZ1KplxUMT9MLM/edit?usp=sharing">
    <img src="{{ '/assets/img/genericworkflow.PNG' | relative_url }}">
  </a>

# GBIF supports publication, discovery and use of four classes of data:

[IPT manual](https://ipt.gbif.org/manual/en/ipt/latest/)

* *Resource metadata*
* *Checklist Data*
* *Occurrence Data*
* *Sampling Event Data*

At the simplest, GBIF enables sharing information describing a biodiversity data resource – even when no further digital information is currently available from the resource. Other data classes support an increasingly richer and wider range of information on species, their distributions and abundance.

Data publishers are strongly encouraged to share their data using the richest appropriate data class. This maximizes the usefulness of the data for users.

To give yourself an introduction to how the IPT can be used to publish biodiversity data through GBIF.org, it’s highly recommended watching this concise 25 minute live demo below:

<a href="https://www.youtube.com/watch?v=eDH9IoTrMVE" title="IPT movie">
<img src="{{ '/assets/img/bbpf-ipt.png' | relative_url }}" alt="Alternate Text" />
</a>

![Announcement](https://github.com/DimEvil/croment/assets/3965195/7bcb145f-fcb9-4970-ba61-0bb49d8ec9e9){: .image-with-shadow }



# Prerequisites

You require an account on a GBIF Integrated Publishing Toolkit (IPT) to publish your data.

**Hint:** it is highly recommended that you save yourself time and money by requesting an account on an IPT located at a data hosting centre in your country or community.

**Hint:** you could install and maintain your own IPT instance if you have technical skills and capacity to maintain it online near 100% of the time.

**Hint:** if no data hosting centre exists in your country, and you or your organization don’t have the technical skills and capacity to host an IPT, you can contact the GBIF Helpdesk <helpdesk@gbif.org> for assistance.

Assuming that you would like to register your dataset with GBIF and make it globally discoverable via GBIF.org, your dataset must be affiliated with an organization that is registered with GBIF.

**Hint:** to register your organization with GBIF, start by completing this online questionnaire. The registration process can take days, so in parallel you can proceed to publish your data.

**Hint:** if you aren’t affiliated with any organization, you can contact the GBIF Helpdesk <helpdesk@gbif.org> for assistance. In the meantime, you can proceed to publish your data.


# Instructions
To publish your data, follow the 7 steps below.

![screenshot]({{ page.root }}/fig/flow-all.png){: .image-with-shadow }

### 1. Select the class of biodiversity data you have from this list:

* Resource metadata
* Checklist Data
* Occurrence Data
* Sampling Event Data

### 2. Transform your data into a table structure, using Darwin Core (DwC) terms as column names

*Hint:* try using an Excel template to structure your data, and understand what DwC terms are required and recommended (Excel templates for each dataset class are available in the above links - see the previous point)

*Hint:* it is possible to use data stored in a supported database

### 3. Upload your data to the IPT

*Hint:* refer to other sections of this manual for additional guidance, such as the Manage Resources Menu section.

### 4. Map the data (e.g. Checklist Data gets mapped to the Taxon Core, Occurrence Data gets mapped to the Occurrence Core, Sampling Event Data gets mapped to the Event Core).

### 5. Fill in resource metadata using the IPT’s metadata editor

### 6. Publish the dataset (make it freely and openly available worldwide)

### 7. Register the dataset with GBIF.

`Your organization must be registered with GBIF (see prerequisite 2 above) and added to your IPT by the IPT administrator. Otherwise, the organization will not be available to choose from in the IPT.`

> ## Exercises 1: Publish this occurrence dataset (dwc-a) on the Croatian IPT [ipt.bioportal.hr](https://ipt.bioportal.hr)
> 
> Most of the work on the publication of the data lies in the data cleaning, mapping and the description of the dataset. Once a Darwin Core archive was generated, it is fairly simple to  publish it again, on another IPT for example. <br>
> Publish [this](https://doi.org/10.15468/5jkd4t) dataset, "already published by the Croatian Faculty of science (which is already a GBIF data publisher) on the GBIF ECA Cloud IPT" again on the Croatian IPT. Make sure you are logged in on the IPT instance. <br>
> You should have recieved a pswdr and a login to the Croatian IPT instance. 
>
> > ## Solution
> > 1. donwload the dwc-a file [here](https://cloud.gbif.org/eca/archive.do?r=med3)
> > 2. Go to the tab `manage resources`
> > 3. create a new dataset `Create new dataset`
> > 4. provide a new shortname
> > 5. Choose `Import from an archived resource`
> >   <img src="{{ 'assets/img/extra/iptimport2.PNG' | relative_url }}" alt="import" width="400">{: .image-with-shadow }
> > 6. Choose the Dwc-a file
> > 7. Click `save`
> > 8. If everything went correct, your metadata and data is correctly mapped in the IPT and ready to publih.
> > 9. Click `publish` to finish this exercise
> {: .solution}
{: .challenge}

> ## Exercises 2: Publish this occurrence dataset on the Croatian IPT [ipt.bioportal.hr](https://ipt.bioportal.hr)
> 
> Unfortunately, in most cases you will not have a DwC-a file availble, meaning, that you should, together with the data researcher or person who would like to publish his or her data to GBIF, create a dwc-a. <br> The IPT is a good tool to create dwc-archives. (There are also other tools available [here for example](https://ipt.gbif.org/manual/en/ipt/latest/dwca-guide#publishing-dwc-a-manually) but we do not recommend this. <br> For this exercise we prepared all the files needed to generate a dwc-a.
> Make sure you are logged in on the IPT instance. <br>
> You should have recieved a pswdr and a login to the Croatian IPT instance. <br>
> You can find an occurrence file [here]({{ page.root }}/data/occurrence_snails.csv) <br>
> You can find the metadata [here](https://docs.google.com/document/d/1m5dgtcwsmPxdWpZbbgb9aa2ncWXhI197/edit?usp=sharing&ouid=106540432290122943029&rtpof=true&sd=true) **Copy paste only the minimal set of information on the right place in the IPT**
>
> > ## Solution
> > 1. donwload the dwc-a file
> > 2. go to the tab `manage resources`
> > 3. create a new dataset `Create new dataset`
> > 4. provide a new shortname
> > 5. select type `occurrence` and push `create`
> > 6. deal with `source data`, `darwin core mappings` and `metadata`  (*tip see session metadata & data validation*)
> > 7. publish your dataset
> > 8. change visibility to `public`
> > 9. register your dataset (not needed in this exercise)
> > 10. Click `publish` to finish this exercise
> {: .solution}
{: .challenge}

> ## Exercises 3: Publish this sample based dataset dataset on the Croatian IPT [ipt.bioportal.hr](https://ipt.bioportal.hr)
> 
> Unfortunately, in most cases you will not have a DwC-a file availble, meaning, that you should, together with the data researcher or person who would like to publish his or her data to GBIF, create a dwc-a. <br> The IPT is a good tool to create dwc-archives.  For this exercise we prepared all the files needed to generate a dwc-a.
> Make sure you are logged in on the IPT instance. <br>
> You should have recieved a pswdr and a login to the Croatian IPT instance. <br>
> You can find an occurrence file here [occurrence]({{ page.root }}/data/occurrence_odonata.csv) <br>
> You can find the event file here [event]({{ page.root }}/data/event_odonata.csv) <br>
> You can find the metadata [here](https://docs.google.com/document/d/1rwI5zFHLyYv0tFx5dxaWrWEy6DFpcEB2nAeyVkzQPF4/edit?usp=sharing) **Copy paste only the minimal set of information on the right place in the IPT**
>
> > ## Solution
> > 1. go to the tab `manage resources`
> > 2. create a new dataset `Create new dataset`
> > 3. provide a new shortname
> > 4. select type `sampling event` and push `create`
> > 5. deal with `source data` add both files to the IPT
> > 6. deal with `darwin core mappings` for the occurrence file
> > 7. deal with `darwin core mappings` for the event file
> > 8. deal with  `metadata`  *also here, only copy paste the minimum needed*
> > 9. publish your dataset
> > 10. change visibility to `public`
> > 11. register your dataset (not needed in this exercise)
> > 12. Click `publish` to finish this exercise
> {: .solution}
{: .challenge}


> ## Exercises 4: Publish this checklist dataset dataset on the Croatian IPT [ipt.bioportal.hr](https://ipt.bioportal.hr)
> 
> Now, we will publish a checklist data on on the IPT. A checklist is a 3rd type of dataset you can publish on Global Biodiversity Information Facility. A cheklist has no occurrences as the core file, but the species (the taxon) is at the centre of the star scheme.    For this exercise we prepared all the files needed to generate a dwc-a.
> Make sure you are logged in on the IPT instance. <br>
> You should have recieved a pswdr and a login to the Croatian IPT instance. <br>
> You can find all the needed data here: [TrIAS](https://github.com/trias-project/ad-hoc-checklist/tree/master/data/processed) The TrIAS cheklist is a live 'cheklist' which is regurlaly updated through `Github actions` and an automatic update function in the IPT. <br>
> You can donwload the needed files from Github. If you want to make sure your published datsets is always up to date, you can use the raw online files as a source file [raw Github content](https://raw.githubusercontent.com/trias-project/ad-hoc-checklist/master/data/processed/taxon.csv)
> For this checklist, we have a taxon, description, distribution, speciesprofile and references file. Only use (download) the taxon, description and spieciesprofile file for this exercise.
> You can find the metadata [here](https://www.gbif.org/dataset/1f3505cd-5d98-4e23-bd3b-ffe59d05d7c2) **Copy paste only the minimal set of information on the right place in the IPT**
>
> > ## Solution
> > 1. go to the tab `manage resources`
> > 2. create a new dataset `Create new dataset`
> > 3. provide a new shortname
> > 4. select type `checklist` and push `create`
> > 5. deal with the `source data` import all files in the IPT. In the IPT, for taxon choose `source data is url` instead of file and use this url [raw Github content](https://raw.githubusercontent.com/trias-project/ad-hoc-checklist/master/data/processed/taxon.csv)
> >    <img src="{{ 'assets/img/extra/iptsourceurl.PNG' | relative_url }}" alt="import" width="400">{: .image-with-shadow }
> > 6. deal with `darwin core mappings` for the `distribution` file
> > 7. deal with `darwin core mappings` for the `distribution` file
> > 8. deal with `darwin core mappings` for the `profile` file
> > 9. deal with  `metadata`  *also here, only copy paste the minimum needed*
> > 10. publish your dataset
> > 11. change visibility to `public`
> > 12. register your dataset (not needed in this exercise)
> > 13. Click `publish` to finish this exercise
> {: .solution}
{: .challenge}



