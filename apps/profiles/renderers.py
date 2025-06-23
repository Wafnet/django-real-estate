import json
from rest_framework.renderers import JSONRenderer

class ProfileJSONRenderer(JSONRenderer):
    """
    Custom JSON renderer for the Profile API.
    """
    charset = 'utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = data.get('errors', None)
        if errors is not None:
            return super(ProfileJSONRenderer, self).render(data)
        return json.dumps({
            'profile': data
        })