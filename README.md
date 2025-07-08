# EcoPack---Sustainable-BI-Solution
### Still Editing this in the github - Business Intelligence and Analytics Systems - Final Project

## **🌍 Introduction / Background**

The global packaging industry, valued at over $1 trillion in 2023, is under pressure due to its role in plastic pollution, with plastic packaging alone accounting for 46% of global plastic waste (UNEP, 2021). With more than 141 million tonnes of plastic packaging waste generated annually, governments and consumers are demanding urgent action (OECD, 2022).

Retailers and e-commerce platforms that rely heavily on plastic-heavy secondary and tertiary packaging are key contributors. Consumers are shifting toward eco-conscious choices, with 74% stating they are willing to pay more for sustainable packaging (McKinsey, 2022). Regulatory actions like the EU Single-Use Plastics Directive and India’s plastic ban are accelerating the need for smarter packaging strategies.

EcoPack is a data-driven platform designed to help companies make informed, sustainable packaging decisions. It uses cloud computing, AI, and lifecycle analysis to suggest cost-effective, environmentally responsible alternatives.

## **🎯 Business Objective**

EcoPack empowers retailers and consumer brands to:

Map and assess current packaging material types and volumes.

Identify inefficiencies or overuse of non-sustainable materials.

Model and compare eco-friendly alternatives using lifecycle impact analysis.

Reduce environmental footprint while maintaining brand value.

### **Benefits include:**

Lower supply-chain costs via reduced material waste.

Improved regulatory alignment (EPR, ESG).

Enhanced brand perception and customer loyalty.

Measurable progress toward corporate sustainability goals.

EcoPack transforms packaging into a strategic differentiator that benefits both business and the planet.

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
![image](https://github.com/user-attachments/assets/a0b94b4e-5765-4dca-a1c8-6d1da184bedd)

### **Insights**
This interactive dashboard offers a rounded and comprehensive view of EcoPack’s sustainable packaging initiatives. It .was designed to assist its team decision-makers in procurement, sustainability, and product management to track relevant metrics, observe trends, and ultimately make data-driven decisions. The dashboard combines data related to financial costs, environmental benefits (e.g., CO2 emissions), legal compliance (e.g., EPR), and supplier performance (e.g., ESG) to help EcoPack seemingly juggle its environmentally responsible goals and objectives with its business asset objectives. Users can dynamically filter the entire dashboard by material type and time period and they can also interact with the various graphs to filter the data to narrow down to specific areas to identify root causes, and monitor the impact of the corporate sustainability initiatives over time.

This dashboards in short helps by:
- Provides a consolidated view of packaging cost, carbon footprint, material sustainability, and supplier ESG performance.
- Helps identify cost inefficiencies and environmental hotspots.
- Facilitates proactive compliance with EPR/ESG regulations.
- Supports strategic decision-making through scenario comparisons.

## **🎛 Interactive Filters and Control**
![image](https://github.com/user-attachments/assets/1728e717-2958-43c4-b375-ee57a8c9d9a3)

### **Insights**
At the top of the dashboard, users are presented with the main filters and controls:

- **Material Type:** Allows users to focus the analysis on (All), Compostable, Plastic, or Recyclable materials.
- **Date Range (Start/End Month):** Enables analysis of specific time periods, from January 2023 to December 2024.
- **EPR_Flag:** A color legend that visually segments data based on Extended Producer Responsibility (EPR) compliance status.

## **📌 Key Performance Indicators (KPIs)**
These cards provide an at a glance summary of the most critical metrics for the selected period.
![image](https://github.com/user-attachments/assets/86ebaf67-290e-4f40-9775-e219a60b190c)

### **Insights**

- **Avg. Packaging Cost per Product:** Shows the average financial cost associated with packaging for each product. So it tracks cost-efficiency and budgeting needs.
- **Average Carbon Footprint:** Displays the average carbon footprint  per product or package. It measures average environmental impact across products.
- **Total CO2 Emissions:** Aggregates the total carbon dioxide emissions footprints, providing a measure of the overall environmental impact and effectiveness of reduction strategies.

These KPIs serve as quick-glance indicators of overall operational and environmental performance.

## **💰 Packaging Cost by Product**
![image](https://github.com/user-attachments/assets/ad6a49f1-83d7-4486-8e70-118e6836346e)

### **Insights**
The individual products (e.g., P14, P10, P8) are represented in the vertical bar chart to rank packaging costs collectively. This allows the viewer to see what packaging costs are highest and could form the basis for a cost-reduction strategy or associated cost-optimization initiatives. The color scale associated with the products is consistent with the EPR_Flag, which could reflect a link between cost and compliance.

## **✅ EPR Compliance by Material Type**
![image](https://github.com/user-attachments/assets/b176a046-c976-418c-bf94-74a8563bc859)

### **Insights**
This bar chart shows the Extended Producer Responsibility (EPR) compliance rates for each packaging material (i.e., Aluminum, Glass, HDPE, LDPE). These elements are important to consider to assess regulatory risk and determine whether the materials you are using are legal and compliant with corporate standards. Insights showed that materials like bagasse had much lower compliance than glass or corrugated materials.

## **🏆 Top Sustainable Supplier by ESG Score**
![image](https://github.com/user-attachments/assets/e86d4cdb-5358-480a-9f5c-9b0f0d4cd294)

### **Insights**
This table shows the ranking of suppliers based on their Environmental, Social, and Governance (ESG) score. It offers a valuable view of the sustainability outcome of the supply chain. It will highlight top performers like GreenPlast and RecycleWorks to help in sourcing the right supplier and developing partnership with environmentally friendly suppliers.
We can use this graph to support vendor negotiations and select them based on the sustainability values.

## **🌫 Emissions by Material Type**
![image](https://github.com/user-attachments/assets/6694cb0a-859f-413c-99c6-637ced458eff)

- **Bar Chart:** Compares carbon footprint across Compostable, Recyclable, and Plastic.
- **Insight:** Identify which materials contribute most to emissions and adjust procurement accordingly.

## **♻️ Plastic Usage & Recyclability Over Time**

- **Line Chart:** Displays trends in material usage (esp. recycled PET) across months.
- **Insight:** Track the progress of recycling efforts and reduction in plastic dependency.

**📊 Data Insights**


Tableau Public: https://public.tableau.com/app/profile/divya.pullivarthi/viz/EcoPack_Dashboard1/Dashboard3?publish=yes












