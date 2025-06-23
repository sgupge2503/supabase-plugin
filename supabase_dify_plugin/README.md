# Supabase Plugin for Dify

This plugin provides a simple tool and endpoint to query rows from a Supabase table.

## Development

Install dependencies:

```bash
pip install -r requirements.txt
```

To run the plugin locally:

```bash
python main.py
```

## Credentials

Set the following credentials when installing the plugin in Dify:

- `supabase_url` – Your Supabase project URL
- `supabase_key` – A service role or anon key

### Packaging

To create a `.difypkg` file run:

```bash
zip -r supabase_plugin-0.0.1.difypkg . -x '__pycache__/*'
```
