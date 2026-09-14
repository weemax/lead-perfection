"""Minimal end-to-end example: authenticate, then call two endpoints.

Credentials are read from the environment so they never live in source
control. Copy .env.example to .env, fill it in, and run:

    python example.py
"""

import os
from pathlib import Path

import lead_perfection as lp

REQUIRED_VARS = (
    'LP_SERVER_ID',
    'LP_CLIENT_ID',
    'LP_USERNAME',
    'LP_PASSWORD',
    'LP_APP_KEY',
)


def load_dotenv(path: Path) -> None:
    """Load KEY=VALUE lines from a .env file without overriding the real environment."""
    if not path.is_file():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, _, value = line.partition('=')
        os.environ.setdefault(key.strip(), value.strip().strip('"\''))


def main() -> None:
    load_dotenv(Path(__file__).parent / '.env')

    missing = [name for name in REQUIRED_VARS if not os.environ.get(name)]
    if missing:
        raise SystemExit(
            f"Missing credentials: {', '.join(missing)}.\n"
            "Copy .env.example to .env and fill it in."
        )

    client = lp.client.Client(
        os.environ['LP_SERVER_ID'],
        os.environ['LP_CLIENT_ID'],
        os.environ['LP_USERNAME'],
        os.environ['LP_PASSWORD'],
        os.environ['LP_APP_KEY'],
    )

    server_id = client.server_id
    access_token = client.authenticate()['access_token']
    print('Authenticated against', server_id)

    lp_menu = lp.menu.Menu(server_id=server_id, access_token=access_token)
    print('Menu Result:', lp_menu.get_menu())

    lp_leads = lp.leads.Leads(server_id=server_id, access_token=access_token)
    print('Leads Confirmed Message Result:', lp_leads.get_leads_confirmed_message())


if __name__ == '__main__':
    main()
