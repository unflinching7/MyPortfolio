# Chiropractic Scheduling and Management System Prototype

## Project Overview
This prototype demonstrates a proof of concept for a Chiropractic Scheduling and Management System designed to optimize appointment scheduling and support decision-making for multi-location chiropractic practices. By integrating predictive analytics, data management, and actionable reporting, it enhances resource utilization, minimizes missed revenue opportunities, and improves patient satisfaction.

### Key Objectives
- **Optimize Scheduling:** Predict high-demand time slots and locations using machine learning.
- **Minimize Revenue Loss:** Identify missed opportunities and their financial impact.
- **Provide Actionable Insights:** Deliver recommendations for staffing and scheduling adjustments.
- **Demonstrate Prototype Workflow:** Use synthetic data to showcase system functionality.

---

## Project Features
- **Synthetic Data Generation:**
  - Simulates customer preferences, chiropractor availability, and appointment outcomes.
  - Data is structured, cleaned, and encoded for use in predictive models.
  
- **Predictive Analytics:**
  - Random Forest predicts slot availability.
  - Revenue impact and missed opportunities addressed through exploratory data analysis and automated reporting.

- **Insight Generation:**
  - Visualizes availability trends, revenue impacts, and missed opportunities.
  - Generates automated reports for decision-makers.

- **Decision Support:**
  - Simulates email communication to deliver actionable recommendations.

---

## Curriculum Integration
This project synthesizes foundational topics from the MS-CISBA program:

### 1. **Software Systems (SS):**
- Predictive algorithms implemented in Python.
- Automated workflows for data analysis and reporting.

### 2. **Data Management (DM):**
- Synthetic data created, stored, and processed using structured pipelines.
- Data cleaning, encoding, and preprocessing to enable machine learning.

### 3. **Business Analytics (BA):**
- Predictive insights for scheduling optimization and revenue impact analysis.
- Visualizations to highlight inefficiencies and support decision-making.

### 4. **Cybersecurity & Networking (CN) (Future Consideration):**
- Potential for secure email communication via encryption.
- Focus on data integrity and secure transfer of insights.

---

## Repository Structure
The repository is organized as follows:

### Primary Files
- **CAP.ipynb**: Google Colab notebook containing the complete prototype, including the embedded **Synthesis Paper**.

### Data
- **chiropractic_data_with_features.csv**: Enhanced synthetic data used in the prototype.

### Models
- **random_forest_model.pkl**: Pre-trained Random Forest model for availability prediction.

### Visualizations
- **availability_trends_heatmap.png**: Heatmap of predicted availability trends.
- **revenue_impact_scatter.png**: Scatterplot of predicted vs. actual revenue impact.


### Presentations
- **slides.pdf**: Final presentation slides summarizing the project.
- **demo_video_link.tx**: Link to video demonstration of the system workflow and outputs.



---

## Results and Visualizations
### 1. Predicted Availability Trends
- Identifies high-demand slots and locations, aiding scheduling decisions.

### 2. Revenue Impact Analysis
- Highlights potential financial losses from missed opportunities.


---

## Additional Resources
## Synthesis Paper: Included in the Colab notebook, explaining curriculum integration and project relevance.
- Video Presentation: Demonstrates the system's workflow and functionality.
- Slides: Summarizes the project for presentation purposes.

---

## Future Enhancements
- Incorporate real-world data to validate and refine predictive models.
- Implement encryption for secure email communication.
- Extend the system to include real-time updates and a user interface for broader usability.