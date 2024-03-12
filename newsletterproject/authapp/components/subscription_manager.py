from django_unicorn.components import UnicornView


class SubscriptionManagerView(UnicornView):
    subscription_status = False
    subscription_tier = ""
    message = ""

    def mount(self):
        # Use mount to initialize values that depend on the request
        self.subscription_status = self.request.user.subscription.status
        self.subscriptionn_tier = self.request.user.subscription.tier

    def unsubscribe(self):
        user = self.request.user
        user.subscription.status = False
        user.subscription.save()
        self.subscription_status = False
        self.message = "You have successfully unsubscribed from our newsletter."
        self.call("hideAlertAfterDelay")
        
    def subscribe(self):
        user = self.request.user
        user.subscription.status = True
        user.subscription.save()
        self.subscription_status = True
        self.message = "You have successfully subscribed to our newsletter."
        self.call("hideAlertAfterDelay")