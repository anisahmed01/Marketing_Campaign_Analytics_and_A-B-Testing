-- =====================================================
-- MARKETING CAMPAIGN ANALYSIS (SQL QUERIES)
-- =====================================================
-- Dataset: marketing_data
-- Objective: Analyze campaign performance, platform trends,
-- efficiency, and conversion metrics across Facebook & Instagram
-- =====================================================



-- =====================================================
-- 1. CAMPAIGN PERFORMANCE (CROSS-PLATFORM)
-- =====================================================
-- Combines Facebook & Instagram data
-- Identifies high-volume campaigns based on conversions
-- =====================================================

SELECT
    campaign,
    SUM(views) AS total_views,
    SUM(clicks) AS total_clicks,
    SUM(conversions) AS total_conversions,
    SUM(cost) AS total_cost
FROM (
    SELECT
        "Facebook Ad Campaign" AS campaign,
        "Facebook Ad Views" AS views,
        "Facebook Ad Clicks" AS clicks,
        "Facebook Ad Conversion" AS conversions,
        "Cost Per Facebook Ad" AS cost
    FROM marketing_data

    UNION ALL

    SELECT
        "Instagram Ad Campaign",
        "Instagram Ad Views",
        "Instagram Ad Clicks",
        "Instagram Ad Conversion",
        "Cost Per Instagram Ad"
    FROM marketing_data
)
GROUP BY campaign
ORDER BY total_conversions DESC;



-- =====================================================
-- 2. PLATFORM COMPARISON (FACEBOOK vs INSTAGRAM)
-- =====================================================
-- Compares total performance across platforms
-- Helps identify which platform drives more engagement
-- =====================================================

SELECT
    'Facebook' AS Platform,
    SUM("Facebook Ad Views") AS Total_Views,
    SUM("Facebook Ad Clicks") AS Total_Clicks,
    SUM("Facebook Ad Conversion") AS Total_Conversions,
    SUM("Cost Per Facebook Ad") AS Total_Cost
FROM marketing_data

UNION ALL

SELECT
    'Instagram' AS Platform,
    SUM("Instagram Ad Views") AS Total_Views,
    SUM("Instagram Ad Clicks") AS Total_Clicks,
    SUM("Instagram Ad Conversion") AS Total_Conversions,
    SUM("Cost Per Instagram Ad") AS Total_Cost
FROM marketing_data;



-- =====================================================
-- 3. CAMPAIGN EFFICIENCY (AVERAGE METRICS)
-- =====================================================
-- Uses AVG() for behavioral comparison
-- NOT weighted → not for final business decisions
-- =====================================================

SELECT
    campaign,
    AVG(ctr) AS avg_ctr,
    AVG(conv_rate) AS avg_conversion_rate,
    AVG(cpc) AS avg_cpc
FROM (
    SELECT
        "Facebook Ad Campaign" AS campaign,
        "Facebook Click-through Rate" AS ctr,
        "Facebook Conversion Rate" AS conv_rate,
        "Facebook Cost Per Click" AS cpc
    FROM marketing_data

    UNION ALL

    SELECT
        "Instagram Ad Campaign",
        "Instagram Click-through Rate",
        "Instagram Conversion Rate",
        "Instagram Cost Per Click"
    FROM marketing_data
)
GROUP BY campaign;



-- =====================================================
-- 4. UNIFIED CAMPAIGN PERFORMANCE (WEIGHTED METRICS)
-- =====================================================
-- TRUE business performance using SUM-based calculations
-- Avoids averaging ratios
-- Used for decision-making
-- =====================================================

SELECT
    campaign,
    SUM(clicks) * 100.0 / SUM(views) AS campaign_ctr,
    SUM(conversions) * 100.0 / SUM(clicks) AS campaign_conversion_rate,
    SUM(cost) * 1.0 / SUM(conversions) AS campaign_cost_per_conversion,
    SUM(cost) AS total_spend,
    SUM(conversions) AS total_conversions
FROM (
    SELECT
        "Facebook Ad Campaign" AS campaign,
        "Facebook Ad Views" AS views,
        "Facebook Ad Clicks" AS clicks,
        "Facebook Ad Conversion" AS conversions,
        "Cost Per Facebook Ad" AS cost
    FROM marketing_data

    UNION ALL

    SELECT
        "Instagram Ad Campaign",
        "Instagram Ad Views",
        "Instagram Ad Clicks",
        "Instagram Ad Conversion",
        "Cost Per Instagram Ad"
    FROM marketing_data
)
GROUP BY campaign
ORDER BY total_conversions DESC;