"""
Zonely Demo Data — sourced from actual Civic Intelligence Reports
Postcodes: LS1 1BA (West One, wellington street, Leeds), LS3 1AA (Leeds City College, Park Lane Campus, Park Lane, Leeds), LS6 3BN (Cumberland Court, Leeds)
"""

import re


def normalize_postcode(raw: str) -> str:
    """Uppercase and strip a postcode string."""
    return raw.strip().upper()


def is_valid_postcode(code: str) -> bool:
    return code in ZONELY_DEMO_DATA


ZONELY_DEMO_DATA = {

    # ─────────────────────────────────────────────────────────────────────────
    # LS1 1BA — Lisbon Street, Leeds City Centre
    # ─────────────────────────────────────────────────────────────────────────
    "LS1 1BA": {
        "street":       "West One, Wellington Street",
        "area":         "Leeds City Centre",
        "ward":         "Little London & Woodhouse",
        "constituency": "Leeds Central and Headingley",
        "civicScore":   560,
        "impactLevel":  "high",
        "impactLabel":  "High Impact",
        "headlineSummary": "City centre postcode with extreme crime rate but strong education profile, above-average incomes and a -38.4% decade crime trend. Commercial-heavy street with limited residential sales data.",
        "breakdown": {
            "Livability":       {"score": 55},
            "Investment":       {"score": 45},
            "Infrastructure":   {"score": 72},
            "Crime & Safety":   {"score": 20},
            "Development":      {"score": 60},
            "Education":        {"score": 78},
            "Affluence":        {"score": 62},
        },

        # ── Demographics ──────────────────────────────────────────────────────
        "population": {
            "avgHHIncome":          "£50K",
            "unemploymentRate":     "2.0%",
            "degreeQualified":      "49%",
            "genderSplit":          "58.5% Male",
            "singleResidents":      "89.9%",
            "veryGoodHealth":       "55.7%",
            "ukBorn":               "45%",
            "euPassportHolders":    "5.8%",
            "arabCommunity":        "17.1%",
            "whiteEthnicGroup":     "50%",
        },

        # ── Property & Investment ─────────────────────────────────────────────
        "property": {
            "avgPrice":             "£9.6M",
            "streetAvg":            "£9.6M",
            "leedsCity":            "£294K",
            "nationalMedian":       "£322K",
            "incomeRank":           "7/10",
            "salesSince1995":       4,
            "recentSales": [
                {"address": "Castle House, 31 Lisbon St (Other)", "price": "£14,500,000", "date": "Jun 2018", "est2025": "£18,186,740"},
            ],
            "roiSnapshot": {
                "avgBuyPrice":      "£9.6M",
                "grossYield":       "N/A",
                "netYield":         "N/A",
                "estRentalIncome":  "N/A",
                "note":             "No flat/residential sales data — commercial/mixed-use only",
            },
            "roiScenarios": {
                "conservative": {"purchasePrice": "£250,000", "stampDuty": "£10,000", "acquisitionCosts": "£262,000", "monthlyRent": "£950",  "annualIncome": "£11,400", "grossYield": "4.6%", "netYield": "3.4%", "fiveYrCapitalGrowth": "+£54K"},
                "baseCase":     {"purchasePrice": "£280,000", "stampDuty": "£11,400", "acquisitionCosts": "£293,400", "monthlyRent": "£1,100", "annualIncome": "£13,200", "grossYield": "4.7%", "netYield": "3.5%", "fiveYrCapitalGrowth": "+£60K"},
                "optimistic":   {"purchasePrice": "£310,000", "stampDuty": "£12,800", "acquisitionCosts": "£324,800", "monthlyRent": "£1,250", "annualIncome": "£15,000", "grossYield": "4.8%", "netYield": "3.6%", "fiveYrCapitalGrowth": "+£67K"},
            },
        },

        # ── Crime ─────────────────────────────────────────────────────────────
        "crime": {
            "crimeRate":        "2,240",
            "crimeRateUnit":    "per 1,000 residents",
            "areaRanking":      "7th highest of 168 in Hunslet & Riverside",
            "leedsRank":        "9th highest of 2,522 areas in Leeds",
            "tenYrTrend":       "-38.4%",
            "primaryCrimeType": "Violence & Sexual Offences (1,176.5/1,000)",
        },

        # ── Bureau Scores ─────────────────────────────────────────────────────
        "bureauScores": {
            "Livability": 55,
            "Investment": 45,
            "Infrastructure": 72,
            "Crime & Safety": 20,
            "Development": 60,
            "Education": 78,
            "Affluence": 62,
        },

        # ── Radar Chart Data ──────────────────────────────────────────────────
        "radarData": {
            "postcode": [55, 45, 72, 20, 60, 78, 62],
            "leedsAvg": [62, 55, 68, 35, 58, 60, 58],
        },

        # ── Health ────────────────────────────────────────────────────────────
        "health": {
            "veryGood": 64.2, "good": 28.8, "fair": 7.0, "bad": 0.0, "veryBad": 0.0,
        },

        # ── Partnership Status ────────────────────────────────────────────────
        "partnershipStatus": {
            "single": 89.9, "marriedOpp": 9.1, "divorced": 0.7, "widowed": 0.0, "marriedSameSex": 0.0, "other": 0.3,
        },

        # ── Investment Phases ─────────────────────────────────────────────────
        "phases": [
            {"phase": "disruption", "title": "Phase 1 — Disruption", "period": "0–2 Years"},
            {"phase": "growth",     "title": "Phase 2 — Growth",     "period": "3–5 Years"},
            {"phase": "compound",   "title": "Phase 3 — Compounding","period": "6–10 Years"},
        ],

        # ── Risk Flags ────────────────────────────────────────────────────────
        "risks": [
            {"level": "high",   "text": "Extreme Crime Rate (2,240/1,000 residents): 7th highest of 168 areas in Hunslet & Riverside; 9th highest of 2,522 areas in Leeds. Violence & Sexual Offences are the primary crime type (1,176.5/1,000). A critical concern for residents and investors."},
            {"level": "high",   "text": "Living Environment 10/10 (IMD): Maximum deprivation score for living environment — air quality, housing conditions and road traffic at worst national tier. Significant liveability concern for any residential use."},
            {"level": "medium", "text": "Very Limited Property Liquidity: Only 4 recorded sales since 1995, all classified as 'Other' (non-residential/commercial type). No flat or residential sales data exists for this postcode, making standard BTL investment analysis impossible on this street specifically."},
            {"level": "medium", "text": "Construction Noise & Disruption: Active development pipeline across city fringe means ongoing construction activity for 2–4 years. Premium lettings may be impacted."},
            {"level": "medium", "text": "Barriers to Housing (8/10): High barriers to housing and services — affordability and access constraints rated 8/10. This is a structural headwind for owner-occupier demand and long-term capital growth."},
            {"level": "low",    "text": "Strong Education Profile: 49% degree qualified (15.2pp above UK avg); 47.3% are economically inactive students. University of Leeds (1,339 yd) provides a continuous pipeline of high-quality student and graduate tenants for the broader LS1 postcode."},
            {"level": "low",    "text": "Above-Average Household Income (£50K): Household income ranks 7/10 nationally — above Leeds borough (£39K) and Yorkshire average (£42K). Income and employment deprivation both score 1/10 (best nationally), signalling a highly economically resilient resident base."},
            {"level": "low",    "text": "Highly Diverse International Community: Only 45% UK-born; 32.3% from Middle East & Asia. 17.1% Arab community (16.5pp above UK avg). Strong international student and professional demand provides a resilient, diverse occupier pool less correlated with domestic economic cycles."},
            {"level": "low",    "text": "Crime Rate Improving Long-Term (-38.4%): Despite extreme current crime levels, the decade-long -38.4% reduction signals structural improvement driven by investment and urban regeneration. The trend trajectory is positive."},
            {"level": "low",    "text": "Central Leeds Location: Wellington Place (HMRC HQ, Channel 4) directly adjacent. Leeds Station ~8 mins walk. Multiple Starbucks, Caffe Nero, Sainsbury's Local within 350 yards. Exceptional density of amenities for city centre workers and students."},
        ],

        # ── Insights ──────────────────────────────────────────────────────────
        "insights": [
            {"icon": "🎓", "title": "Strong Education Profile",              "text": "49% of residents hold a degree or equivalent — 15.2pp above the UK average."},
            {"icon": "👤", "title": "Predominantly Single Student-Professional Demographic", "text": "89.9% of residents are single vs 37.9% UK average."},
            {"icon": "💪", "title": "Healthy Population Above Average",      "text": "90.4% rate their health as Good or Very Good (vs UK 82%)."},
        ],

        # ── Report Meta ───────────────────────────────────────────────────────
        "reportDate":   "April 2026",
        "dataSources":  "ONS - Office for National Statistics · HM Land Registry · Ofsted · UK Police",
    },


    # ─────────────────────────────────────────────────────────────────────────
    # LS3 1AA — Hanover Square, Leeds City Centre
    # ─────────────────────────────────────────────────────────────────────────
    "LS3 1AA": {
        "street":       "Leeds City College, Burley Road",
        "area":         "Little London & Woodhouse",
        "ward":         "Little London & Woodhouse Ward",
        "constituency": "Leeds Central and Headingley",
        "civicScore":   624,
        "impactLevel":  "high",
        "impactLabel":  "High Impact",
        "headlineSummary": "City centre flat hotspot with 7.5% gross yields, 91.3% healthy population and a dramatic -74.1% decade crime decline. Strong graduate demand with 47.2% degree-qualified residents.",
        "breakdown": {
            "Livability":       {"score": 72},
            "Investment":       {"score": 62},
            "Infrastructure":   {"score": 85},
            "Crime & Safety":   {"score": 30},
            "Development":      {"score": 65},
            "Education":        {"score": 78},
            "Affluence":        {"score": 45},
        },

        # ── Demographics ──────────────────────────────────────────────────────
        "population": {
            "avgHHIncome":          "£30.2K",
            "unemploymentRate":     "1.0%",
            "degreeQualified":      "47.2%",
            "genderSplit":          "56.4% Female",
            "singleResidents":      "89.9%",
            "veryGoodHealth":       "62%",
            "ukBorn":               "65.2%",
            "euPassportHolders":    "11.3%",
            "chineseCommunity":     "9.6%",
            "whiteEthnicGroup":     "67.1%",
        },

        # ── Property & Investment ─────────────────────────────────────────────
        "property": {
            "avgPrice":             "£417K",
            "streetAvg":            "£350K",
            "leedsCity":            "£294K",
            "nationalMedian":       "£322K",
            "incomeRank":           "1/10",
            "salesSince1995":       160,
            "recentSales": [
                {"address": "26A Hanover Square (Flat)",     "price": "£165,000", "date": "Jan 2024", "est2025": "£170,285"},
                {"address": "26A Hanover Square (Flat)",     "price": "£134,000", "date": "Oct 2017", "est2025": "£169,514"},
                {"address": "26A Hanover Square (Flat)",     "price": "£118,000", "date": "Aug 2012", "est2025": "£188,034"},
                {"address": "32 Hanover Square (Semi-Det.)", "price": "£500,000", "date": "Jun 2009", "est2025": "£989,071"},
                {"address": "34 Hanover Square (Semi-Det.)", "price": "£125,000", "date": "Apr 2009", "est2025": "£254,213"},
            ],
            "roiSnapshot": {
                "avgBuyPrice":      "£169K",
                "grossYield":       "~7.5%",
                "netYield":         "~5.3%",
                "estRentalIncome":  "~£1,050/mo",
                "note":             "Flats/Maisonettes only",
            },
            "roiScenarios": {
                "conservative": {"purchasePrice": "£155,000", "stampDuty": "£6,200",  "acquisitionCosts": "£162,200", "monthlyRent": "£950",  "annualIncome": "£11,400", "grossYield": "7.0%", "netYield": "5.3%", "fiveYrCapitalGrowth": "+£34K"},
                "baseCase":     {"purchasePrice": "£169,000", "stampDuty": "£6,770",  "acquisitionCosts": "£176,770", "monthlyRent": "£1,050", "annualIncome": "£12,600", "grossYield": "7.5%", "netYield": "5.6%", "fiveYrCapitalGrowth": "+£37K"},
                "optimistic":   {"purchasePrice": "£185,000", "stampDuty": "£7,400",  "acquisitionCosts": "£193,400", "monthlyRent": "£1,200", "annualIncome": "£14,400", "grossYield": "7.8%", "netYield": "5.9%", "fiveYrCapitalGrowth": "+£41K"},
            },
        },

        # ── Crime ─────────────────────────────────────────────────────────────
        "crime": {
            "crimeRate":        "2.8",
            "crimeRateUnit":    "per 1,000 residents",
            "areaRanking":      "3rd lowest of 5 in Little London & Woodhouse",
            "leedsRank":        "133rd highest of 2,522 in Leeds",
            "tenYrTrend":       "-74.1%",
            "primaryCrimeType": "Public Order offences (nightlife proximity)",
        },

        # ── Bureau Scores ─────────────────────────────────────────────────────
        "bureauScores": {
            "Livability":      72,
            "Investment":      62,
            "Infrastructure":  85,
            "Crime & Safety":  30,
            "Development":     65,
            "Education":       78,
            "Affluence":       45,
        },

        # ── Radar Chart Data ──────────────────────────────────────────────────
        "radarData": {
            "postcode": [72, 62, 85, 30, 65, 78, 45],
            "leedsAvg": [65, 58, 70, 52, 62, 55, 60],
        },

        # ── Health ────────────────────────────────────────────────────────────
        "health": {
            "veryGood": 64.2, "good": 28.8, "fair": 7.0, "bad": 0.0, "veryBad": 0.0,
        },

        # ── Partnership Status ────────────────────────────────────────────────
        "partnershipStatus": {
            "single": 89.9, "marriedOpp": 7.0, "divorced": 1.6, "widowed": 0.5, "marriedSameSex": 0.0, "other": 1.0,
        },

        # ── Investment Phases ─────────────────────────────────────────────────
        "phases": [
            {"phase": "disruption", "title": "Phase 1 — Disruption", "period": "0–2 Years"},
            {"phase": "growth",     "title": "Phase 2 — Growth",     "period": "3–5 Years"},
            {"phase": "compound",   "title": "Phase 3 — Compounding","period": "6–10 Years"},
        ],

        # ── Risk Flags ────────────────────────────────────────────────────────
        "risks": [
            {"level": "high",   "text": "Crime Domain 10/10 (IMD): Highest national tier for crime risk. Public Order offences are primary — driven by nightlife proximity. Not household-targeted crime but a significant livability concern for families."},
            {"level": "high",   "text": "Living Environment 10/10 (IMD): Urban air quality and road traffic density at maximum deprivation score. Dense city centre context limits green space. Not suitable for buyers prioritising residential quiet."},
            {"level": "medium", "text": "Short-Term Rental Oversupply Risk: 4,200 units in Leeds pipeline. Temporary rental softening possible in 0–2 year window as new supply comes to market. Monitor void rates closely in 2025–2026."},
            {"level": "medium", "text": "Construction Noise & Disruption: Active development pipeline across city fringe means ongoing construction activity for 2–4 years. Premium lettings may be impacted."},
            {"level": "medium", "text": "Affordability Barrier 9/10 (IMD): Very high barriers to housing — mortgage affordability for owner-occupiers is stretched. This is a structural risk to long-term capital growth rates."},
            {"level": "low",    "text": "Exceptional Graduate Talent Pool: 73.5% degree qualified — near the highest of any Leeds postcode. Sustained pipeline of graduates who will seek to rent locally upon graduation."},
            {"level": "low",    "text": "Gross Yields 6.9–7.5% Available: Recent flat sales at £215K–£258K with estimated rents of £1,400–£1,750 offer gross yields competitive with the North West market average of ~5.5%."},
            {"level": "low",    "text": "100% Gigabit Broadband Coverage: Full-fibre gigabit internet to all premises is a premium driver for tech-sector tenants, remote workers and startups. Extremely rare for a UK postcode."},
            {"level": "low",    "text": "Crime Trend Improving — 10yr Decline: Despite current crime domain score, the decade-long downward trend signals structural improvement from investment and gentrification of the area."},
            {"level": "low",    "text": "International Demand Driver: Only 53% UK-born residents and 17.1% Middle East passport holders represents strong international occupier demand — both student and professional — providing a diverse tenant base resistant to domestic economic downturns."},
        ],

        # ── Insights ──────────────────────────────────────────────────────────
        "insights": [
            {"icon": "🎓", "title": "Strong Education Profile",         "text": "47.2% of residents hold a degree or equivalent — significantly above the UK average."},
            {"icon": "👤", "title": "Young Single Professional Demographic", "text": "71% of residents are single vs 37.9% UK average, driven by proximity to university."},
            {"icon": "💪", "title": "Healthy Young Population",         "text": "91.3% rate their health as Good or Very Good (vs UK 82%) — a clear sign of a young active population."},
        ],

        # ── Report Meta ───────────────────────────────────────────────────────
        "reportDate":   "April 2026",
        "dataSources":  "ONS - Office for National Statistics · HM Land Registry · Ofsted · UK Police",
    },


    # ─────────────────────────────────────────────────────────────────────────
    # LS6 3BN — Chapel Lane, Headingley, Leeds
    # ─────────────────────────────────────────────────────────────────────────
    "LS6 3BN": {
        "street":       "Cumberland Court",
        "area":         "Headingley",
        "ward":         "Headingley and Hyde park ",
        "constituency": "Leeds Central and Headingley",
        "civicScore":   637,
        "impactLevel":  "medium",
        "impactLabel":  "Medium Impact",
        "headlineSummary": "Headingley's student corridor with competitive 5.6–6.6% gross yields, 244 sales since 1995 and University of Leeds providing structural tenant demand year-round.",
        "breakdown": {
            "Livability":       {"score": 72},
            "Investment":       {"score": 65},
            "Infrastructure":   {"score": 75},
            "Crime & Safety":   {"score": 52},
            "Development":      {"score": 55},
            "Education":        {"score": 72},
            "Affluence":        {"score": 55},
        },

        # ── Demographics ──────────────────────────────────────────────────────
        "population": {
            "avgHHIncome":          "£42K",
            "unemploymentRate":     "3.8%",
            "degreeQualified":      "42.8%",
            "genderSplit":          "52.6% Male",
            "singleResidents":      "87.1%",
            "veryGoodHealth":       "57.3%",
            "ukBorn":               "85.8%",
            "euBornResidents":      "3.2%",
            "pakistaniCommunity":   "3.4%",
            "whiteEthnicGroup":     "82.7%",
        },

        # ── Property & Investment ─────────────────────────────────────────────
        "property": {
            "avgPrice":             "£431K",
            "streetAvg":            "£307K",
            "leedsCity":            "£294K",
            "nationalMedian":       "£322K",
            "incomeRank":           "4/10",
            "salesSince1995":       244,
            "recentSales": [
                {"address": "50 Chapel Lane (Terraced)",  "price": "£317,000", "date": "Nov 2025", "est2025": "£317,292"},
                {"address": "21 Chapel Lane (Semi-Det.)", "price": "£138,000", "date": "Oct 2025", "est2025": "£138,638"},
                {"address": "70 Chapel Lane (Terraced)",  "price": "£360,000", "date": "Dec 2024", "est2025": "£374,455"},
                {"address": "42 Chapel Lane (Terraced)",  "price": "£366,000", "date": "Sep 2024", "est2025": "£383,630"},
                {"address": "21A Chapel Lane (Terraced)", "price": "£172,000", "date": "Mar 2023", "est2025": "£193,123"},
            ],
            "roiSnapshot": {
                "avgBuyPrice":      "£307K",
                "grossYield":       "~5.8%",
                "netYield":         "~4.2%",
                "estRentalIncome":  "~£1,480/mo",
                "note":             "All property types — Chapel Lane",
            },
            "roiScenarios": {
                "conservative": {"purchasePrice": "£172,000", "stampDuty": "£6,860",  "acquisitionCosts": "£180,860", "monthlyRent": "£950",  "annualIncome": "£11,400", "grossYield": "6.6%", "netYield": "5.0%", "fiveYrCapitalGrowth": "+£37K"},
                "baseCase":     {"purchasePrice": "£317,000", "stampDuty": "£14,510", "acquisitionCosts": "£333,510", "monthlyRent": "£1,480", "annualIncome": "£17,760", "grossYield": "5.6%", "netYield": "4.2%", "fiveYrCapitalGrowth": "+£68K"},
                "optimistic":   {"purchasePrice": "£366,000", "stampDuty": "£17,480", "acquisitionCosts": "£385,480", "monthlyRent": "£1,700", "annualIncome": "£20,400", "grossYield": "5.6%", "netYield": "4.2%", "fiveYrCapitalGrowth": "+£79K"},
            },
        },

        # ── Crime ─────────────────────────────────────────────────────────────
        "crime": {
            "crimeRate":        "112.8",
            "crimeRateUnit":    "per 1,000 residents",
            "areaRanking":      "17th of 45 areas in ward",
            "leedsRank":        "922nd safest of 2,522 areas in Leeds",
            "tenYrTrend":       "-3.3%",
            "primaryCrimeType": "Violence & Sexual Offences (~64.1/1,000, rising year-on-year)",
        },

        # ── Bureau Scores ─────────────────────────────────────────────────────
        "bureauScores": {
            "Livability":      72,
            "Investment":      65,
            "Infrastructure":  75,
            "Crime & Safety":  52,
            "Development":     55,
            "Education":       72,
            "Affluence":       55,
        },

        # ── Radar Chart Data ──────────────────────────────────────────────────
        "radarData": {
            "postcode": [72, 65, 75, 52, 55, 72, 55],
            "leedsAvg": [62, 60, 68, 55, 58, 52, 57],
        },

        # ── Health ────────────────────────────────────────────────────────────
        "health": {
            "veryGood": 57.3, "good": 30.4, "fair": 9.3, "bad": 2.1, "veryBad": 0.8,
        },

        # ── Partnership Status ────────────────────────────────────────────────
        "partnershipStatus": {
            "single": 87.1, "marriedOpp": 8.2, "divorced": 3.5, "separated": 0.9, "widowed": 0.2, "sameSexOther": 0.1,
        },

        # ── Investment Phases ─────────────────────────────────────────────────
        "phases": [
            {"phase": "disruption", "title": "Phase 1 — Disruption", "period": "0–2 Years"},
            {"phase": "growth",     "title": "Phase 2 — Growth",     "period": "3–5 Years"},
            {"phase": "compound",   "title": "Phase 3 — Compounding","period": "6–10 Years"},
        ],

        # ── Risk Flags ────────────────────────────────────────────────────────
        "risks": [
            {"level": "high",   "text": "Violence & Sexual Offences Rising (Primary Crime Type): Violence and sexual offences at ~64.1 per 1,000 residents annually, rising year-on-year. This is the most significant crime risk for LS6 3BN and is particularly relevant for student and lone occupiers. Families should weigh this carefully."},
            {"level": "high",   "text": "Living Environment Deprivation 9/10 (IMD): The area scores 9/10 on the living environment domain, driven by housing quality and outdoor environment indicators. The high-density student housing stock in the LS6 belt is a key driver. Not suitable for buyers prioritising premium residential quality."},
            {"level": "medium", "text": "HMO Regulation Risk: Leeds City Council has introduced Article 4 directions in Headingley restricting new HMO conversions without planning permission. This may limit future HMO supply but could also compress yields on existing HMO stock if regulation tightens further."},
            {"level": "medium", "text": "Construction Noise & Disruption: Active development pipeline across city fringe means ongoing construction activity for 2–4 years. Premium lettings may be impacted."},
            {"level": "medium", "text": "Health Deprivation Domain 7/10: Health deprivation scores above average (7/10), which is counterintuitive given the young demographic. This may reflect chronic underlying deprivation among non-student long-term residents co-habiting the ward, and warrants monitoring."},
            {"level": "low",    "text": "Consistent University Rental Demand: University of Leeds is ranked top 10 in the UK with 38,000+ students. Headingley is the primary off-campus residential corridor, ensuring structural tenant demand year on year regardless of macroeconomic conditions."},
            {"level": "low",    "text": "Competitive Gross Yields 5.6–6.6%: Recent terraced sales at £172K–£366K with estimated rents of £950–£1,700 offer gross yields competitive with the Yorkshire average. Lower-value semi-detached properties offer particularly attractive entry points for BTL investors."},
            {"level": "low",    "text": "100% Gigabit Broadband Coverage: Full-fibre gigabit internet to all premises — a premium draw for student and young professional tenants. 100% ultrafast (300Mbit/s+) availability means zero broadband infrastructure risk for any occupier type."},
            {"level": "low",    "text": "Stable Long-Term Crime Trend: Despite the elevated violent crime rate, the overall crime level has fallen ~3.3% over the past decade. The area is ranked 922nd safest of 2,522 Leeds areas — placing it in the top 37% safest in the city."},
            {"level": "low",    "text": "Highly Educated, Active Resident Base: Over 80% of residents hold HNC-level qualifications or above (38% HNC/A-Level, 42.8% degree+). Only 7.7% have no qualifications vs 18.2% UK average. This supports stable, responsible tenancy demand."},
        ],

        # ── Insights ──────────────────────────────────────────────────────────
        "insights": [
            {"icon": "🎓", "title": "Above-Average Education Profile",       "text": "42.8% of residents hold a degree or equivalent — well above the UK average."},
            {"icon": "👤", "title": "Predominantly Single Student-Residential Demographic", "text": "87.1% of residents are single — the highest proportion in Headingley."},
            {"icon": "💪", "title": "Healthy, Young Population",             "text": "87.7% rate their health as Good or Very Good (vs UK 82%). The area has a young, active demographic."},
        ],

        # ── Report Meta ───────────────────────────────────────────────────────
        "reportDate":   "April 2026",
        "dataSources":  "ONS - Office for National Statistics · HM Land Registry · Ofsted · UK Police",
    },
}