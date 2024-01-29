# nsgssimple

This repository has Site24x7 Azure functions for collecting logs from Microsoft Azure Blob Storage and Event Hubs, along with Azure ARM templates for automated deployment.

| Function | Description |
|---|---|
| [Site24x7 Azure Event Hub Function](BlobForwarder) | Collects and forwards Azure diagnostics logs from Event Hub to Site24x7 AppLogs. |
| [Site24x7 Azure Nsg Flow log Function](NsgFlowLogsForwarder) | Collects and forwards Azure NSG Flow logs from Azure Blob Storage to Site24x7 AppLogs. |

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Faneshpugal%2Fnsgssimple%2Fmain%2FNewTemplate.json)

