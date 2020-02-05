from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class GCPLauncherExtension(Extension):

    def __init__(self):
        super(GCPLauncherExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        actions = list()
        query = event.get_argument() or ""

        array = [
            [
                "Dashboard",
                OpenUrlAction("https://console.cloud.google.com/home/dashboard"),
                "images/gcp_logo.png"
            ],
            [
                "Compute Engine",
                OpenUrlAction("https://console.cloud.google.com/compute"),
                "images/compute_icon.png"
            ],
            [
                "Kubernetes Engine",
                OpenUrlAction("https://console.cloud.google.com/kubernetes"),
                "images/kube_icon.png"
            ],
            [
                "Cloud SQL",
                OpenUrlAction("https://console.cloud.google.com/sql"),
                "images/sql_icon.png"
            ],
            [
                "App Engine",
                OpenUrlAction("https://console.cloud.google.com/appengine"),
                "images/app_engine_icon.png"
            ],
            [
                "Cloud Functions",
                OpenUrlAction("https://console.cloud.google.com/functions"),
                "images/cloud_functions_icon.png"
            ],
            [
                "Datastore",
                OpenUrlAction("https://console.cloud.google.com/datastore"),
                "images/datastore.png"
            ],
            [
                "BigQuery",
                OpenUrlAction("https://console.cloud.google.com/bigquery"),
                "images/big_query.png"
            ],
            [
                "Storage",
                OpenUrlAction("https://console.cloud.google.com/storage"),
                "images/storage_icon.png"
            ],
            [
                "VPC Network",
                OpenUrlAction("https://console.cloud.google.com/networking"),
                "images/vpc_network_icon.png"
            ],
            [
                "Network Services",
                OpenUrlAction("https://console.cloud.google.com/net-services"),
                "images/network_services_icon.png"
            ],
            [
                "Cloud Build",
                OpenUrlAction("https://console.cloud.google.com/cloud-build"),
                "images/build_icon.png"
            ],
            [
                "Container Registry",
                OpenUrlAction("https://console.cloud.google.com/gcr"),
                "images/container_registry_icon.png"
            ],
            [
                "Security",
                OpenUrlAction("https://console.cloud.google.com/security"),
                "images/security_icon.png"
            ],
            [
                "IAM Admin",
                OpenUrlAction("https://console.cloud.google.com/iam-admin"),
                "images/iam_admin_icon.png"
            ],
            [
                "Filestore",
                OpenUrlAction("https://console.cloud.google.com/filestore"),
                "images/filestore_icon.png"
            ],
            [
                "Stackdriver Logging",
                OpenUrlAction("https://console.cloud.google.com/logs"),
                "images/logging_icon.png"
            ],
            [
                "Stackdriver Monitoring",
                OpenUrlAction("https://console.cloud.google.com/monitoring"),
                "images/monitoring_icon.png"
            ],
            [
                "Billing",
                OpenUrlAction("https://console.cloud.google.com/billing"),
                "images/billing_icon.png"
            ],
            [
                "Marketplace",
                OpenUrlAction("https://console.cloud.google.com/marketplace"),
                "images/marketplace_icon.png"
            ],
            [
                "Pricing Calculator",
                OpenUrlAction("https://cloud.google.com/products/calculator"),
                "images/pricing_calculator_icon.png"
            ]
        ]

        if query != "":
           array = [x for x in array if query.lower() in x[0].lower()]

        for val in array:
            actions.append(
                ExtensionResultItem(name=val[0], on_enter=val[1], icon=val[2])
            )

        return RenderResultListAction(actions)

if __name__ == '__main__':
    GCPLauncherExtension().run()
