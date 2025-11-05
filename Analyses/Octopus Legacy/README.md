# 🧭 Octopus Legacy - Deals Deep Dive


### 🎯 Goal & Scope
This exploratory data analysis (EDA) investigates Octopus Legacy’s operational and commercial data to reveal patterns, trends, and opportunities. 
The focus is **diagnostic/explanatory** (what is happening and why), not predictive. We summarise performance, identify drivers, and surface issues that impact decision‑making.

### 🧩 Executive Summary
This analysis uncovers key performance trends and lead-generation insights for Octopus Legacy between July and October 2025. The data reveals strong growth in deals, a concerning loss rate at closure, and distinct differences across acquisition channels and product categories. 
Actionable opportunities include improving conversion at closing, replicating September’s organic growth, and leveraging upselling potential from Will purchases. Data quality was also a core issue throughout this analysis suggesting we need to improve data infrastructure and on the ground consultant processes. 

### 📊 Key Findings
- **Rising activity trend:** Revenue could increase 200% from **July to October**, peaking at the **end of October**, suggesting strong campaign-driven demand.  
- **High loss rate:** Of all closed deals, **61% were lost**, indicating a major friction point. This should be a **priority area for investigation**. This could be linked to **pricing competitiveness** or **customer experience bottlenecks**.  
- **Channel mix insights:**  
  - **Charity leads** account for **44% of total leads**, highlighting valuable partnerships, though we’ll want to check  if its cost effective.  
  - **Pay-per-click (PPC)** contributes **32% of leads**, suggesting healthy pipeline volume but also a **potential over-reliance on paid acquisition** due to low brand recognition.  
  - **Organic leads surged by 59% from August to September**, a key success worth **replicating and analysing for cause** (e.g., SEO, content, or partnerships).  
- **Product performance:**  
  - **Wills** dominate sales volume — the most frequently sold but **lowest-value product**, suggesting **strong entry-level appeal** with **upsell potential**.  
  - **Affiliates** generate the **highest average order value (£794)**, followed by **Organic (£680)**, while **Charity** has the **lowest (£528)**. This indicates **channel-specific quality differences** worth leveraging in campaign targeting.  
- **Opportunities:**  
  - Investigate **why Close losses spike at closing stage**.  
  - **Learn from organic success** in September.  
  - **Develop an upsell strategy** targeting customers who purchase Wills.  
  - **Rebalance lead acquisition** towards more cost-efficient, higher-value channels.

### 📈 Metrics Recommondations
- **⭐️ Average Order Value (AOV):**
    - Definition: Average Revenue generated from total line items in an order
    - Why track it? Informs us of the value of transactions over different segments (Lead Source, Customer Segments) and whether any interventions (Such as an AB test) could lift spending per order.
    - Formula: AVG(SUM(line_item_revenue) OVER (PARTITION BY deal_id))

- **⭐️ Deal Conversion Rate (DCR):**
    - Definition: The % of deals which are successfully purchased following document preparation. This is based on volume.
    - Why track it? Helps identify any customer friction around time of purchase and benchmarks consultant performance
    - Formula: COUNT(Successful Deals) / COUNT(Prepared Documents)

- **⭐️ Acquisition Costs (AC):**
    - Definition: The £ needed in order to acquire 1 customer
    - Why track it? Informs us of the value of different marketing channels so that we can better allocate budget
    - Formula: SUM(Marketing & Sales Spend) / COUNT(Number of customers)


#### The Long term vision:
- **⭐️ North Star Metrics**: We'd want to create a handful of KPIs across departments which inform whether our interventions are benefitting the team.
- **🎄 Metric Tree**: Combine these departmental metrics into a hierarchy. Leading indicators at the bottom of the tree feed into the top. These allow us to see what interventions are making an impact on the business and to what extent.

### 🚨 Data Quality Issues 🚨

- Free field text leading to inaccurate data:
  -  lead_city
  - product_name

- Potential Bugs:
  - `current_deal_stage_entered_at` anomalous volumes on 2025-10-28. Will need investigation
  - Possible product duplication: some deals (e.g., deal_id 524223) include multiple wills per purchase likely input error, though no refund patterns suggest customers were correctly charged.
  - Missing line items in Closed Won deals: some completed deals lack associated items, which undermines revenue accuracy and must be investigated immediately before reporting continues.
  
- Potential Process Bugs:
  - Appointments show process issues: some deals progress or close before appointments occur, likely due to admin backlogs or multiple bookings per deal — needs consultant feedback to confirm causes.

#### Solutions
- Drop down options for consultants or pre-filled city.
- Setting up dbt alerts to identify issues sooner as well as dedicated time for data cleaning our models.
- Meeting with consultants to understand process pain points and reasons behind data entry.
- Dedicated data modelling time to strengthen staging models.
- Provide data training to spread awareness of shared data accountability. 

### Miscellaneous
- Google Sheets document can be found here:
https://docs.google.com/spreadsheets/d/11PPZhg9DnRUcE6piqqyU9Am97hEsHyO0olbUxEiVB0g/edit?usp=sharing

## 👤 Author
**Guy Winfield** 

## 🗓 Version History
- 0.1 Initial EDA README for Octopus Legacy