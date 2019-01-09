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
                OpenUrlAction("https://console.cloud.google.com/compute/"),
                "images/compute_icon.png"
            ],
            [
                "Kubernetes Engine",
                OpenUrlAction("https://console.cloud.google.com/kubernetes/"),
                "images/kube_icon.png"
            ],
            [
                "Cloud SQL",
                OpenUrlAction("https://console.cloud.google.com/sql/"),
                "images/sql_icon.png"
            ],
            [
                "Pricing Calculator",
                OpenUrlAction("https://cloud.google.com/products/calculator/"),
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
