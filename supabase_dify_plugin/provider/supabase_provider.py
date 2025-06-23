from typing import Dict, Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class SupabaseProvider(ToolProvider):
    def __init__(self):
        super().__init__()

    def _validate_credentials(self, credentials: Dict[str, Any]) -> None:
        url = credentials.get('supabase_url')
        key = credentials.get('supabase_key')
        if not url:
            raise ToolProviderCredentialValidationError('supabase_url is required')
        if not key:
            raise ToolProviderCredentialValidationError('supabase_key is required')
