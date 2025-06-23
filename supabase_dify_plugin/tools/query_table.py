from typing import Any, Dict, Generator

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from supabase import create_client, Client

class QueryTableTool(Tool):
    def __init__(self, runtime, session):
        super().__init__(runtime=runtime, session=session)
        self.client: Client | None = None

    def init_client(self):
        if self.client is None:
            url = self.runtime.credentials.get('supabase_url')
            key = self.runtime.credentials.get('supabase_key')
            self.client = create_client(url, key)

    def _invoke(self, parameters: Dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        table = parameters.get('table')
        limit = int(parameters.get('limit', 10))
        if not table:
            yield self.create_text_message('missing table parameter')
            return
        try:
            self.init_client()
            result = self.client.table(table).select('*').limit(limit).execute()
            yield self.create_variable_message('rows', result.data)
        except Exception as e:
            yield self.create_text_message(str(e))
