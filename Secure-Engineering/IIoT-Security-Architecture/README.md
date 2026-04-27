# 🏭 Lab: IIoT Architecture & Predictive Maintenance
**Category:** Industrial Cybersecurity / IoT Engineering | **Stack:** MQTT, Python, AWS IoT, ESP32

## 📖 Project Overview
Designed a comprehensive **Industrial Internet of Things (IIoT)** system for *Precision Manufacturing Inc.* to solve equipment downtime and energy inefficiency. This project focuses on the intersection of real-time sensor data and secure industrial communication.

## 🎯 System Objectives
* **Predictive Maintenance:** Utilizing temperature and vibration sensors to detect failures before they happen.
* **Energy Optimization:** Automated power reduction for idle machinery via industrial relays.
* **Remote Monitoring:** A centralized dashboard for real-time visibility into factory health.

## 🛠️ The Architecture
* **Edge Layer:** ESP32 microcontrollers connected to Thermocouples (Temp) and Accelerometers (Vibration).
* **Gateway Layer:** Industrial Raspberry Pi / NVIDIA Jetson Nano running **Edge Computing** to process data locally before sending it to the cloud.
* **Connectivity:** **MQTT Protocol** for low-latency, lightweight data transmission over Wi-Fi/LoRaWAN.
* **Cloud Layer:** AWS DynamoDB for logging and React.js for the frontend dashboard.

## 🛡️ Security Measures (The "Cyber" Layer)
* **Encryption:** Implemented **AES-256** for data at rest and **TLS/SSL** for data in transit.
* **Access Control:** Role-Based Access Control (RBAC) to ensure only authorized engineers can trigger maintenance actions.
* **Maintenance:** **FOTA (Firmware Over-the-Air)** updates to ensure devices receive security patches without manual intervention.

[Link to Full Architecture Report](./IIoT_Predictive_Maintenance_Security_Architecture.pdf)
