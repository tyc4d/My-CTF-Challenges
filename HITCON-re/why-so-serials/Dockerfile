# escape=`
FROM mcr.microsoft.com/dotnet/framework/aspnet:4.8

SHELL ["powershell"]

COPY src /inetpub/wwwroot/whysoserial
 RUN Remove-WebSite -Name 'Default Web Site'
 RUN New-Website -Name 'whysoserial' -Port 80 `
     -PhysicalPath 'c:\inetpub\wwwroot\whysoserial' -ApplicationPool '.NET v4.5'
EXPOSE 80

ENTRYPOINT ["C:\\ServiceMonitor.exe", "w3svc"]