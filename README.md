# OpenFaaS Vs Azure Functions Project

Welcome to the **OpenFaaS Vs Azure Functions** project repository! This project aims to compare and contrast the performance of OpenFaaS and Azure Functions using CPU and memory-intensive workloads.

## Folder Structure

- **Functions**: This folder contains implementations of both CPU-intensive (fibonacci) and memory-intensive (matrix multiplication) codes, along with their respective Dockerfiles.
- **Jmeter Test files**: Here, you can find the load testing files designed for testing both OpenFaaS and Azure Functions.
- **Load Test Results - Dashboard**: Explore the dashboard reports that showcase the results of the load testing.

## Load Test Results Dashboard

The load test results are presented in the form of interactive dashboard reports. To view the results, follow these steps:

1. Navigate to the respective test and platform folders:
   - For Stepping thread load test: [`Stepping Thread Test Results - Dashboard`](./Load%20Test%20Results-%20Dashboards/Stepping%20Thread%20Load%20Testing)
   - For Burst load test: [`Burst Test Results - Dashboard`](./Load%20Test%20Results-%20Dashboards/Burst%20Load%20Testing)
   
   
2. Look for the `index.html` file within each folder and open it in your browser to access the interactive dashboard.

Remember that the dashboard reports will provide insights into the performance of both OpenFaaS and Azure Functions under different workloads.

## Conclusion

Through this project, we aim to provide valuable insights into the performance characteristics of OpenFaaS and Azure Functions. The load test results and interactive dashboards will help you make informed decisions based on your specific use case and workload requirements.
