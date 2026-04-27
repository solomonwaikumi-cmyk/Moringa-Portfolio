# 🛡️ Lab: Strategic XSS Mitigation & Bypass Analysis
**Category:** Web Application Penetration Testing | **Tools:** Burp Suite, DVWA, PHP Source Code Analysis | **Focus:** OWASP A03:2021

## 📖 Project Overview
Conducted a strategic investigation into the effectiveness of security hardening for a legacy HR management platform. Unlike standard vulnerability scans, this lab focused on analyzing **Medium** and **Impossible** security tiers to understand how specific code-level mitigations (like blacklisting vs. encoding) prevent or fail against Cross-Site Scripting (XSS) attacks.

## 🎯 Technical Objectives
* **Bypass Analysis:** Demonstrated that "Blacklisting" filters in the **Medium** security tier can be circumvented using case-variation payloads and alternative HTML events (e.g., `onerror`).
* **Source Code Review:** Identified the transition from insecure `str_replace()` logic to secure `htmlspecialchars()` functions in the PHP backend.
* **Traffic Manipulation:** Utilized **Burp Suite** to intercept and modify HTTP requests, simulating how an attacker probes for filter weaknesses.
* **Defense-in-Depth:** Documented the impact of **Anti-CSRF Tokens** and **Context-Aware Output Encoding** as primary defense mechanisms.



## 🛠️ The Analysis Workflow
1. **Low Level:** Confirmed initial exploitation of Stored/Reflected XSS.
2. **Medium Level:** Probed for filter logic; identified that the server was stripping specific tags and developed a bypass payload.
3. **Impossible Level:** Attempted multiple injection techniques and verified through source code review that input was being correctly encoded.
4. **Conclusion:** Drafted a technical report comparing the "Why" behind vulnerability prevention in modern apps.

[Link to Technical PDF Report](./Web_App_Security_Part2_Report_Solomon_Waikumi.pdf)
