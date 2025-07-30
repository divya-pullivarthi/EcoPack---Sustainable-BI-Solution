# EcoPack---Sustainable-BI-Solution
### Still Editing this in the github - Business Intelligence and Analytics Systems - Final Project

## **🌍 Introduction / Background**

The global packaging industry, valued at over $1 trillion in 2023, is under pressure due to its role in plastic pollution, with plastic packaging alone accounting for 46% of global plastic waste (UNEP, 2021). With more than 141 million tonnes of plastic packaging waste generated annually, governments and consumers are demanding urgent action (OECD, 2022).

Retailers and e-commerce platforms that rely heavily on plastic-heavy secondary and tertiary packaging are key contributors. Consumers are shifting toward eco-conscious choices, with 74% stating they are willing to pay more for sustainable packaging (McKinsey, 2022). Regulatory actions like the EU Single-Use Plastics Directive and India’s plastic ban are accelerating the need for smarter packaging strategies.

EcoPack is a data-driven platform designed to help companies make informed, sustainable packaging decisions. It uses cloud computing, AI, and lifecycle analysis to suggest cost-effective, environmentally responsible alternatives.

## **🎯 Business Objective**

EcoPack empowers retailers and consumer brands to:

- Map and assess current packaging material types and volumes.
- Identify inefficiencies or overuse of non-sustainable materials.
- Model and compare eco-friendly alternatives using lifecycle impact analysis.
- Reduce environmental footprint while maintaining brand value.

### **Benefits include:**

- Lower supply-chain costs via reduced material waste.
- Improved regulatory alignment (EPR, ESG).
- Enhanced brand perception and customer loyalty.
- Measurable progress toward corporate sustainability goals.
- EcoPack transforms packaging into a strategic differentiator that benefits both business and the planet.

## **⚡ Current Situation and Opportunity Statement**

Most retailers and e-commerce firms currently lack a data-driven system to evaluate the sustainability and efficiency of their packaging. They depend on manual, fragmented, or supplier-dependent insights, which fail to reflect the environmental impact accurately.

EcoPack solves this by integrating internal packaging data, lifecycle analysis, and sustainability benchmarks. It helps businesses identify inefficiencies (like overuse, recyclability gaps, and high emissions) and simulate sustainable alternatives that align with environmental and economic goals. This supports regulatory compliance, brand value, and cost savings.

## **🧱 Data Architecture & Flow**

### **Data Approach for This Project:**

Since no real-world dataset was available, all data for this project was synthetically created based on thorough research to reflect realistic packaging-related scenarios. Therefore, traditional multi-source ingestion like ERP or CRM systems was not used.

### **Process (in project simulation context):**

Data Creation → Preprocessing & Cleaning → Data Modeling (Star Schema) → Visualization (Dashboard)

This simulated flow reflects how a real-world pipeline would behave using structured business packaging data.

## **🔄 Data Lifecycle**

### **1. Data Creation**

Due to the unavailability of real-world datasets, synthetic data was created based on research to simulate realistic packaging-related scenarios.

### **2. Preprocessing**

All preprocessing steps—including cleaning, transformation, and validation—were implemented in the Data_Preprocessing.py file, which is available in this repository.

### **Data Quality Checks**
| Column Name	 | Quality Check | 
|:-----------|:------------:|
| Missing Values | No cells are empty |
| record_date | Format validation (YYYY-MM-DD), no future dates, not null |
| product_id | Uniqueness check, not null |
| supplier_id | Valid values (S1-S10), referential integrity with supplier_name |
| material_weight_kg | Numeric range (≥0), not null |
| packaging_cost_usd | Numeric range (≥0) |
| recyclable_pct | 0-100, not null |
| epr_compliant | Only 'Y' or 'N' |


### **3. Data Model**

#### **Data Source and Structure:**
The dataset used in this project is synthetically generated based on extensive research and industry knowledge, rather than sourced from existing ERP or supplier systems. As a result, the data is currently structured as a single flat table combining both descriptive attributes (dimensions) and measurable metrics (facts). This approach simplifies data creation and allows for rapid prototyping of the BI solution. Future iterations may involve creating normalized fact and dimension tables if real-world source systems become available.

#### **Conceptual Fact and Dimension Fields**
Although the current dataset is a single table, we can logically separate the fields into star schema with one fact table and several dimension tables:

#### **3.1 Fact Table**
**Packaging_Fact**
| Column Name	 | Description | 
|:-----------|:------------:|
| product_id | Foreign Key → Product_Dim |
| supplier_id | Foreign Key → Supplier_Dim |
| material | Foreign Key → Material_Dim |
| record_date | Foreign Key → Date_Dim |
| material_weight_kg | Total weight of material used |
| packaging_cost_usd | Cost of packaging |
| recyclable_pct | Percent recyclable |
| carbon_footprint_kg | Environmental impact |
| cost_savings_usd | Cost savings from switching materials |

#### **3.2 Dimension**
**Product_Dim**

| Column Name	 | Description | 
|:-----------|:------------:|
| product_id | Unique ID for each SKU |
| product_name | Name of the product |

**Supplier_Dim**

| Column Name	 | Description | 
|:-----------|:------------:|
|supplier_id	| Unique ID for supplier |
| supplier_name	| Supplier’s name |
| supplier_esg_score	| Environmental/Social score |
| epr_compliant	| Y/N regulatory compliance status |

**Material_Dim**

| Column Name	 | Description | 
|:-----------|:------------:|
| material	| Type of packaging material |
| material_type |	Classification (Plastic, Compostable, etc.) |

**Date_Dim**

| Column Name	 | Description | 
|:-----------|:------------:|
|record_date	| Actual date of packaging record |
| month	| Derived month |
| year	| Derived year |

## **📊 Dashboard Descriptions & Insights**

The EcoPack dashboard was designed to provide business stakeholders and sustainability teams with rich, actionable insights. It allows users to make informed decisions about packaging strategies, reduce environmental impact, and optimize supplier choices. Here's a detailed breakdown of each component:

## **🔍 Dashboard**
<img width="3299" height="1845" alt="image" src="https://github.com/user-attachments/assets/75c8c258-2fc4-4f4d-a976-6759bf32b8d5" />

### **Insights**
This interactive dashboard offers a rounded and comprehensive view of EcoPack’s sustainable packaging initiatives. It was designed to assist its team decision-makers in procurement, sustainability, and product management to track relevant metrics, observe trends, and ultimately make data-driven decisions. The dashboard combines data related to financial costs, environmental benefits (e.g., CO2 emissions), legal compliance (e.g., EPR), and supplier performance (e.g., ESG) to help EcoPack seemingly juggle its environmentally responsible goals and objectives with its business asset objectives. Users can dynamically filter the entire dashboard by material type and time period and they can also interact with the various graphs to filter the data to narrow down to specific areas to identify root causes, and monitor the impact of the corporate sustainability initiatives over time.

This dashboards in short helps by:
- Provides a consolidated view of packaging cost, carbon footprint, material sustainability, and supplier ESG performance.
- Helps identify cost inefficiencies and environmental hotspots.
- Facilitates proactive compliance with EPR/ESG regulations.
- Supports strategic decision-making through scenario comparisons.

## **🎛 Interactive Filters and Control**
<img width="1206" height="293" alt="image" src="https://github.com/user-attachments/assets/3a528f2f-5720-4e97-aa04-4567e3fc0140" />

### **Insights**
One of the key features of this dashboard is that it is completely interactive and can therefore be analyzed and explored in a deeper way. This can be done in two ways:

- **Global Filters:** It is simple to govern the scope of the entire dashboard using the easy to use controls at the top of the view including:
    - **Material Type:** Allows users to focus the analysis on (All), Compostable, Plastic, or Recyclable materials.
    - **Date Range (Start/End Month):** Enables analysis of specific time periods, from January 2023 to December 2024.
    - **EPR_Flag:** A color legend that visually segments data based on Extended Producer Responsibility (EPR) compliance status.
    - **Supplier Name:** A dropdown menu that allows filtering the entire dashboard for one or more specific suppliers.
      
- **Action Filters:** In addition to global controls, the dashboard uses action filters to support interaction across charts. Clicking on a data point in any chart (e.g. clicking 'Plastic' in the Emissions by Material Type, or clicking 'P14' in the Packaging Cost by Product) will instantly filter all other visualizations. This powerful aspect of the dashboard enables the user to isolate a specific product, material, or supplier and instantly see how it is performing across all other metrics in the dashboard, from ESG scores to monthly usage trends.

## **📌 Key Performance Indicators (KPIs)**
These cards provide an at a glance summary of the most critical metrics for the selected period.
<img width="2070" height="250" alt="image" src="https://github.com/user-attachments/assets/ae540545-1b18-4d91-9f9e-3761a24faf6b" />

### **Insights**

- **Avg. Packaging Cost per Product:** Shows the average financial cost associated with packaging for each product, which is currently $133.30. So it tracks cost-efficiency and budgeting needs.
- **Average Carbon Footprint:** Displays the average carbon footprint per product or package, currently at 2.353. It measures average environmental impact across products.
- **Total CO2 Emissions:** Aggregates the total carbon dioxide emissions footprints, currently 4,481, providing a measure of the overall environmental impact and effectiveness of reduction strategies.

These KPIs serve as quick-glance indicators of overall operational and environmental performance.

## **💰 Packaging Cost by Product**
<img width="767" height="604" alt="image" src="https://github.com/user-attachments/assets/e3506631-7904-476d-8184-8c3c133e39b5" />

### **Insights**
The individual products (e.g., P14, P10, P8) are represented in the horizontal bar chart to rank packaging costs collectively. This allows the viewer to see what packaging costs are highest and could form the basis for a cost-reduction strategy or associated cost-optimization initiatives. Product P14 stands out as the most expensive at $19,785.78. The color scale associated with the products is consistent with the EPR_Flag, which could reflect a link between cost and compliance.

## **✅ EPR Compliance by Material Type**
<img width="1472" height="575" alt="image" src="https://github.com/user-attachments/assets/8d2c0235-2b83-442f-8f71-8cd3cf95bc5d" />

### **Insights**
This bar chart shows the Extended Producer Responsibility (EPR) compliance rates for each packaging material (i.e., Aluminum, Bagasse, Corrugated, Glass, HDPE, LDPE, etc.). These elements are important to consider to assess regulatory risk and determine whether the materials you are using are legal and compliant with corporate standards. Insights showed that materials like Bagasse (at 29.2%) had much lower compliance than Glass (74.7%) or Corrugated cardboard (71.0%).

## **🏆 Top Sustainable Supplier by ESG Score**
<img width="1024" height="455" alt="image" src="https://github.com/user-attachments/assets/d1fddefa-b60c-4ddd-a62d-279eb5ceaf95" />

### **Insights**
This table shows the ranking of suppliers based on their Environmental, Social, and Governance (ESG) score. It offers a valuable view of the sustainability outcome of the supply chain. It will highlight top performers like GreenPlast (28,566) and RecycleWorks (20,567) to help in sourcing the right supplier and developing partnership with environmentally friendly suppliers.
We can use this graph to support vendor negotiations and select them based on the sustainability values.

## **🌫 Emissions by Material Type**
<img width="1026" height="961" alt="image" src="https://github.com/user-attachments/assets/09b16a85-ce8d-49b9-87b9-f93836197ae1" />

### **Insights**
The bar chart is relatively simple but effective and is a good breakdown of total emissions by broad material categories: Compostable, Plastic, and Recyclable. The chart indicates that Plastic is the highest contributing category at 2,412 units of emissions in this view, and therefore should be prioritized for reduction.

## **📈 Material Usage & Sustainability Performance**
<img width="2260" height="811" alt="image" src="https://github.com/user-attachments/assets/58c5b177-f30e-4ae1-8381-1002dac12b21" />

### **Insights**
This dual-axis combination chart provides a time-series analysis of material usage and a key sustainability metric from January 2023 to December 2024.
- **Stacked Area Chart (Left Axis - Material Weight Kg):** This chart visualizes the total weight of packaging material used each month, broken down by type: Compostable (light blue), Plastic (gray), and Recyclable (green). It clearly shows the mix and volume of materials over time.
- **Line Chart (Right Axis - Weighted Avg. Rate %):** The dark line tracks a key performance indicator, such as the weighted average recyclability or compliance rate, across the same period.

This visualisation aims to showcase the relationship between material consumption and sustainability performance. Stakeholders can track how shifts in the material mix (e.g., reducing gray plastic area, increasing green recyclable area) affect the overall sustainability rate shown by the dark line. This allows for long-term pattern recognition and monitoring the impact of environmental initiatives.

## **📊 Dashboard Overall Insights as a Analyst**
The true power of the EcoPack dashboard lies in its interactivity. By applying filters, an analyst can move beyond high-level summaries to uncover deep, actionable insights and answer critical business questions. The following scenarios demonstrate how the dashboard facilitates this analysis.

### **Insights 1: The Plastic Dilemma - Low Cost, High Environmental Price**
When we filter the dashboard to show only Plastic materials, the core problem becomes immediately clear.

<img width="3301" height="1838" alt="image" src="https://github.com/user-attachments/assets/31d6e219-d58e-4f21-8f52-413899f8bdc2" />

- **The Story:** Plastic is, by far, our worst environmental offender. The Average Carbon Footprint skyrockets to 3.330 (the highest of any category), and it contributes a massive 1,046 units to our Total CO2 Emissions.
- **The Why:** The Avg. Packaging Cost per Product at $121.60 is moderate, making it a financially tempting option. This creates a direct conflict between cost management and sustainability goals.
- **Critical Finding:** The Material Usage & Sustainability Performance chart shows that the Weighted Avg. Rate (representing sustainability/compliance) fluctuates but remains low. The EPR Compliance chart confirms this, with materials like LDPE showing very low compliance (36.61%).
- **Actionable Conclusion:** Our primary target for reduction must be plastic. The data allows us to be specific, focusing first on replacing low-compliance and high-emission plastics like LDPE, while investigating if higher-compliance plastics like HDPE (63.10%) can serve as a temporary bridge.

### **Insights 2: The Trade-off of Compostable & Recyclable Filters**
If plastic is the problem, what is the best solution? By filtering between Compostable and Recyclable materials, the dashboard reveals a crucial strategic trade-off.

#### **The Compostable Option: Low Cost, Low Carbon, High Risk**

<img width="3295" height="1843" alt="image" src="https://github.com/user-attachments/assets/3f2e5832-9435-4802-ad25-909fea5ecd78" />

- **The Upside:** Compostables are our cheapest alternative ($116.75 Avg. Cost) and have the lowest carbon impact (1.376 Avg. Carbon Footprint).
- **The Downside:** They carry significant regulatory risk. The EPR Compliance for Bagasse is extremely low at 32.74%. This could expose the company to fines or brand damage.

#### **The Recyclable Option: High Cost, High Compliance, Good-Enough Carbon**

<img width="3308" height="1843" alt="image" src="https://github.com/user-attachments/assets/a5c05ec9-733d-4b70-95b5-a56e6b3166d4" />

- **The Upside:** Recyclables are our safest bet from a regulatory standpoint. Materials like Glass (78.38%) and Corrugated (77.01%) boast high EPR compliance, and the Weighted Avg. Rate in the time-series chart is consistently high and stable.
- **The Downside:** This safety comes at a price. Recyclables are the most expensive category, with an Avg. Packaging Cost of $145.10.
- **Actionable Conclusion:** The dashboard doesn't give one "right" answer; it frames the strategic choice. Do we pursue the low-cost, low-carbon compostable route and focus on mitigating the compliance risk? Or do we invest in the more expensive but "safer" recyclable materials to guarantee compliance? This data empowers leadership to make a fully informed decision.

### **Insight 3: Drilling Down to Supplier Performance**
Beyond material types, we can assess the performance of a specific partner. Filtering the dashboard for a single supplier, like ClearCycle, allows for targeted analysis and vendor management.

<img width="3293" height="1840" alt="image" src="https://github.com/user-attachments/assets/0db290c8-abce-46fa-8c74-94f51d523c80" />

- **The Story:** A quick look at the KPIs for ClearCycle shows they are a very expensive supplier ($160.82 Avg. Cost), with a relatively high carbon footprint (2.573).
- **The Material Mix:** The EPR Compliance chart reveals why. ClearCycle supplies us with both highly compliant materials like Glass (100%) and very low-compliance materials like Bagasse (26.3%). Their emissions are driven primarily by the plastic they supply.
- **Actionable Conclusion:** This view provides concrete data for supplier negotiations. We can approach ClearCycle with specific questions:
    - Why are your overall costs so high compared to the market average?
    - Can we work together to phase out the high-risk Bagasse from your supply?
    - What are the alternatives for the high-emission plastic you provide?

This turns a general sustainability goal into a specific, data-driven conversation with a partner.

## **Tableau Public:**
https://public.tableau.com/views/EcoPack_Dashboard1/Dashboard3?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## **📌 Author**
Divya Pullivarthi

Project completed for course IS 574: Business Intelligence and Analytics Systems

LinkedIn










