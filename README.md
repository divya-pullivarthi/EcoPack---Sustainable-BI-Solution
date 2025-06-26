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

## **2. Preprocessing**

All preprocessing steps—including cleaning, transformation, and validation—were implemented in the Data_Preprocessing.py file, which is available in this repository.

### **Data Quality Checks**
| Column Name	 | Quality Check | 
|:-----------|:------------:|
| Missing Values | No cells are empty |
| record_date | Format validation (YYYY-MM-DD), no future dates, not null |
| product_id | Uniqueness check, not null |
| supplier_id | Valid values (S1-S10), referential integrity with supplier_name |
| material_weight_kg | Numeric range (≥0), not null |
| packaging_cost_usd | Numeric range (≥0), outlier detection |
| recyclable_pct | 0-100, not null |
| epr_compliant | Only 'Y' or 'N' |

2.  Data Quality Checks
Column Name		Quality Check
Missing Values	No cells are empty
record_date		Format validation (YYYY-MM-DD), no future dates, not null
product_id	Uniqueness check, not null
supplier_id	Valid values (S1-S10), referential integrity with supplier_name
material_weight_kg	Numeric range (≥0), not null
packaging_cost_usd	Numeric range (≥0), outlier detection
recyclable_pct	0-100, not null
epr_compliant	Only 'Y' or 'N'

3. Data Transformation Rules
Source Column	Transformation Rule	Target Column
record_date	Standardize date format to YYYY-MM-DD across all rows	record_date
epr_compliant	Convert 'Y' to TRUE and 'N' to FALSE for boolean compatibility	is_epr_compliant
material_type	Capitalize first letter only (e.g., 'Plastic', 'Compostable') for consistency	material_type
material_weight_kg	Round to two decimal places to ensure numeric consistency	material_weight_kg
packaging_cost_usd	Validate that all values are positive; flag if negative or zero	packaging_cost_usd
supplier_esg_score	Ensure float values are retained; no transformation if already clean	supplier_esg_score
product_id, supplier_id	Use as foreign keys for joining with product and supplier dimension tables	product_id, supplier_id
















Key transformations include:

Dates standardized (YYYY-MM-DD)

Weights and costs validated (non-negative)

Recyclable % and ESG scores normalized
