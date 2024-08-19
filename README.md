---
layout: default
title: Top UK Youtubers 2024 Project
---


**Top UK Youtubers 2024 Project**
using Excel > Python > SQL > Looker Studio


![Dashboard View on Looker](assets/images/ScreenRecording2024-08-18at11.25.37-ezgif.com-crop.gif)




# Table of contents 

- [Objective](#objective)
- [Data Source](#data-source)
- [Stages](#stages)
- [Design](#design)
  - [Mockup](#mockup)
  - [Tools](#tools)
- [Development](#development)
  - [Pseudocode](#pseudocode)
  - [Data Exploration](#data-exploration)
  - [Data Cleaning](#data-cleaning)
  - [Transform the Data](#transform-the-data)
  - [Create the SQL View](#create-the-sql-view)
- [Testing](#testing)
  - [Data Quality Tests](#data-quality-tests)
- [Visualisation](#visualisation)
  - [Results](#results)
  - [DAX Measures](#dax-measures)
- [Analysis](#analysis)
  - [Findings](#findings)
  - [Validation](#validation)
  - [Discovery](#discovery)
- [Recommendations](#recommendations)
  - [Potential ROI](#potential-roi)
  - [Potential Courses of Actions](#potential-courses-of-actions)
- [Conclusion](#conclusion)




# Objective 

**Pain Point**: The Head of Marketing needs to identify the top UK YouTubers in 2024 to choose the most effective influencers for upcoming marketing campaigns.

**Ideal Solution**: Develop a dashboard that highlights key metrics such as subscriber count, total views, videos uploaded, and engagement. This tool will empower the marketing team to make data-driven decisions on influencer collaborations.

## User story 

As the Head of Marketing, I need a dashboard that analyses UK YouTube channel performance. This will help me pinpoint the top channels by metrics like subscriber count and average views, enabling better decisions for influencer partnerships and maximising campaign impact.


# Data source 

- What data is needed to achieve our objective?

We need data on the top UK YouTubers in 2024 that includes their 
- channel names
- total subscribers
- total views
- total videos uploaded



- Where is the data coming from? 
The data is sourced from Kaggle (an Excel extract), [see here to find it.](https://www.kaggle.com/datasets/bhavyadhingra00020/top-100-social-media-influencers-2024-countrywise?resource=download)


# Stages

- Design
- Developement
- Testing
- Analysis 
 


# Design 

## Dashboard components required 
- What should the dashboard contain based on the requirements provided?

To understand what it should contain, we need to figure out what questions we need the dashboard to answer:

1. Who are the top 10 YouTubers with the most subscribers?
2. Which 3 channels have uploaded the most videos?
3. Which 3 channels have the most views?
4. Which 3 channels have the highest average views per video?
5. Which 3 channels have the highest views per subscriber ratio?
6. Which 3 channels have the highest subscriber engagement rate per video uploaded?

For now, these are some of the questions we need to answer, this may change as we progress down our analysis. 


## Dashboard mockup

- What should it look like? 

Some of the data visuals that may be appropriate in answering our questions include:

1. Table
2. Treemap
3. Scorecards
4. Horizontal bar chart 




![Dashboard-Mockup](assets/images/mokkup.png)




## Tools 


| Tool | Purpose |
| --- | --- |
| MS Excel | Exploring the data |
| Python via VS Code | Cleaning and scraping missing data |
| MySQL Workbench | Further cleaning, testing, and analysing the data |
| Looker Studio by Google | Visualising the data via interactive dashboards |
| GitHub | Hosting the project documentation and version control |
| Mokkup AI | Designing the wireframe/mockup of the dashboard | 


# Development

## Pseudocode

- What's the general approach in creating this solution from start to finish?

1. Get the data
2. Explore the data in Excel
3. Use Python API scraping script to fill in missing data
4. Clean the data with Python then move to SQL
5. Clean the data on SQL
6. Visualise the data in Looker Studio
7. Generate the findings based on the insights
8. Write the documentation + commentary
9. Publish the data to GitHub Pages

## Data exploration notes

This is the stage where you have a scan of what's in the data, errors, inconcsistencies, bugs, weird and corrupted characters etc  


- What are your initial observations with this dataset? What's caught your attention so far? 

1. There are at least 4 columns that contain the data we need for this analysis, which signals we have everything we need from the file without needing to contact the client for any more data. 
2. The first column contains the channel ID with what appears to be channel IDS, which are separated by a @ symbol - we need to extract the channel names from this.
3. Some of the cells and header names are in a different language - we need to confirm if these columns are needed, and if so, we need to address them.
4. We have more data than we need, so some of these columns would need to be removed





## Data cleaning 
- What do we expect the clean data to look like? (What should it contain? What contraints should we apply to it?)

The aim is to refine our dataset to ensure it is structured and ready for analysis. 

The cleaned data should meet the following criteria and constraints:

- Only relevant columns should be retained.
- All data types should be appropriate for the contents of each column.
- No column should contain null values, indicating complete data for all records.

Below is a table outlining the constraints on our cleaned dataset:

| Property | Description |
| --- | --- |
| Number of Rows | 100 |
| Number of Columns | 4 |

And here is a tabular representation of the expected schema for the clean data:

| Column Name | Data Type | Nullable |
| --- | --- | --- |
| channel_name | VARCHAR | NO |
| total_subscribers | INTEGER | NO |
| total_views | INTEGER | NO |
| total_videos | INTEGER | NO |



- What steps are needed to clean and shape the data into the desired format?

1. Remove unnecessary columns by only selecting the ones you need
2. Extract Youtube channel names from the first column
3. Rename columns using aliases







### Transform the data 



```sql
/*
# 1. Select the required columns
# 2. Extract the channel name from the 'NOMBRE' column
*/

-- 1.
SELECT
    SUBSTRING_INDEX(NOMBRE, '@', 1) AS channel_name,  -- 2.
    total_subscribers,
    total_views,
    total_videos

FROM
    top_uk_youtubers_2024;

```


### Create the SQL view 

```sql
/*
# 1. Create a view to store the transformed data
# 2. Ensure the extracted channel name is in VARCHAR(100)
# 3. Select the required columns from the top_uk_youtubers_2024 SQL table
*/

-- 1.
CREATE VIEW view_uk_youtubers_2024 AS

-- 2.
SELECT
    CAST(SUBSTRING_INDEX(NOMBRE, '@', 1) AS CHAR(100)) AS channel_name, -- 2.
    total_subscribers,
    total_views,
    total_videos

-- 3.
FROM
    top_uk_youtubers_2024;

```


# Testing 

- What data quality and validation checks are you going to create?

Here are the data quality tests conducted:

## Row count check
```sql
/*
# Count the total number of records (or rows) in the SQL view
*/

SELECT
    COUNT(*) AS no_of_rows
FROM
    view_uk_youtubers_2024;


```

**Output:** 100 Rows ✔️



## Column count check
### SQL query 
```sql
/*
# Count the total number of columns (or fields) are in the SQL view
*/


SELECT
    COUNT(*) AS column_count
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'view_uk_youtubers_2024'
```
**Output:** 4 Columns ✔️


## Data type check
### SQL query 
```sql
/*
# Check the data types of each column from the view by checking the INFORMATION SCHEMA view
*/

-- 1.
SELECT
    COLUMN_NAME,
    DATA_TYPE
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_NAME = 'view_uk_youtubers_2024';
```
**Output:** channel_name = varchar / total_subs = int / total_views = bigint / total_vids = int ✔️


## Duplicate count check
### SQL query 
```sql
/*
# 1. Check for duplicate rows in the view
# 2. Group by the channel name
# 3. Filter for groups with more than one row
*/

-- 1.
SELECT
    channel_name,
    COUNT(*) AS duplicate_count
FROM
    view_uk_youtubers_2024

-- 2.
GROUP BY
    channel_name

-- 3.
HAVING
    COUNT(*) > 1;
```
**Output:** No duplicates ✔️


# Visualisation 


## Results

- What does the dashboard look like?

![GIF of Looker Dashboard](assets/images/ScreenRecording2024-08-18at11.25.37-ezgif.com.gif)

This shows the Top UK Youtubers in 2024 so far. 


## Looker Table Calculations

### 1. Total Subscribers (M)
```sql
Total Subscribers (M) = 
total_subscribers/1000000

```

### 2. Total Views (B)
```sql
total_views/1000000000

```


### 4. Average Views Per Video (M)
```sql
Average Views per Video (M) = 
IF(total_videos > 0, (total_views / total_videos) / 1000000, NULL)

```


### 5. Subscriber Engagement Rate
```sql
Subscriber Engagement Rate = 
SUM(total_subscribers) / SUM(total_videos)

```


### 6. Views per subscriber
```sql
SUM(total_views)/SUM(total_subscribers)

```




# Analysis 

## Findings

- What did we find?

For this analysis, we're going to focus on the questions below to get the information we need for our marketing client - 

Here are the key questions we need to answer for our marketing client: 
1. Who are the top 10 YouTubers with the most subscribers?
2. Which 3 channels have uploaded the most videos?
3. Which 3 channels have the most views?
4. Which 3 channels have the highest average views per video?
5. Which 3 channels have the highest views per subscriber ratio?
6. Which 3 channels have the highest subscriber engagement rate per video uploaded?


### 1. Who are the top 10 YouTubers with the most subscribers?

| Rank | Channel Name         | Subscribers (M) |
|------|----------------------|-----------------|
| 1    | NoCopyrightSounds    | 33.70           |
| 2    | DanTDM               | 28.90           |
| 3    | Dan Rhodes           | 27.10           |
| 4    | Miss Katy            | 24.90           |
| 5    | Mister Max           | 24.60           |
| 6    | KSI                  | 24.10           |
| 7    | Dua Lipa             | 23.70           |
| 8    | Jelly                | 23.60           |
| 9    | Sidemen              | 21.60           |
| 10   | Mrwhosetheboss       | 19.20           |


### 2. Which 3 channels have uploaded the most videos (excluding news channels)?

| Rank | Channel Name    | Videos Uploaded |
|------|-----------------|-----------------|
| 1    | GRM Daily       | 15,021          |
| 2    | Manchester City | 8,503           |
| 3    | Liverpool FC    | 6,772           |



### 3. Which 3 channels have the most views?


| Rank | Channel Name | Total Views (B) |
|------|--------------|-----------------|
| 1    | DanTDM       | 19.78           |
| 2    | Dan Rhodes   | 18.56           |
| 3    | Mister Max   | 15.97           |


### 4. Which 3 channels have the highest average views per video?

| Channel Name | Averge Views per Video (M) |
|--------------|-----------------|
| Mark Ronson  | 332.69          |
| Jessie J     | 60.98           |
| Dua Lipa     | 4.80            |


### 5. Which 3 channels have the highest views per subscriber ratio?

| Rank | Channel Name       | Views per Subscriber        |
|------|-----------------   |---------------------------- |
| 1    | GRM Daily          | 1200.56                     |
| 2    | Nickelodeon        | 1062.67                     |
| 3    | Disney Channel UK  | 1037.19                     |



### 6. Which 3 channels have the highest subscriber engagement rate per video uploaded?

| Rank | Channel Name    | Subscriber Engagement Rate  |
|------|-----------------|---------------------------- |
| 1    | Mark Ronson     | 345,500                     |
| 2    | Jessie J        | 110,416.67                  |
| 3    | Dua Lipa        | 84,642.86                   |


### Notes

For this analysis, we'll prioritize analysing the metrics that are important in generating the expected ROI for our marketing client, which are the YouTube channels with the most 

- subscribers
- total views
- videos uploaded



## Validation 

### 1. Youtubers with the most subscribers 

#### Calculation breakdown

Campaign idea = product placement 

1. NoCopyrightSounds 
- Average views per video = 6.43 million
- Product cost = $5
- Potential units sold per video = 6.43 million x 2% conversion rate = 128,600 units sold
- Potential revenue per video = 128,600 x $5 = $643,000
- Campaign cost (one-time fee) = $50,000
- **Net profit = $643,000 - $50,000 = $593,000**

b. DanTDM

- Average views per video = 5.36 million
- Product cost = $5
- Potential units sold per video = 5.36 million x 2% conversion rate = 107,200 units sold
- Potential revenue per video = 107,200 x $5 = $536,000
- Campaign cost (one-time fee) = $50,000
- **Net profit = $536,000 - $50,000 = $486,000**

c. Dan Rhodes

- Average views per video = 11.38 million
- Product cost = $5
- Potential units sold per video = 11.38 million x 2% conversion rate = 227,600 units sold
- Potential revenue per video = 227,600 x $5 = $1,138,000
- Campaign cost (one-time fee) = $50,000
- **Net profit = $1,138,000 - $50,000 = $1,088,000**


Best option from category: Dan Rhodes


#### SQL query 

```sql
/* 

# 1. Define variables 
# 2. Create a CTE that rounds the average views per video 
# 3. Select the column you need and create calculated columns from existing ones 
# 4. Filter results by Youtube channels
# 5. Sort results by net profits (from highest to lowest)

*/


-- 1. 
SET @conversionRate = 0.02;		-- The conversion rate @ 2%
SET @productCost = 5.0;			-- The product cost @ $5
SET @campaignCost = 50000.0;		-- The campaign cost @ $50,000	


-- 2.  
WITH ChannelData AS (
    SELECT 
        channel_name,
        total_views,
        total_videos,
        ROUND((CAST(total_views AS FLOAT) / total_videos), -4) AS rounded_avg_views_per_video
    FROM 
        youtube_db.dbo.view_uk_youtubers_2024
)

-- 3. 
SELECT 
    channel_name,
    rounded_avg_views_per_video,
    (rounded_avg_views_per_video * @conversionRate) AS potential_units_sold_per_video,
    (rounded_avg_views_per_video * @conversionRate * @productCost) AS potential_revenue_per_video,
    ((rounded_avg_views_per_video * @conversionRate * @productCost) - @campaignCost) AS net_profit
FROM 
    ChannelData


-- 4. 
WHERE 
    channel_name in ('NoCopyrightSounds', 'DanTDM', 'Dan Rhodes')    


-- 5.  
ORDER BY
	net_profit DESC

```

![Most videos](assets/images/most_subs.png)

#### Output - numbers match sql results



### 2. Youtubers with the most videos uploaded

### Calculation breakdown 

Campaign idea = sponsored video series  

1. GRM Daily
- Average views per video = 510,000
- Product cost = $5
- Potential units sold per video = 510,000 x 2% conversion rate = 10,200 units sold
- Potential revenue per video = 10,200 x $5= $51,000
- Campaign cost (11-videos @ $5,000 each) = $55,000
- **Net profit = $51,000 - $55,000 = -$4,000 (potential loss)**

b. **Manchester City**

- Average views per video = 240,000
- Product cost = $5
- Potential units sold per video = 240,000 x 2% conversion rate = 4,800 units sold
- Potential revenue per video = 4,800 x $5= $24,000
- Campaign cost (11-videos @ $5,000 each) = $55,000
- **Net profit = $24,000 - $55,000 = -$31,000 (potential loss)**

b. **Yogscast**

- Average views per video = 690,000
- Product cost = $5
- Potential units sold per video = 690,000 x 2% conversion rate = 13,800 units sold
- Potential revenue per video = 13,800 x $5= $69,000
- Campaign cost (11-videos @ $5,000 each) = $55,000
- **Net profit = $69,000 - $55,000 = $14,000 (profit)**


Best option from category: Yogscast

#### SQL query 
```sql
/* 
# 1. Define variables
# 2. Create a CTE that rounds the average views per video
# 3. Select the columns you need and create calculated columns from existing ones
# 4. Filter results by YouTube channels
# 5. Sort results by net profits (from highest to lowest)
*/


-- 1.
SET @conversionRate  = 0.02;           -- The conversion rate @ 2%
SET @productCost  = 5.0;               -- The product cost @ $5
SET @campaignCostPerVideo  = 5000.0;   -- The campaign cost per video @ $5,000
SET @numberOfVideos  = 11;               -- The number of videos (11)


-- 2.
WITH ChannelData AS (
    SELECT
        channel_name,
        total_views,
        total_videos,
        ROUND((CAST(total_views AS FLOAT) / total_videos), -4) AS rounded_avg_views_per_video
    FROM
        youtube_db.dbo.view_uk_youtubers_2024
)


-- 3.
SELECT
    channel_name,
    rounded_avg_views_per_video,
    (rounded_avg_views_per_video * @conversionRate) AS potential_units_sold_per_video,
    (rounded_avg_views_per_video * @conversionRate * @productCost) AS potential_revenue_per_video,
    ((rounded_avg_views_per_video * @conversionRate * @productCost) - (@campaignCostPerVideo * @numberOfVideos)) AS net_profit
FROM
    ChannelData


-- 4.
WHERE
    channel_name IN ('GRM Daily', 'Man City', 'YOGSCAST Lewis & Simon ')


-- 5.
ORDER BY
    net_profit DESC;
```

![Most videos](assets/images/most_videos.png)

#### Output - numbers match sql results





### 3.  Youtubers with the most views 

#### Calculation breakdown

Campaign idea = Influencer marketing 

a. DanTDM

- Average views per video = 5.36 million
- Product cost = $5
- Potential units sold per video = 5.36 million x 2% conversion rate = 107,200 units sold
- Potential revenue per video = 107,200 x $5 = $536,000
- Campaign cost (3-month contract) = $130,000
- **Net profit = $536,000 - $130,000 = $406,000**


b. Dan Rhodes

- Average views per video = 11.38 million
- Product cost = $5
- Potential units sold per video = 11.38 million x 2% conversion rate = 227,600 units sold
- Potential revenue per video = 227,600 x $5 = $1,138,000
- Campaign cost (3-month contract) = $130,000
- **Net profit = $1,138,000 - $130,000 = $1,008,000**


c. Mister Max

- Average views per video = 13.98 million
- Product cost = $5
- Potential units sold per video = 13.98 million x 2% conversion rate = 279,600 units sold
- Potential revenue per video = 279,600 x $5 = $1,398,000
- Campaign cost (3-month contract) = $130,000
- **Net profit = $1,398,000 - $130,000 = $1,268,000**


Best option from category: Mister Max



#### SQL query 
```sql
/*
# 1. Define variables
# 2. Create a CTE that rounds the average views per video
# 3. Select the columns you need and create calculated columns from existing ones
# 4. Filter results by YouTube channels
# 5. Sort results by net profits (from highest to lowest)
*/



-- 1.
SET @conversionRate  = 0.02;        -- The conversion rate @ 2%
SET @productCost  = 5.0;            -- The product cost @ $5
SET @campaignCost  = 130000.0;      -- The campaign cost @ $130,000



-- 2.
WITH ChannelData AS (
    SELECT
        channel_name,
        total_views,
        total_videos,
        ROUND(CAST(total_views AS FLOAT) / total_videos, -4) AS avg_views_per_video
    FROM
        youtube_db.dbo.view_uk_youtubers_2024
)


-- 3.
SELECT
    channel_name,
    avg_views_per_video,
    (avg_views_per_video * @conversionRate) AS potential_units_sold_per_video,
    (avg_views_per_video * @conversionRate * @productCost) AS potential_revenue_per_video,
    (avg_views_per_video * @conversionRate * @productCost) - @campaignCost AS net_profit
FROM
    ChannelData


-- 4.
WHERE
    channel_name IN ('Mister Max', 'DanTDM', 'Dan Rhodes')


-- 5.
ORDER BY
    net_profit DESC;

```
![Most videos](assets/images/most_view.png)

#### Output - numbers match sql results



## Discovery

- What did we learn?

We discovered that 


1. NoCopyrightSounds, Dan Rhodes and DanTDM are the channnels with the most subscribers in the UK
2. GRM Daily, Man City and Yogscast are the channels with the most videos uploaded
3. DanTDM, Dan RHodes and Mister Max are the channels with the most views
4. Entertainment channels are useful for broader reach, as the channels posting consistently on their platforms and generating the most engagement are focus on entertainment and music 




## Recommendations 

- What do you recommend based on the insights gathered? 
  
1. Dan Rhodes is the best YouTube channel to collaborate with if we want to maximise visbility because this channel has the most YouTube subscribers in the UK
2. Although GRM Daily, Man City and Yogcasts are regular publishers on YouTube, it may be worth considering whether collaborating with them with the current budget caps are worth the effort, as the potential return on investments is significantly lower compared to the other channels.
3. Mister Max is the best YouTuber to collaborate with if we're interested in maximising reach, but collaborating with DanTDM and Dan Rhodes may be better long-term options considering the fact that they both have large subscriber bases and are averaging significantly high number of views.
4. The top 3 channels to form collaborations with are NoCopyrightSounds, DanTDM and Dan Rhodes based on this analysis, because they attract the most engagement on their channels consistently.


### Potential ROI 
- What ROI do we expect if we take this course of action?

1. Setting up a collaboration deal with Dan Rhodes would make the client a net profit of $1,008,000 per video
2. An influencer marketing contract with Mister Max can see the client generate a net profit of $1,268,000
3. If we go with a product placement campaign with DanTDM, this could  generate the client approximately $484,000 per video. If we advance with an influencer marketing campaign deal instead, this would make the client a one-off net profit of $406,000.
4. NoCopyrightSounds could profit the client $593,000 per video too (which is worth considering) 




### Action plan
- What course of action should we take and why?

Based on our analysis, we beieve the best channel to advance a long-term partnership deal with to promote the client's products is the Dan Rhodes channel. 

We'll have conversations with the marketing client to forecast what they also expect from this collaboration. Once we observe we're hitting the expected milestones, we'll advance with potential partnerships with DanTDM, Mister Max and NoCopyrightSounds channels in the future.   

- What steps do we take to implement the recommended decisions effectively?


1. Reach out to the teams behind each of these channels, starting with Dan Rhodes
2. Negotiate contracts within the budgets allocated to each marketing campaign
3. Kick off the campaigns and track each of their performances against the KPIs
4. Review how the campaigns have gone, gather insights and optimize based on feedback from converted customers and each channel's audiences 


