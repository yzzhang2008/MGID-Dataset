## MGID: A Social Media Based Multi-Modal Getty Image Depression and Emotion Dataset

### Introduction
To support the development of social meida based multi-modal depression and emotion joint recognition, we collect textual and visual documents from Getty Image, and create a weakly labeled multi-modal depression and emotion dataset, called MGID. We we set a list of keywords with strongly depression (e.g., "depressive patient", "depression", etc.) and emotions ("happy", "scary", etc.) to query Getty Images, and use the labels of these words to weakly label the retrieved multi-modal documents of the first thirty pages. Based on these documents, we construct a new multi-modal Getty Image depression and emotion (MGID) dataset. It contains 2500 depressive and 2500 non-depressive samples. As for emotion, we divide MGID into SIX emotions, i.e., happiness, depressed, neutral, fear, surprise (including positive and negative feelings), anger.

### Dataset Distribution
![Dataset Distribution](https://github.com//yzzhang2008//MGID-Dataset//edit//main//distribution.png)

### Citation
All publications reporting on research using this database have to acknowledge this by citing the following article:<br> 
To be waited...

### How To Use

#### (1) Download Raw Data
*** As for text, the title and textual content has been encapsulated into .zip file. One can access it directionly.<br> 
*** As for raw image, since Getty Image is a commercial platform, we will not upload the raw image directionly. Instead, we choose to upload its image URL, and provide the   imagedownloader.py to download all raw images in MGID.

#### (2) User license
##### 1. Commercial and academic use
MGID is made available for research purposes only. Any commercial use of this data is forbidden.
##### 2. Redistribution
The user may not distribute the database or parts of it to any third party.
##### 3. Publications
The use of data for illustrative purposes in publications is allowed. Publications include both scientific papers and
presentations for scientific/educational purposes. 
##### 4. Changes
  The author is allowed to change these terms of use at any time. 
##### 5. Warranty
  We open it just for the development of depression detection. The dataset comes without any warranty. In no event shall the provider be held responsible for any loss or damage caused by the use of this data.
