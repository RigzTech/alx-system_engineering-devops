Postmortem: Web Service Outage on May 14, 2024
 
Issue Summary
 
On May 14, 2024, our web service experienced an outage that lasted for approximately 2 hours, from 14:Local time for the corresponding Julian Day within the mentioned timeline will be at a range of 16:00 UTC to 24:00 UTC. Our system went through a performance issue during which users almost faced unresponsiveness, slow connections, and intermittent downtime (about 70%).  These users were unable to access our web application and succeed in achieving their goals. The identified root cause of the issue was a configuration error in the load balancers, which did not handle requests properly due to them being improperly configured. 
 
Timeline
 
14:0000 UTC - Outage starts and faulty operation with time outs and slowness appear. 
 14:05 UTC – Primary host failure notification warns of a big 5xx error jump. 
 14:10 UTC: Engineers start their investigations paying special attention to code deployments that might have caused the recent occurrences. 
 14:At this time same day, UTC 25 roll-out plans are not hyped, instead change is geared towards infrastructure. 
 14:40 UTC - Maliciously wrongly considering a DDoS as an explosion of the safety instrument threatens to end the initial security inspection. 
 15:00 UTC - A scrutiny of the load balancer logs unveiled a peculiarity in the routing of the network traffic, thereby. 
 15:15 UTC - Incident is escalated to the NOC or a cloud provider (e. g. , Amazon Web Services). 
 15:30 UTC – AB was found to be related to the configuration error of the load balancers possibly. 
 15:fast 50 UTC - load balancer settings updated. 
 16:0 Hours, Universal Time Coordinated - Service is back to normal; monitoring shows that error rates return to normal. 
 
Root Cause and Resolution
 
An outage triggered through wrong configuration modifications to the load balancers was the exact cause. However, that grid update that was implemented has created a loophole that misdirects incoming requests to the servers that are already overloaded while others are not. 
 
The remedy entailed restoring the load balancer configurations to their previous state and, then, very carefully re-deploying the new updates with a monitoring check for every change, before progressing to additional changes. 
 
Corrective and Preventative Measures
 
To prevent similar issues in the future and improve our response to outages, the following measures are being implemented:To prevent similar issues in the future and improve our response to outages, the following measures are being implemented:
 
Improve Configuration Management: Provide that every component of deployment that is modified should be tested and verified in the staging environment before being used in production. 
 
Enhance Monitoring: Insert more measuring points for load-balancers metrics to identify the irregularities of traffic distribution. 
 
Update Incident Response Protocol: In make the incident response plan more detailed by adding a software checklist for infrastructure-related problems, for example, the load balancer error and the corresponding steps to address this issue. 
 
Conduct Training Sessions: Prepare the employee with regular training on incident handling and tract problems on the network stack. 
 
Specific Tasks
 
Patch Load Balancer Software: Be sure to get the load balancer software up to date with new security patches and performance improvements wherever possible. 
 
Add Load Balancer Monitoring: Install additional RPM on load balancer status and ameliorate thresholds on alerting deviations in traffic. 
 
Review Change Management Procedures: Modify and enrich the change management process where verification and testing by the peer are included. 
 
Incident Response Drills: Organization of the team shall be a task of the engineering team to practice drills beforehand quarterly. 


