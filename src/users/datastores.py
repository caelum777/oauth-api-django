from oauth2_provider.models import Application


def get_client_tokens():
    application = Application.objects.get(name="users2")
    return {"client_id": application.client_id, "client_secret": application.client_secret}
