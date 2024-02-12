# Deployment Basics with Tomcat Defaults

Tomcat supports two modes of deployment: packed and unpacked. 

- **Packed Deployment**: The entire web application is packaged in a WAR (Web ARchive) file. 
- **Unpacked Deployment**: Individual pieces are placed in a directory structure that matches the contents of a WAR file when uncompressed.

Packed deployment is generally cleaner, safer, and easier. It is the preferred method for deploying web applications. However, Tomcat supports both approaches, giving developers flexibility in deployment.

## Benefits of Packed Deployment:

- **Simplicity**: Packed deployment simplifies the deployment process and makes undeployment and redeployment straightforward.
- **Ease of Management**: Undeploying an application involves removing the WAR file, and redeploying is as simple as replacing the existing WAR file with an updated version.
- **Compatibility**: Packed deployment is compatible with other servlet containers like Jetty, making it a widely accepted standard.

## How to Deploy?

- **Build Tools**: Deployment can be automated using build tools like Ant or Maven, which provide tasks for deploying WAR files to Tomcat.
- **Integrated Development Environments (IDEs)**: IDEs such as Eclipse, NetBeans, and IntelliJ offer built-in deployment capabilities, abstracting away the complexities of deployment scripts.
- **Tomcat Scripts**: Apache Tomcat's download site provides scripts for deployment, simplifying the process for users who prefer command-line tools.

Deployment scripts provided by Apache Tomcat and IDEs streamline the deployment process, making it easier for developers to manage their applications on Tomcat servers.

