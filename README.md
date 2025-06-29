# EcoPack---Sustainable-BI-Solution
### Business Intelligence and Analytics Systems - Final Project

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

![image](https://github.com/user-attachments/assets/8d2cbab3-0196-48cf-bc9a-44d9efd2c1de)
### **Insights**
- Provides a consolidated view of packaging cost, carbon footprint, material sustainability, and supplier ESG performance.
- Helps identify cost inefficiencies and environmental hotspots.
- Facilitates proactive compliance with EPR/ESG regulations.
- Supports strategic decision-making through scenario comparisons.

## **🎛 Filters and Control**
![image](https://github.com/user-attachments/assets/a32685dd-e548-4e29-849c-4f3b1e2dc5e7)

### **Insights**
- **Material Type Selector:** Filter by Plastic, Compostable, Recyclable or All to compare sustainability performance.
- **Record Date Slider:** Explore time-based trends for usage, emissions, and cost.
- **EPR Compliance Flag:** Focus on compliant/non-compliant materials for regulatory tracking.

## **📌 Key Metrics**
![image](https://github.com/user-attachments/assets/2b0b2497-f146-4870-a209-43133192c1f4)

### **Insights**
- Average Packaging Cost per Product: Tracks cost-efficiency and budgeting needs.
- Average Carbon Footprint: Measures average environmental impact across products.
- Total CO2 Emissions: Summarizes overall footprint and effectiveness of reduction strategies.
- These KPIs serve as quick-glance indicators of overall operational and environmental performance.

## **💰 Packaging Cost by Product**
![image](https://github.com/user-attachments/assets/8fdfbcc6-07fa-4fd0-869f-8a19fb9e2573)

### **Insights**
- **Bar Chart:** Highlights the top 5 products incurring the highest packaging costs.
- **Insight:** Prioritize optimization efforts on these high-impact products.

✅ EPR Compliance by Material Type

Bar Chart: Shows EPR performance of materials like HDPE, PET, PLA, and more.

Insight: Helps identify low-performing materials for regulatory risks and substitution planning.

🏆 Top Sustainable Supplier by ESG Score

Table View: Ranks suppliers by ESG scores and EPR compliance.

Insight: Supports vendor negotiations and selection based on sustainability values.

🌫 Emissions by Material Type

Bar Chart: Compares carbon footprint across Compostable, Recyclable, and Plastic.

Insight: Identify which materials contribute most to emissions and adjust procurement accordingly.

♻️ Plastic Usage & Recyclability Over Time

Line Chart: Displays trends in material usage (esp. recycled PET) across months.

Insight: Track the progress of recycling efforts and reduction in plastic dependency.

📊 Data Insights


Tableau Public: https://public.tableau.com/app/profile/divya.pullivarthi/viz/EcoPack_Dashboard1/Dashboard3?publish=yes












