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
