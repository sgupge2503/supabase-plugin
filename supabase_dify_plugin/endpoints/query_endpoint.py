import json
from typing import Mapping
from werkzeug import Request, Response
from dify_plugin import Endpoint

class QueryEndpoint(Endpoint):
    def _invoke(self, r: Request, values: Mapping, settings: Mapping) -> Response:
        data = r.get_json() or {}
        table = data.get('table')
        limit = data.get('limit', 10)
        tool_resp = self.session.tool.invoke_builtin_tool(
            'codex/supabase_plugin/supabase_plugin',
            'query_table',
            parameters={'table': table, 'limit': limit}
        )
        rows = None
        for chunk in tool_resp:
            if chunk.type.value == 'variable' and chunk.message.variable_name == 'rows':
                rows = chunk.message.variable_value
            elif chunk.type.value == 'text':
                return Response(
                    response=json.dumps({'error': chunk.message.text}),
                    status=400,
                    content_type='application/json'
                )
        return Response(
            response=json.dumps({'rows': rows}),
            status=200,
            content_type='application/json'
        )
