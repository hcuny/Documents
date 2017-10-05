Auther: **Cunyuan(Anthony) Huang**

## Overview
This is a document for overall code usage of intern project "**Anomaly Detection in System Signals**". It included descriptions of main code pieces written for this project both in R and Python, overview of some other explorations is also provided. Detailed information can be found within scripts. 

## Part 1: Univariate Anomaly Detection
### 1.1 Time series forecast 
#### Python File: 
 > **day_tot.py**: lstm model for daily queue volume metric.
 > **day_qv.py**: lstm model for daily queue volume metric.
 > **hour_qv.py**: lstm model for hourly queue volume metric.

- Prerequisites: 
> python version 3.5+ 
> Build on tensorflow, keras 
- Input File: ts906.csv(daily), ts_hour_911.csv(hourly)
- Output File: Model prediction results to be saved in local environment
- Command line Usage:
```
usage: python ~.py input_path output_path
```
Note: the structure and methodology of 3 files are similar, all implemented LSTM forecasting for metrics. Since many details including features, time windows, NN structures need to be changed, so they are written in seperate scripts.
#### R File:
> **queue_v_hour.R**: hourly total queue metric. 
> **total_order.R**: daily total order metric. 
> **total_queue.R**: daily total queue metric.
- Input File: ts906.csv(daily), ts_hour_911.csv(hourly)
- Output File: Prediction results for different methods, uploaded in dataset section.

Note: The structure of the 3 scripts are similar, both implemented different models in R, including STLM, different versions of Holt-Winters, and online ensembling in Opera.
> Usage: install required R package, change the path variable and directly run scripts.


## Part 2: EWS Clustering Analysis
#### Python File: EWS_clustering.ipynb

- Input File: ts_hour_929_vcnc.csv
- Usage: Change the path variable and directly run scripts.
## Part 3: Anomaly Deep Dive
#### Python File: KLDivergence.ipynb
- Input File: 
> USpd_pm_queue.csv: payment method daily top.
> USpd_gl_queue.csv: GL groups daily top.
> USpd_asins_queue.csv: ASINS daily top.
> asin_match.pkl: ASINS code to name match table.

- Usage: Change the path variable and directly run scripts.
## Part 4: Others
> Data extraction and feature engineering: data_re_extraction.ipynb
> Holiday season features and visualization: Holiday_Growth_Exp.ipynb
> Explotary data analysis: EDA.ipynb
> Model comparison & visualization: compare.ipynb
> Seasonal ARIMA modeling: SARIMAX.ipynb
> Queue volume forecast US digital: qv_USDD.R
> Queue rate short term forecast:queue_rate_short_term.R
