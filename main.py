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
                "images/sql_icon.png"
            ],
            [
                "Cloud Functions",
                OpenUrlAction("https://console.cloud.google.com/functions"),
                "images/sql_icon.png"
            ],
            [
                "Storage",
                OpenUrlAction("https://console.cloud.google.com/storage"),
                "images/sql_icon.png"
            ],
            [
                "VPC Network",
                OpenUrlAction("https://console.cloud.google.com/networking"),
                "images/sql_icon.png"
            ],
            [
                "Network Services",
                OpenUrlAction("https://console.cloud.google.com/net-services"),
                "images/sql_icon.png"
            ],
            [
                "Cloud Build",
                OpenUrlAction("https://console.cloud.google.com/cloud-build"),
                "images/sql_icon.png"
            ],
            [
                "Container Registry",
                OpenUrlAction("https://console.cloud.google.com/gcr"),
                "images/sql_icon.png"
            ],
            [
                "Security",
                OpenUrlAction("https://console.cloud.google.com/security"),
                "images/gcp_logo.png"
            ],
            [
                "Billing",
                OpenUrlAction("https://console.cloud.google.com/billing"),
                "images/gcp_logo.png"
            ],
            [
                "IAM & Admin",
                OpenUrlAction("https://console.cloud.google.com/iam-admin"),
                "images/gcp_logo.png"
            ],
            [
                "Marketplace",
                OpenUrlAction("https://console.cloud.google.com/marketplace"),
                "images/gcp_logo.png"
            ],
            [
                "Pricing Calculator",
                OpenUrlAction("https://cloud.google.com/products/calculator"),
                "images/gcp_logo.png"
            ]
        ]

        for val in array:
            actions.append(
                ExtensionResultItem(name=val[0], on_enter=val[1], icon=val[2])
            )

        return RenderResultListAction(actions)

if __name__ == '__main__':
    GCPLauncherExtension().run()
